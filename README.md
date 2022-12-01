# Classical Variational Benchmarks for Digital Quantum Simulators

Benchmark data are presented in folders that correspond to different Hamiltonian types.
For example, the folder `TfIsing` contains data for the transverse-field Ising model.

The files in each folder contain benchmark results on several lattices, and contain the following information:

* `Energy`: the total energy of the system
* `Sigma`: the statistical error on the mean of the energy, for methods where this is relevant
* `Energy Variance`: the value of $\langle H^2 \rangle - \langle H \rangle^2$. Even if it reaches the machine precision, please fill in the machine precision and do not leave it blank
* `DOF`: number of degrees of freedom. For spins and spinless fermions it is the number of spins, and for spinful fermions it is `Nup + Ndown`
* `Method`: a short description of the method, with literature reference if applicable
* `Data Repository`: if present, it points to the location of the data necessary to reproduce the result

Each file therefore contains aggregated results for a physical system coming from different methods.
