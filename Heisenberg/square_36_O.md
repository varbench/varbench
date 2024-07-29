| Energy             | Sigma  | Energy Variance        | DOF | Einf | Method                       | Reference |
|--------------------|--------|------------------------|-----|------|------------------------------|-----------|
| -86.9071441699763  |        |                        | 36  | 0    | Exact diagonalization        | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/square_36_O/ed_lattice_symmetries.sh) |
| -86.90713263791655 |        | 0.00045932030843687244 | 36  | 0    | DMRG (bond dimension = 2048) | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/square_36_O/dmrg.sh) |
| -85.4857           | 0.0035 | 12.2737                | 36  | 0    | RBM (alpha = 1)              | TODO: own code (RBM) |
| -85.6567           | 0.0036 | 13.4570                | 36  | 0    | Jastrow baseline             | TODO: own code (Jastrow) |
