| Energy             | Sigma  | Energy Variance     | DOF | Einf | Method                       | Reference |
|--------------------|--------|---------------------|-----|------|------------------------------|-----------|
| -76.320176597454   |        |                     | 36  | 0    | Exact diagonalization        | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_36_P_0.7/ed_lattice_symmetries.sh) |
| -76.30909588668733 |        | 0.19627705600487386 | 36  | 0    | DMRG (bond dimension = 2048) | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_36_P_0.7/dmrg.sh) |
| -75.9732           | 0.0028 | 7.80946             | 36  | 0    | RBM (alpha = 1)              | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_36_P_0.7/vmc_rbm.sh) |
| -69.5699           | 0.0083 | 70.6665             | 36  | 0    | Jastrow baseline             | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_36_P_0.7/vmc_jastrow.sh) |
