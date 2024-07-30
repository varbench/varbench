| Energy             | Sigma  | Energy Variance    | DOF | Einf | Method                       | Reference |
|--------------------|--------|--------------------|-----|------|------------------------------|-----------|
| -84.454070394730   |        |                    | 36  | 0    | Exact diagonalization        | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_36_P_0.8/ed_lattice_symmetries.sh) |
| -84.35283374817100 |        | 0.9038783749210779 | 36  | 0    | DMRG (bond dimension = 2048) | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_36_P_0.8/dmrg.sh) |
| -84.1270           | 0.0026 | 7.07829            | 36  | 0    | RBM (alpha = 1)              | TODO: own code (RBM) |
| -83.0161           | 0.0042 | 18.2412            | 36  | 0    | Jastrow baseline             | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_36_P_0.8/vmc_jastrow.sh) |
