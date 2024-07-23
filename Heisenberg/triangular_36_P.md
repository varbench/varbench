| Energy             | Sigma  | Energy Variance   | DOF | Einf | Method                       | Reference |
|--------------------|--------|-------------------|-----|------|------------------------------|-----------|
| -80.6937689612426  |        |                   | 36  | 0    | Exact diagonalization        | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/triangular_36_P/ed_lattice_symmetries.sh) |
| -80.36672248793934 |        | 7.068731007373572 | 36  | 0    | DMRG (bond dimension = 2048) | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/triangular_36_P/dmrg.sh) |
| -70.7915           | 0.0065 | 43.4753           | 36  | 0    | RBM (alpha = 1)              | TODO: own code (RBM) |
| -70.0967           | 0.0060 | 37.0349           | 36  | 0    | Jastrow baseline             | TODO: own code (Jastrow) |
