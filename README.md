# Classical Variational Benchmarks for Digital Quantum Simulators

Benchmark data is presented in folders that correspond to different models.
For example, the folder `TfIsing` contains data for the Transverse-Field Ising model.

The files in each folders contain benchmark results on several lattices, and contain the following information.

`Energy`: the total Energy of the system

`Sigma`: the statistical error on the mean of the energy (for methods where this is relevant)

`Energy Variance`: the value of $\langle H^2 \rangle - \langle H \rangle^2$ for the given method

`DOF`: number of degrees of freedom. For spin models it's the number of spins, and for Hubbard model it's `Nup + Ndown`

`Method`: name of the method used with a short description of the parameters (if relevant)

`Data Repository`: if present, it points to the location of the data necessary to reproduce the result

Each file therefore contains aggregated results coming from different methods.
