import os
import sys

sys.path.insert(0, os.path.abspath("."))

import importlib.metadata

# -- Project information -----------------------------------------------------

project = "MultiscaleRun"
author = "Open Brain Institute / BBP HPC"

# Acknowledgment for funding and support
acknowledgment = """
The development of this software was supported by funding to the Blue Brain Project,
a research center of the École polytechnique fédérale de Lausanne (EPFL),
from the Swiss government's ETH Board of the Swiss Federal Institutes of Technology.

Copyright (c) 2005-2023 Blue Brain Project/EPFL
Copyright (c) 2025 Open Brain Institute
"""

# The full version, including alpha/beta/rc tags
version = importlib.metadata.version("multiscale_run")
release = version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx_mdinclude",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["**/metadata.md", "build/**"]
suppress_warnings = ["docutils", "image.not_readable", "ref.ref"]

doctest_global_setup = """
from multiscale_run.config import MsrConfig
config = MsrConfig._from_dict(
    {
        "run": MsrConfig._from_dict({"dt": 0.1, "tstop": 1.0}),
        "multiscale_run": MsrConfig._from_dict(
            {
                "ndts": 1,
                "connections": [],
                "with_steps": False,
                "with_bloodflow": False,
                "with_metabolism": False,
            }
        ),
    }
)
def gen_mesh():
    pass
def gen_node_sets():
    pass
"""


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "obi_sphinx_theme"
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/openbraininstitute/MultiscaleRun",
            "icon": "fa-brands fa-github",
        },
    ],
    "navbar_align": "left",
}

# Output file base name for HTML help builder.

autodoc_mock_imports = ["neurodamus", "mpi4py", "nbconvert"]
htmlhelp_basename = "python_doc"

autoclass_content = "both"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
