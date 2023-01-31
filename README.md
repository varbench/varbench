# Classical Variational Benchmarks for Digital Quantum Simulators

Benchmark data are presented in folders that correspond to different Hamiltonian types. For example, the folder `TFIsing` contains data for the transverse-field Ising model.

Data for each specific Hamiltonian are presented in a file, whose filename describes the lattice geometry (see `lattice.md`, except for impurity models) and other parameters such as interaction strength and number of fermions.

The file is a Markdown table, and each row shows a result from a specific numerical method, with the following information:

* `Energy`: the energy expectation $\langle H \rangle$ of the whole system
* `Sigma`: the statistical error on the energy expectation, for methods where this is relevant
* `Energy Variance`: the value of $\langle H^2 \rangle - \langle H \rangle^2$. Even if it reaches the machine precision, please fill in the machine precision and do not leave it blank
* `DOF`: number of degrees of freedom. For spins and spinless fermions it is the number of particles, and for spinful fermions it is `Nup + Ndown`
* `Einf`: zero point of energy, usually defined as the energy expectation at infinite temperature
* `Method`: a short description of the method, with literature reference if applicable
* `Data Repository`: if present, it points to the location of the data necessary to reproduce the result

Note that all rows in a same file always have the same `DOF` and `Einf`, but we replicate them in every row to simplify data analysis.
