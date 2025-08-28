# CMarkov_CellCycle_Checkopints
The repository contains codes to run Markov chain-like model that simulates cell cycle state transitions under DNA damage

README

Overview

This document provides instructions for using three scripts: MakeParameterSets_Parameterscan.py, Markov_CellCycle_Check.py, and Parallel_Markov.sh. These scripts are used sequentially to generate and process parameter sets for Markov model simulations.

File Descriptions

1. MakeParameterSets_Parameterscan.py:
   - Functionality: Generates a directory of parameter files used for Markov model simulations.
   - Usage: Modify parameter values as needed, then run the script to output parameter files.

2. Markov_CellCycle_Check.py:
   - Functionality: Simulates cell cycle dynamics based on parameters from the generated files.
   - Usage: Processes each parameter file to simulate the respective conditions.
   - Note: Contains additional parameters that can be adjusted to refine simulation conditions.

3. Parallel_Markov.sh:
   - Functionality: Runs Markov_CellCycle_Check.py concurrently across all parameter files using limited parallelism.
   - Usage: Facilitates efficient simulation by managing simultaneous execution using semaphores.

Dependencies

Ensure the following dependencies are installed on your system:
- Python 3.x
- NumPy (Install using `pip install numpy`)
- math (standard library; no installation required)
- random (standard library; no installation required)
- itertools (standard library; no installation required)
- decimal (standard library; no installation required)
- multiprocessing (standard library; no installation required)
- sys (standard library; no installation required)
- pyprobs (Install using `pip install pyprobs`, if applicable)

These libraries and modules are necessary for the proper execution of the provided Python scripts.

Execution Steps

Step 1: Generate Parameter Files

1. Open MakeParameterSets_Parameterscan.py and specify your desired parameter values within the script.
2. Execute the script in terminal:
   python MakeParameterSets_Parameterscan.py
   This will create a directory named Parameterscan_default containing files with parameter sets.

Step 2: Run Simulations

1. Ensure Markov_CellCycle_Check.py and Parallel_Markov.sh are in the same directory as the Parameterscan_default directory.
2. Modify any necessary parameters directly within Markov_CellCycle_Check.py to suit your analysis needs.
3. Run the shell script to start the simulation:
   sh Parallel_Markov.sh

Step 3: Analyze Results

- The outputs of the simulations will be written to result files in the same directory, typically named using the pattern MarkovModel_simulation_results_<parameterset>.txt.

Summary of Code Operations

- MakeParameterSets_Parameterscan.py creates numerous combinations of parameters for a Markov model, writes them to text files, and organizes these files to be used in simulations.
- Markov_CellCycle_Check.py processes these parameter files to simulate cell cycle transitions under specified conditions, considering DNA damage and repair.
- Parallel_Markov.sh manages the execution of simulations in parallel while limiting system resource use, enhancing efficiency by running multiple simulations concurrently.

Output Files

The output files, typically named MarkovModel_simulation_results_<parameterset>.txt, contain detailed results of the simulations based on each set of parameters:

1. Header Information:
   - Includes labels for each column, such as:
     - parset: Identifier for the parameter set.
     - replicate: The replicate number.
     - cellID: Identifier for each simulated cell.
     - time: The time point at which the state of the cell is recorded.
     - DSB: The level of DNA damage at the designated time point.
     - phase: The current phase of the cell cycle.
     - DNAcontent: The DNA content in the cell.
     - ploidy: The ploidy level of the cell.
     - MN: Mitotic error indicator.
     - Parameters used in the simulation.

2. Simulation Data:
   - Each line corresponds to a recorded state of a cell at a given time, detailing the evolution of the parameters during the simulation.

