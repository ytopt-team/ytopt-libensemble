This directory includes all files for autotuning ECP app OpenMC with the problem size XXL using ytopt-libensemble on OLCF Crusher only. 

Because OpenMC code is very complex,
its application parameters are command line parameters, we can avoid the compiling and just need to pass these parameters to the OpenMC executable. 
We precompile OpenMC to two executables: openmc and openmc-queueless. The file openmc.sh is the code mold, and the parameter space is defined in run_ytopt.py.
