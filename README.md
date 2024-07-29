# Variational Benchmarks for Quantum Many-Body Problems

[![Paper (v1)](https://img.shields.io/badge/paper%20%28v1%29-arXiv%3A2302.04919-B31B1B)](https://arxiv.org/abs/2302.04919)
[![DOI](https://zenodo.org/badge/388489339.svg)](https://zenodo.org/badge/latestdoi/388489339)

Benchmark data are presented in folders that correspond to different Hamiltonian types. For example, the folder `TFIsing` contains data for the transverse-field Ising model.

Data for each specific Hamiltonian are presented in a file, whose filename describes the lattice geometry (see `lattice.md`, except for impurity models) and other parameters such as interaction strength and number of fermions.

The file is a Markdown table, and each row shows a result from a specific numerical method, with the following information:

* `Energy`: the energy expectation $\langle H \rangle$ of the whole system
* `Sigma`: the statistical error on the energy expectation, for methods where this is relevant
* `Energy Variance`: the value of $\langle H^2 \rangle - \langle H \rangle^2$. Even if it reaches the machine precision, please fill in the machine precision and do not leave it blank
* `DOF`: number of degrees of freedom. For spins and spinless fermions it is the number of particles, and for spinful fermions it is `Nup + Ndown`
* `Einf`: zero point of energy, usually defined as the energy expectation at infinite temperature
* `Method`: a short description of the method
* `Reference`: the literature reference and the code repository to reproduce the result. Note that some links point to the latest version of [methods](https://github.com/varbench/methods) repository on GitHub. To fully reproduce the results in the paper, please use the archived version of methods repository on Zenodo instead

Note that all rows in a same file always have the same `DOF` and `Einf`, but we replicate them in every row to simplify data analysis.

## Plotting

The plots in the paper are presented in the folder `scripts/`. To reproduce them, run the following (on Linux with Python 3 installed):
```sh
cd scripts/
pip install -r requirements.txt
./plot_all.sh
```
