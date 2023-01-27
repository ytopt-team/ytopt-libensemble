# Autotuning Framework ytopt-libensemble
[ytopt](https://github.com/ytopt-team/ytopt.git) is a machine-learning-based search software package that consists of sampling a small number of input parameter configurations, evaluating them, and progressively fitting a surrogate model over the input-output space until exhausting the user-defined time or the maximum number of evaluations. The package is built based on Bayesian Optimization that solves any optimization problem and is especially useful when the objective function is difficult to evaluate. It provides an interface that deals with unconstrained and constrained problems. The software is designed to operate in the manager-worker computational paradigm, where one manager node fits the surrogate model and generates promising input configurations and worker nodes perform the computationally expensive evaluations and return the outputs to the manager node. The asynchronous aspect of the search allows the search to avoid waiting for all the evaluation results before proceeding to the next iteration. As soon as an evaluation is finished, the data is used to retrain the surrogate model, which is then used to bias the search toward the promising configurations.

[libensemble](https://github.com/ytopt-team/libensemble.git) is a Python toolkit for coordinating workflows of asynchronous and dynamic ensembles of calculations in parallel. It helps users take advantage of massively parallel resources to solve design, decision, and inference problems and expands the class of problems that can benefit from increased parallelism. libensemble employs a manager/worker scheme that communicates via MPI, multiprocessing, or TCP. A manager allocate work to multiple workers. Workers control and monitor any level of work from small subnode tasks to huge many-node computations.

By integrating libensemble with ytopt, the autotuning framework ytopt-libensemble not only accelerates the evaluation process of ytopt in parallel but also improves the accuracy fo Random Forests surrage model by feeding more data to make the search more efficient.


# Install instructions
The autotuning framework ytopt-libensemble requires the following components: ConfigSpace,scikit-optimize, autotune, ytopt, and libensemble.

* We recommend creating isolated Python environments (python >=3.7) on your local machine using [conda](https://docs.conda.io/projects/conda/en/latest/index.html), for example:

```
conda create --name ytune python=3.10
conda activate ytune
```

* Create a directory for ytopt tutorial as follows:
```
mkdir ytune
cd ytune
```

* Install [ConfigSpace](https://github.com/ytopt-team/ConfigSpace.git):
```
git clone https://github.com/ytopt-team/ConfigSpace.git
cd ConfigSpace
pip install -e .
cd ..
```

* Install [scikit-optimize](https://github.com/ytopt-team/scikit-optimize.git):
```
git clone https://github.com/ytopt-team/scikit-optimize.git
cd scikit-optimize
pip install -e .
cd ..
```

* Install [autotune](https://github.com/ytopt-team/autotune.git):
```
git clone -b version1 https://github.com/ytopt-team/autotune.git
cd autotune
pip install -e .
cd ..
```

* Install [ytopt](https://github.com/ytopt-team/ytopt.git):
```
git clone https://github.com/ytopt-team/ytopt.git
cd ytopt
pip install -e .
cd ..
```

* Install [libensemble](https://github.com/ytopt-team/libensemble.git):
```
git clone https://github.com/ytopt-team/libensemble.git
cd libensemble
pip install -e .
cd ..
```

After installing ConfigSpace, Scikit-optimize, autotune, ytopt, and libensemble successfully, the autotuning framework ytopt-libensemble is ready to use.
Note: For the diagnosis purpose, look at the log files (*.log) or text files (*.txt) for any error under the current directory.

# Tutorials

* [Autotuning the MPI/OpenMP version of XSBench](https://github.com/ytopt-team/ytopt-libensemble/tree/main/ytopt-libe-xsbench)
* [Autotuning the GPU version of OpenMC](https://github.com/ytopt-team/ytopt-libensemble/tree/main/ytopt-libe-openmc)
