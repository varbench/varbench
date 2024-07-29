| Energy               | Sigma   | Energy Variance        | DOF | Einf | Method                       | Reference |
|----------------------|---------|------------------------|-----|------|------------------------------|-----------|
| -115.232707303718485 |         |                        | 36  | 0    | Exact diagonalization        | [code](https://github.com/varbench/methods/blob/main/scripts/TFIsing/square_36_P_3/ed_lattice_symmetries.sh) |
| -115.23270149009103  |         | 0.00029784587604808627 | 36  | 0    | DMRG (bond dimension = 1024) | [code](https://github.com/varbench/methods/blob/main/scripts/TFIsing/square_36_P_3/dmrg.sh) |
| -115.23165           | 0.00028 | 0.082848699            | 36  | 0    | RBM (alpha = 1)              | TODO: own code (RBM) |
| -115.19484           | 0.00062 | 0.39779351             | 36  | 0    | Jastrow baseline             | TODO: own code (Jastrow) |
