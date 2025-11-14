"""This module provides the command line interface of the multiscale-run
console-scripts entrypoint of the Python package (see setup.py)

The CLI provides the required commands to create a run simulations.
"""

import argparse
import copy
import functools
import json
import logging
import os
import platform
import shutil
import stat
import subprocess
import textwrap
import warnings
from pathlib import Path

import scipy.sparse
from nbconvert.nbconvertapp import main as NbConvertApp

from . import __version__
from .config import DEFAULT_CIRCUIT, NAMED_CIRCUITS
from .simulation import MsrSimulation
from .templates import MSR_CONFIG_JSON, MSR_POSTPROC, SBATCH_TEMPLATE
from .utils import MsrException, copy_symlinks, merge_dicts, pushd


def _cli_logger():
    logger = logging.getLogger("cli")
    logger.setLevel(logging.WARN)
    ch = logging.StreamHandler()
    formatter = logging.Formatter("࿋ %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.propagate = False
    return logger


LOGGER = _cli_logger()
del _cli_logger


def command(func):
    """Decorator for every command functions"""
    # extract first line of function docstring, and use it
    # for --help description
    func_doc = func.__doc__ or ""
    func.__argparse_help__ = func_doc.split("\n", 1)[0]

    @functools.wraps(func)
    def wrap(directory=None, **kwargs):
        directory = Path(directory or ".")
        directory.mkdir(parents=True, exist_ok=True)
        with pushd(directory):
            return func(directory=directory, **kwargs)

    return wrap


@command
def init(directory, circuit, check=True, force=False, metabolism="standard"):
    """Setup a new simulation"""

    if not force:
        dir_content = set(Path(".").iterdir())
        dir_content.discard(Path(".logs"))
        if dir_content:
            raise MsrException(
                f"Directory '{directory}' is not empty. "
                "Use option '-f' to overwrite the content of the directory."
            )
    assert metabolism in ["standard", "young", "aged"]

    circuit_def = NAMED_CIRCUITS[circuit]

    sbatch_parameters = copy.copy(circuit_def.sbatch_parameters)
    loaded_modules = filter(lambda s: len(s) > 0, os.environ.get("LOADEDMODULES", "").split(":"))
    sbatch_parameters["loaded_modules"] = loaded_modules
    SBATCH_TEMPLATE.stream(sbatch_parameters).dump("simulation.sbatch")
    shutil.copy(MSR_POSTPROC, MSR_POSTPROC.name)
    shutil.copy(circuit_def.path / "simulation_config.json", ".")
    shutil.copy(circuit_def.path / "circuit_config.json", ".")
    shutil.copy(circuit_def.path / "node_sets.json", ".")
    copy_symlinks(circuit_def.path, ".")

    rd = {"msr_version": str(__version__)}

    circuit_config = circuit_def.json()
    if metabolism != "standard":
        p_split = circuit_config["multiscale_run"]["metabolism"]["julia_code_path"].rsplit(".", 1)
        rd.setdefault("metabolism", {})["julia_code_path"] = (
            f"{p_split[0]}_{metabolism}.{p_split[1]}"
        )

    circuit_config = merge_dicts(child={"multiscale_run": rd}, parent=circuit_config)
    with open(MSR_CONFIG_JSON, "w") as ostr:
        json.dump(circuit_config, ostr, indent=4)

    LOGGER.warning("Preparation of the simulation configuration and environment succeeded")
    LOGGER.warning(
        "The generated setup is already ready to compute "
        "with the command 'multiscale-run compute' or via the "
        "generated sbatch file. But feel free to browse and tweak "
        "the JSON configuration files at will!"
    )

    LOGGER.warning(f'Set up with circuit: "{circuit}" and metabolism type: "{metabolism}"')
    folder_path = os.path.abspath(directory)
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        LOGGER.warning(f"Folder: {os.path.abspath(directory)}")
        content = os.listdir(folder_path)
        LOGGER.warning(
            f"Contents of the folder {folder_path}:\n" + "\n".join(f"- {item}" for item in content)
        )
    else:
        LOGGER.warning(f"Directory: {directory}")
    return directory


@command
def compute(**kwargs):
    """Compute the simulation"""
    _check_local_neuron_mechanisms()
    sim = MsrSimulation()
    sim.main()


@command
def stats(**kwargs):
    """Get some stats from a simulation"""
    MsrSimulation.stats()


@command
def check(**kwargs):
    """Check environment sanity"""
    sane = True
    LOGGER.warning("Running minimalist checks to test environment sanity")
    sim = MsrSimulation()
    sim.configure()

    sane &= _check_local_neuron_mechanisms()

    if sane:
        LOGGER.warning("The simulation environment looks sane")
    else:
        LOGGER.warning("Inconsistencies have been spotted")
        MsrException("Environment sanity check failed")


@command
def post_processing(notebook: str, **kwargs) -> Path:
    """Execute a Jupyter notebook over the simulation results to generate an HTML document

    Returns
      Path to the created HTML report
    """
    from .config import MsrConfig

    conf = MsrConfig()
    results = str(conf.output.output_dir)
    NbConvertApp(["--execute", "--to", "html", "--no-input", f"--output-dir={results}", notebook])
    return Path(results) / (Path(notebook).stem + ".html")


def _check_local_neuron_mechanisms():
    """Perform sanity check in case the mod files library has been cloned in the
    simulation directory for local editing.

    Returns
       False if something smelly has been identified, True otherwise
    """
    sane = True
    mod_files = Path("mod")
    if not mod_files.exists():
        return sane

    mod_files_mtime = max(entry.stat()[stat.ST_MTIME] for entry in os.scandir(mod_files))

    for ext in [".so", ".dll", ".dylib"]:
        nrn_mechanisms = Path(platform.machine()) / ("libnrnmech" + ext)
        if nrn_mechanisms.exists():
            break
    if not nrn_mechanisms.exists() or nrn_mechanisms.stat()[stat.ST_MTIME] < mod_files_mtime:
        sane = False
        LOGGER.warning(
            textwrap.dedent(
                f"""\
            Content of 'mod' directory is more recent that Neuron mechanisms file {nrn_mechanisms}.
            Consider rebuilding it with the following command:

                cd {os.getcwd()}
                build_neurodamus.sh mod
        """
            )
        )

    if nrn_mechanisms.exists():
        env_nrn_mechanisms = os.environ.get("NRNMECH_LIB_PATH")
        if env_nrn_mechanisms != str(nrn_mechanisms.resolve()):
            sane = False
            LOGGER.warning(
                textwrap.dedent(
                    f"""
                A custom version of Neuron mechanisms library have been detected
                    in the simulation directory: {nrn_mechanisms.resolve()}
                but the NRNMECH_LIB_PATH environment variable is not pointing it.
                To use it, you may define the environment variable as follow

                    export NRNMECH_LIB_PATH={nrn_mechanisms.resolve()}
            """
                )
            )
    return sane


@command
def edit_mod_files(**kwargs):
    """Clone the Neurodamus mod files library for local editing

    1. $ cp -r $NEURODAMUS_NEOCORTEX_ROOT ./mod
    2. $ build_neurodamus.sh
    3. Patch simulation.sbatch to override NEURODAMUS_NEOCORTEX_ROOT
    4. Write instructions to the console

    """
    if Path("mod").exists():
        raise MsrException("Directory 'mod' already exists. Remove it first to reinitialize it")

    if (ndam_root := os.environ.get("NEURODAMUS_NEOCORTEX_ROOT")) is None:
        raise MsrException("Environment variable 'NEURODAMUS_NEOCORTEX_ROOT' is missing")
    if os.environ.get("NRNMECH_LIB_PATH") is None:
        raise MsrException("Environment variable 'NRNMECH_LIB_PATH' is missing")
    ndam_mod = Path(ndam_root) / "share" / "neurodamus_neocortex" / "mod"
    if not ndam_mod.exists():
        raise MsrException(f"Directory '{ndam_mod}' does not exist")

    print("copying neocortex mod files library locally")
    shutil.copytree(ndam_mod, "mod")
    print("building local mod files")
    build_cmd = f"build_neurodamus.sh '{ndam_mod}' --only-neuron"
    subprocess.check_call(build_cmd, shell=True)
    nrn_mechanims = (Path(platform.machine()) / "libnrnmech.so").resolve()
    if not nrn_mechanims.exists():
        raise MsrException(
            f"Missing file expected to be built by 'build_neurodamus.sh': '{nrn_mechanims}'"
        )

    sbatch_script = Path("simulation.sbatch")
    if sbatch_script.exists():
        with sbatch_script.open() as istr:
            content = istr.read()
        if "export NRNMECH_LIB_PATH" not in content:
            print(f"Patching {sbatch_script} to take the new Neuron mechanisms into account")
            content = content.replace(
                "-----\n\n",
                f"-----\n\n# Use local Neuron mechanisms\nexport NRNMECH_LIB_PATH={nrn_mechanims}\n\n",
            )
            with sbatch_script.open("w") as ostr:
                ostr.write(content)
    else:
        LOGGER.warning(f"Could not find '{sbatch_script}. Skip patching")

    print(
        textwrap.dedent(
            f"""\
        Neuron mechanisms have been successfully built.
        Define the following environment variable to take them into account during multiscale-run simulations:

            export NRNMECH_LIB_PATH={nrn_mechanims}

        Whenever you modify the mod files, launch this command to rebuild the mechanisms:

            cd {os.getcwd()}
            build_neurodamus.sh mod --only-neuron

        Happy hacking!
    """
        )
    )


def argument_parser():
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    ap.add_argument("--verbose", "-v", action="count", default=0)
    subparsers = ap.add_subparsers(title="commands")

    parser_init = subparsers.add_parser("init", help=init.__argparse_help__)
    parser_init.set_defaults(func=init)
    parser_init.add_argument(
        "--circuit",
        choices=sorted(list(NAMED_CIRCUITS)),
        default=DEFAULT_CIRCUIT,
    )
    parser_init.add_argument(
        "-f",
        "--force",
        default=False,
        action="store_true",
        help="Force files creations if directory already exists",
    )
    parser_init.add_argument(
        "--metabolism",
        choices=["standard", "young", "aged"],
        default="standard",
        help="Choose Metabolism type. ",
    )
    parser_init.add_argument(
        "--no-check",
        action="store_const",
        const=False,
        default=True,
        dest="check",
        help="Do not verify simulation health",
    )
    parser_init.add_argument("directory", nargs="?")

    parser_check = subparsers.add_parser("check", help=check.__argparse_help__)
    parser_check.set_defaults(func=check)
    parser_check.add_argument("directory", nargs="?")

    parser_compute = subparsers.add_parser("compute", help=compute.__argparse_help__)
    parser_compute.set_defaults(func=compute)
    parser_compute.add_argument("directory", nargs="?")

    parser_stats = subparsers.add_parser("stats", help=stats.__argparse_help__)
    parser_stats.set_defaults(func=stats)
    parser_stats.add_argument("directory", nargs="?")

    parser_postproc = subparsers.add_parser(
        "post-processing", help=post_processing.__argparse_help__
    )
    parser_postproc.set_defaults(func=post_processing)
    parser_postproc.add_argument(
        "--notebook",
        default=MSR_POSTPROC.name,
        help="path to the Jupyter notebook to execute. Default is %(default)s",
    )
    parser_postproc.add_argument("directory", nargs="?")

    parser_edit_mod_files = subparsers.add_parser(
        "edit-mod-files", help=edit_mod_files.__argparse_help__
    )
    parser_edit_mod_files.set_defaults(func=edit_mod_files)
    parser_edit_mod_files.add_argument("directory", nargs="?")

    return ap


def main(**kwargs):
    """Package script entry-point for the multiscale-run CLI utility.

    Args:
        kwargs: optional arguments passed to the argument parser.
    """
    from .utils import comm, size

    ap = argument_parser()
    args = ap.parse_args(**kwargs)
    args = vars(args)

    warnings.filterwarnings("ignore", category=scipy.sparse.SparseEfficiencyWarning)

    verbosity = args.pop("verbose")
    log_level = logging.WARN
    if verbosity == 1:
        log_level = logging.INFO
    elif verbosity > 1:
        log_level = logging.DEBUG
    logging.basicConfig(level=log_level)

    if callback := args.pop("func", None):
        try:
            callback(**args)
        except Exception as e:
            LOGGER.error(str(e), exc_info=True)
            if size() > 1:
                comm().Abort(errorcode=1)
            else:
                raise MsrException(str(e))
    else:
        ap.error("a subcommand is required.")
