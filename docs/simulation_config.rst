Simulation Configuration
========================

This document describes the various configurations available in `simulation_config.json` in the section `multiscale_run`. The general documentation about SONATA Simulation Configuration file `here <https://sonata-extension.readthedocs.io/en/latest/>`_.

Paths
=====

A configuration key with *_path* suffix is considered as a filesystem path.
Paths are resolved and you can use keys that you defined elsewhere in the file. For example:

.. code-block::

  {
      "custom_path": "foo0",
      "new_path": "${custom_path}/foo1"
  }

`new_path` is resolved into: `foo0/foo1`.

You can also use `${pkg_data_path}` to point to a location in the MultiscaleRun installation folder.

Base section
==============

This is the base section that configures the parameters to run MultiscaleRun simulations.

- **with_steps**: Boolean. Indicates whether the STEPS simulator is enabled. It computes the extracellular reactions/diffusions of the molecules. Currently only `false` is accepted (triple-run not supported).
- **with_bloodflow**: Boolean. Indicates whether the AstroVascPy simulator is enabled. It computes the blood flows and volumes inside the vasculature. Currently only `false` is accepted (quad-run not supported).
- **with_metabolism**: Boolean. Indicates whether the Metabolism simulator is enabled. It computes the metabolism of the neurons (ATP/ADP etc. generation/consumption). This is the only additional simulator currently supported alongside Neurodamus (dual-run).
- **cache_save**: Boolean. If true, some simulation matrices are cached on the filesystem. It greatly speeds up initialization in future simulations.
- **cache_load**: Boolean. If true, some simulation matrices are loaded from the cache, if present. Used in conjunction with `cache_save`.
- **logging_level**: Integer. Defines the verbosity level of Neurodamus logs.
- **mesh_path**: String. Path to the mesh file used in simulations, e.g., "mesh/autogen_mesh.msh".
- **cache_path**: String. Filesystem location where the cached files are stored, e.g., "cache".
- **mesh_scale**: Float. Scale factor applied to the mesh dimensions, typically in the order of 1e-6.
- **config_format**: Integer. Specifies the configuration format version. Current version is 3.
- **msr_version**: String. Indicates the version of the MultiscaleRun that created this file, e.g., "1.0".
- **ndts**: Optional, Integer. Main MultiscaleRun iteration time step. Measured in Neurodamus time steps. If no entry is provided the one is calculated for you based on the time steps of the various simulators. It is suggested to let the program decide.

Preprocessor
==============

- **mesh**: This collects all the parameters required to let MultiscaleRun generates the mesh (necessary for STEPS and some connections among simulators). A custom mesh can be provided in the `mesh` folder. In that case the custom mesh is used instead.

  - **explode_factor**: Float. With 1 the auto-generating-mesh routine creates cube that touches the convex hull of all the segment extremities of the vasculature and the neurons. We need something slightly bigger to be sure of encompassing everything in the mesh. Usually kept at 1.001.
  - **base_length**: Float. Base length of mesh elements.
  - **refinement_steps**: Integer. Number of refinement steps applied to the mesh. Currently Omega_h fails if the number of tetrahedra is less than the number of ranks.

- **node_sets**

  - **filter_neuron**: Boolean. Determines if the neurons connected to astrocytes must be filtered out when generating the mesh.
  - **neuron_population_name**: String. Name of the neuron population to use. Typically: "All".
  - **astrocyte_population_name**: String. Name of the astrocyte population to use. Typically: "astrocytes".

Connections among simulators
============================

The section **connections** describes how data is exchanged between different simulators. Simulations advance by alternating between simulators, each progressing according to its own time step.

Users can define connections between simulators using a list of dicts. When multiple connections apply, their order matters: the last connection in the list takes priority.

<<<<<<< HEAD
Each connection specifies a source simulator `src_simulator` and a destination simulator `dest_simulator`. By default, data is exchanged whenever the internal times of both simulators coincide.

This behavior can be customized with the `ndts` parameter, allowing connections to synchronize simulators with differing internal times. This is particularly useful in hybrid integration schemes, where data may propagate backward in time to update simulators that have not yet reached the corresponding time step.
=======
- **after_metabolism_advance**: Connections executed after metabolism advances (dual-run)
- **after_steps_advance**: Connections executed after STEPS advances (not currently supported)
- **before_bloodflow_advance**: Connections executed before bloodflow advances (not currently supported)

Keys different from the list provided are disregarded and a warning is emitted. Currently, only `after_metabolism_advance` is functional for dual-run simulations.
>>>>>>> main

Configuration specification
---------------------------

.. note::
<<<<<<< HEAD
   When working with metabolism connections, you do not need to set indexes explicitly. However, you may need to reference them by name. The available indexes are defined in ``multiscale_run/metabolism/indexes.py`` as two singleton objects: ``PIdx`` (parameter indexes) and ``UIdx`` (variable indexes). For example, ``UIdx.atp_i_n`` corresponds to index 13 for neuronal intracellular ATP. In the future multiscale run will give you a rundown of the accepted indexes.
=======
   When working with metabolism connections, you do not need to set indexes explicitly. However, you may need to reference them by name. The available indexes are defined in ``multiscale_run/metabolism/indexes.py`` as two singleton objects: ``PIdx`` (parameter indexes) and ``UIdx`` (variable indexes). For example, ``UIdx.atp_i_n`` corresponds to index 13 for neuronal intracellular ATP.
>>>>>>> main

Each connection must specify:

- **src_simulator**: String. Simulator, source of the values that need to be synced. Possible values are "neurodamus", "steps", "bloodflow", or "metabolism".
- **src_get_func**: String. Getter function for the source simulator.
- **src_get_kwargs**: Dict. Inputs for the getter function for the source simulator.
- **dest_simulator**: String. Simulator, destination of the values that need to be synced. Possible values are "neurodamus", "steps", "bloodflow", or "metabolism". It is very probably the same simulator mentioned as the key of the current connection.
- **dest_get_func**: String. Setter function to the destination simulator.
- **dest_get_kwargs**: Dict. Inputs for the setter function for the destination simulator.
- **action**: String. Sync action type. It may be:

  - **set**: values from the source simulator are set into the destination simulator overriding what was there before.
  - **sum**: values from the source simulator are added to the destination simulator values.
  - **merge**: deltas (compared to the previous time step value of the destination simulator) for source and destination
    simulators are computed and added together to merge the results.
    This is typically used for syncing Neurodamus and Metabolism: Neurodamus consumes ATP while Metabolism generates ATP.
    This merging mechanism reconciles the 2 simulators every time Metabolism advances. Notice that this is the only
    syncing action that may change the values for the source simulator too. In that case also the following keys are required:

    - **src_set_func**: String. Setter function for the source simulator.
    - **src_set_kwargs**: Dict. Inputs for the Setter function for the source simulator.
    - **dest_get_func**: String. Getter function to the destination simulator.
    - **dest_get_kwargs**: Dict. Inputs for the getter function for the destination simulator.

Optionally, the user may specify:

- **src_set_func** and  **src_set_kwargs**: in this case, the final value is also set in the source simulator (this field is required for the `merge` action).
- **transform_expression**: additional custom operations that may be performed on the values before setting them in the simulators. More on this in: :ref:`data transformation <data_transformation_label>`.
- `ndts`: if set it overrides the standard connection timing where the simulators connect when their times coincide.

Concrete example
----------------

.. code-block:: json

    {
<<<<<<< HEAD
        "connections": [
            {
                "src_simulator": "neurodamus",
                "src_get_func": "get_var",
                "src_get_kwargs": {"var": "atpi", "weight": "volume"},
                "src_set_func": "set_var",
                "src_set_kwargs": {"var": "atpi"},
                "dest_simulator": "metabolism",
                "dest_get_func": "get_vm_idx",
                "dest_get_kwargs": {"idx": "atp_c_n"},
                "dest_set_func": "set_vm_idxs",
                "dest_set_kwargs": {"idxs": "atp_c_n"},
                "action": "merge"
            }
        ]
=======
        "connections": {
            "after_metabolism_advance": [
                {
                    "src_simulator": "neurodamus",
                    "src_get_func": "get_var",
                    "src_get_kwargs": {"var": "atpi", "weight": "volume"},
                    "src_set_func": "set_var",
                    "src_set_kwargs": {"var": "atpi"},
                    "dest_simulator": "metabolism",
                    "dest_get_func": "get_vm_idx",
                    "dest_get_kwargs": {"idx": "atp_c_n"},
                    "dest_set_func": "set_vm_idxs",
                    "dest_set_kwargs": {"idxs": "atp_c_n"},
                    "action": "merge"
                }
            ]
        }
>>>>>>> main
    }

In the previous block MultiscaleRun is instructed to `merge` (the action) the values from Neurodamus and Metabolism simulators (just after Metabolism calls `advance`). It follows the equation:

.. math::

    a_{n_{\text{metabolism}}+1} = a_{\text{metabolism} \; n_{\text{metabolism}}+1} + a_{\text{neurodamus} \; n_{\text{metabolism}}+1} - a_{n_{\text{metabolism}}}

All these values are based on the time step of Metabolism. :math:`n_{\text{metabolism}}` is the n\ :sup:`th` time step for Metabolism. The reconciled value at :math:`n_{\text{metabolism}}+1` is equal to the value from Metabolism plus the value from Neurodamus minus the previous reconciled value.

The remaining keys indicate functions and arguments for setters and getters for both source and destination. For example, to set the values to the destination we use the function `set_vm_idxs` and its arguments are: `"idxs": "atp_c_n"`. The index name `"atp_c_n"` is automatically resolved to its numeric value (see the note above about metabolism indexes).

.. _data_transformation_label:

Data transformation
-------------------

It is possible to specify data transformation operations when sending values from one simulator to another with the **conversion** JSON object. It is a python expression whose result overrides the data transferred and can be specified in the **transform_expression** configuration key.
The Python expression is executed in a restricted environment where only few symbols are usable:

- `vals`: the data being transferred
- `config`: the JSON configuration object
- `math`: the module from the standard library
- `np`: the NumPy module
- the computational Python builtins: `abs`, `min`, `max`, `pow`, `round`, and `sum`

In addition, a few matrices are available to perform the various averages that are likely required:

- **nXsecMat**: neuron x section matrix. ``nXsecMat.dot(vals)`` does the volume-weighted average of the section-based values in ``vals``. Adimensional. Each element is: ``V_j / V_i`` where ``V_i`` is the total volume of the neuron and ``V_j`` is the volume of the section. Neurons and sections are local to the MPI rank.
- **nsecXnsegMat**: neuron section x neuron segment matrix. ``nsecXnsegMat.dot(vals)`` does the volume-weighted average of the section-based values in ``vals``. Adimensional. Each element is: ``V_j / V_i`` where ``V_i`` is the total volume of the section and ``V_j`` is the volume of the segment. Sections and segments are local to the rank.
- **nXnsegMatBool**: ``nXnsegMatBool = nXsecMat.dot(nsecXnsegMat) > 0``
- **nsegXtetMat**: neuron segment x tet matrix. Adimensional. Each element is ``V_seg_in_tet_ij / V_seg_i`` where ``V_seg_in_tet`` is the volume of the neuron segment ``i`` in tet ``j`` and ``V_seg_i`` is the volume of the neuron segment ``i``. Tets are global while segments are local to the MPI rank. This means that each rank has a big row block of the total matrix.
- **tetXbfVolsMat**: tetrahedra x bloodflow segments matrix. Adimensional. Each element is ``V_seg_in_tet_ij / V_seg_i`` where ``V_seg_in_tet`` is the volume of the bloodflow segment ``i`` in tet ``j`` and ``V_seg_i`` is the volume of the bloodflow segment ``i``. Tets and bloodflow segments are global and the same matrix is shared among all the ranks.
- **tetXbfFlowsMat**: tetrahedra x bloodflow segments matrix. Bool matrix that computes what are the flows entering or exiting a tet. Segments completely encompassed inside a tet are not counted except if they are inputs/outputs of the bloodflow simulator. Adimensional. Tets and bloodflow segments are global and the same matrix is shared among all the ranks.
- **tetXtetMat**: tetrahedra x tetrahedra matrix that rescales tet values to a reference, average tet. Adimensional and diagonal. Each element of the diagonal is: ``V_avg / V_i`` where ``V_avg`` is the volume of the average tet and ``V_i`` is the volume of the tet ``i``. Tets are global and the same matrix is shared among all the ranks.

Examples of valid expressions:

- ``vals * 1e-8`` - Simple scaling
- ``vals / 2 * (-0.92 + np.sqrt(0.92 * 0.92 + 4 * 0.92 * (1.4449961078157665 / vals - 1)))`` - Complex calculation for ADP from ATP
- ``abs(vals) * 5e-10`` - Absolute value with scaling
- ``nXsecMat.dot(vals)`` - Volume-weighted averaging across neuron sections

Full example of JSON connections with transformation:

.. code-block:: json

  {
    "connections": {
      [
        {
          "src_simulator": "neurodamus",
          "src_get_func": "get_var",
          "src_get_kwargs": {"var": "ina", "weight": "area"},
          "dest_simulator": "metabolism",
          "dest_set_func": "set_parameters_idxs",
          "dest_set_kwargs": {"idxs": "ina_density"},
          "action": "set"
        },
        {
          "src_simulator": "neurodamus",
          "src_get_func": "get_var",
          "src_get_kwargs": {"var": "atpi", "weight": "volume"},
          "transform_expression": "vals / 2 * (-0.92 + np.sqrt(0.92 * 0.92 + 4 * 0.92 * (1.4449961078157665 / vals - 1)))",
          "dest_simulator": "metabolism",
          "dest_set_func": "set_vm_idxs",
          "dest_set_kwargs": {"idxs": "adp_c_n"},
          "action": "set"
        }
      ]
    }
  }


Metabolism
==========

Parameters of the Metabolism simulator. The metabolism model is embedded in Python and uses constants defined in ``multiscale_run/metabolism/constants.py``.

- **ndts**: Integer. Time step of the simulator. Measured in number of Neurodamus time steps.
- **u0**: Dict. Initial values for the metabolism variables. Keys can be index names (e.g., ``"atp_c_n"``) from ``UIdx`` in ``multiscale_run/metabolism/indexes.py``. Empty dict uses default values from ``multiscale_run/metabolism/initial_conditions.py``.
- **constants**: Dict. Constants for the metabolism model organized by category. Each key is a category name (e.g., ``"ATDMP"``, ``"Glycogen"``, ``"GeneralConstants"``) corresponding to dataclasses in ``multiscale_run/metabolism/constants.py``. Values are dicts with parameter names and their values. Example:

  .. code-block:: json

      {
          "ATDMP": {
              "ATDPtot_n": 1.4449961078157665
          },
          "Glycogen": {
              "au": [128.0, 100.0, 100.0, 90.0, 80.0, 75.0]
          },
          "GeneralConstants": {
              "mito_volume_fraction": [0.0459, 0.0522, 0.064, 0.0774, 0.0575, 0.0403],
              "xNEmod": 0.025,
              "KdNEmod": 0.0003
          }
      }

- **parameters**: Dict. Initial parameter values for the metabolism model. Keys can be index names (e.g., ``"ina_density"``) from ``PIdx`` in ``multiscale_run/metabolism/indexes.py``. During initialization (before any advance), connections to metabolism may replace these values. In that case, the `merge` action is downgraded to a `set` action. Example:

  .. code-block:: json

      {
          "notBigg_FinDyn_W2017": 0.0001,
          "notBigg_Fout_W2017": 0.0001,
          "notBigg_vV_b_b": 0.023
      }

- **solver_kwargs**: Dict. Parameters for the ODE solver. The solver is currently ``Radau`` from scipy. Common parameters include ``method``, ``rtol``, ``atol``.
- **checks**: Dict. Checks performed on metabolism inputs (parameters and vm) at every metabolism time step to verify integrity. Items are optional. Parameters and variables not mentioned are still checked to be normal numbers (no inf, nan allowed). Structure:

  .. code-block:: json

      {
          "checks": {
              "parameters": {
                  "notBigg_FinDyn_W2017": {
                      "kwargs": {"leb": 0.0},
                      "response": "exclude_neuron"
                  }
              },
              "vm": {
                  "atp_c_n": {
                      "kwargs": {"lb": 0.25, "hb": 2.5},
                      "response": "abort_simulation"
                  }
              }
          }
      }

  - **parameters** / **vm**: Dict. Checks for parameters or variables respectively. Keys are index names (strings like ``"atp_c_n"`` or ``"notBigg_FinDyn_W2017"``).
  - **kwargs**: Dict. Checking routine arguments (optional entries):

    - **lb**: Float. Lower bound (exclusive): \(lb < v\)
    - **leb**: Float. Lower bound (inclusive): \(lb \leq v\)
    - **hb**: Float. Upper bound (exclusive): \(v < hb\)
    - **heb**: Float. Upper bound (inclusive): \(v \leq heb\)

  - **response**: String. Action if check fails:

    - **exclude_neuron**: Remove neuron from simulation. Simulation continues with remaining neurons. If no neurons remain (across all ranks), simulation aborts at end of MultiscaleRun iteration.
    - **abort_simulation**: Immediately abort the simulation.

STEPS (Disabled)
================

.. note::
   STEPS simulator is not currently supported (triple-run disabled). This section is kept for reference only.

Parameters for the STEPS simulator.

- **ndts**: Integer. Time step of the simulator. Measured in number of Neurodamus time steps.
- **conc_factor**: Float. Rescaling factor for the number of molecules. Necessary because the mesh is very coarse and STEPS may overflow.
- **compname**: String. Name of the `STEPS compartment <https://steps.sourceforge.net/manual/API_2/API_geom.html?highlight=compartment#steps.API_2.geom.Compartment>`_.
- **Volsys**: Dict. `System volume <https://steps.sourceforge.net/manual/API_2/API_model.html?highlight=volumesystem#steps.API_2.model.VolumeSystem>`_ parameters.
    - **name**: String. Name of the system volume. It needs to be the same that was used to create appropriate physical entity in the mesh.
    - **species**: Dict. Parameters of the reaction-diffusion species.
        - **conc_0**: Float. Initial concentration in `mM`.
        - **diffcst**: Float. `Diffusion <https://steps.sourceforge.net/manual/API_2/API_model.html?highlight=diffusion#steps.API_2.model.Diffusion>`_ constant in SI units.
        - **ncharges**: Integer. Charge number of the ion.

Blood Flow (Disabled)
=====================

.. note::
   Blood flow simulator is not currently supported (quad-run disabled). This section is kept for reference only.

Parameters for the blood flow simulator (AstroVascPy).

- **ndts**: Integer. Time step of the simulator. Measured in number of Neurodamus time steps.
- other parameters: `astrovascpy parameters <https://astrovascpy.readthedocs.io/latest/generated/astrovascpy.typing.html#astrovascpy.typing.VasculatureParams>`_.

Reports
=======

Parameters to report the simulation outcome. Currently, MultiscaleRun reports in the same folder as Neurodamus. The location is stated in `output.output_dir`. Here we try to mimic how Neurodamus reports so that the postprocessing can digest both MultiscaleRun and Neurodamus files. Example:

.. code-block:: json

    {
        "reports": {
            "metabolism": {
                "metab_ina": {
                    "src_get_func": "get_parameters_idx",
                    "src_get_kwargs": {"idx": "ina_density"},
                    "unit": "mA/cm^2",
                    "file_name": "metab_ina.h5",
                    "when": "after_sync"
                },
                "metab_atpi": {
                    "src_get_func": "get_vm_idx",
                    "src_get_kwargs": {"idx": "atp_c_n"},
                    "unit": "mM",
                    "file_name": "metab_atpi.h5",
                    "when": "after_sync"
                }
            }
        }
    }

- **src_get_func**: String. Getter function for the simulator. For metabolism, use ``get_parameters_idx`` for parameters or ``get_vm_idx`` for variables. Other options include ``alive_gids`` to report which neurons are still active.
- **src_get_kwargs**: Dict. Inputs for the getter function. For metabolism, use ``{"idx": "index_name"}`` where ``index_name`` is a string from ``PIdx`` (for parameters) or ``UIdx`` (for variables) defined in ``multiscale_run/metabolism/indexes.py``.
- **unit**: String. Units of the values in the report.
- **file_name**: String. Name of the HDF5 output file.
- **when**: String. Timing of the report relative to synchronization. Possible values:

  - **after_sync**: Report values after synchronization between simulators
  - **before_sync**: Report values before synchronization

  Multiple reports with different file names can capture both before and after sync states.

`bloodflow` reports are vasculature-segment-based (not currently supported). The section has the same structure as for `metabolism` apart from the content of `src_get_kwargs`. If you leave it empty the report will give the results for all the segments. Otherwise, you can specify a subset of them adding an `idxs` array of their indexes.

