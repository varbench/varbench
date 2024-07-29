| Energy              | Sigma  | Energy Variance   | DOF | Einf | Method                       | Reference |
|---------------------|--------|-------------------|-----|------|------------------------------|-----------|
| -102.867902314985   |        |                   | 36  | 0    | Exact diagonalization        | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_36_P_1/ed_lattice_symmetries.sh) |
| -102.67869884652434 |        | 7.164533866758574 | 36  | 0    | DMRG (bond dimension = 2048) | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_36_P_1/dmrg.sh) |
| -102.12601          | 0.0045 | 20.4796           | 36  | 0    | RBM (alpha = 1)              | TODO: own code (RBM) |
| -100.82252          | 0.0050 | 25.3075           | 36  | 0    | Jastrow baseline             | TODO: own code (Jastrow) |
