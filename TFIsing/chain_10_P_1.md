| Energy              | Sigma  | Energy Variance | DOF | Einf | Method                     | Reference |
|---------------------|--------|-----------------|-----|------|----------------------------|-----------|
| -12.784906442999322 |        |                 | 10  | 0    | Exact Solution             | [code](https://github.com/https://github.com/varbench/methods/blob/main/programs/exact_ising_1d/exact_ising_1d.py) |
| -12.784906442999326 |        | 1.1e-13         | 10  | 0    | DMRG (bond dimension = 28) | [code](https://github.com/https://github.com/varbench/methods/blob/main/scripts/TFIsing/chain_10_P_1/dmrg.sh) |
| -12.785231          | 4.8e-5 | 0.0024565159    | 10  | 0    | RBM (alpha = 1)            | TODO: own code (RBM) |
| -12.77246           | 3.0e-4 | 0.09330111      | 10  | 0    | Jastrow baseline           | TODO: own code (Jastrow) |
