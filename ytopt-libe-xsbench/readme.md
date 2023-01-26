This directory includes all files for autotuning ECP proxy app XSBench using ytopt-libensemble on a laptop, ALCF Theta and OLCF Crusher.

# Directory
```
laptop/	
    Autotuning XSBench on a laptop for demonstration
theta/
    Autotuning XSBench on ALCF Theta
crusher/	
    Autotuning XSBench on OLCF Crusher 

```

# Instructions for testing the autotuning framework on a laptop 
Follow the ytopt-libensemble installation instructions to install ytopt and libensemble on a laptop such as a Macbook Pro. Aussume that MPI and OpenMP programming environments are installed and supported already (use "brew install open-mpi" to install MPI; use "brew install libomp" to install OpenMP). 

Do the following steps:
```
cd laptop
* If you want to change the compiler mpicc (default), edit the file plopper.py. 
* make sure to create the conda environemnt ytune before running a test
* use the run script runs.sh to autotune XSBench
./runs.sh
```
After it is finished, one performance file results.csv is generated. The file looks like 
```
p0,p1,p2,p3,p4,RUNTIME,elapsed_sec
8,20,#pragma omp parallel for,sockets,master,20.224,24.39652395248413
4,20, ,threads,master,20.194,45.44950008392334
8,64, ,sockets,master,20.17,45.55336308479309
8,40, ,threads,master,20.13,66.76408386230469
2,40,#pragma omp parallel for,sockets,spread,20.155,67.15401411056519
8,10,#pragma omp parallel for,threads,spread,20.212,88.18876695632935
2,80, ,threads,master,20.296,88.57480216026306
8,128, ,threads,master,20.452,109.7756142616272
8,80, ,sockets,master,20.222,110.09131217002869
```
where p0,p1,p2,p3,p4 are the tunable parameters; objective stands for the application execution time (in seconds); and elapsed_sec stands for the wall-clock time.
