| Energy             | Sigma  | Energy Variance   | DOF | Einf | Method                       | Reference |
|--------------------|--------|-------------------|-----|------|------------------------------|-----------|
| -97.7575895972357  |        |                   | 36  | 0    | Exact diagonalization        | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/square_36_P/ed_lattice_symmetries.sh) |
| -97.72162414290578 |        | 1.385137434483113 | 36  | 0    | DMRG (bond dimension = 2048) | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/square_36_P/dmrg.sh) |
| -96.2702           | 0.0037 | 13.9167           | 36  | 0    | RBM (alpha = 1)              | TODO: own code (RBM) |
| -96.4427           | 0.0038 | 14.7488           | 36  | 0    | Jastrow baseline             | TODO: own code (Jastrow) |
