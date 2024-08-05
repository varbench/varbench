| Energy              | Sigma  | Energy Variance       | DOF | Einf | Method                     | Reference |
|---------------------|--------|-----------------------|-----|------|----------------------------|-----------|
| -12.381489999654734 |        |                       | 10  | 0    | Exact Diagonalization      | [code](https://github.com/varbench/methods/blob/main/scripts/TFIsing/chain_10_O_1/ed_netket.sh) |
| -12.381489999654796 |        | 4.8e-13               | 10  | 0    | DMRG (bond dimension = 13) | [code](https://github.com/varbench/methods/blob/main/scripts/TFIsing/chain_10_O_1/dmrg.sh) |
| -12.381718          | 2.2e-5 | 0.00049440652         | 10  | 0    | RBM (alpha = 1)            | [code](https://github.com/varbench/methods/blob/main/scripts/TFIsing/chain_10_O_1/vmc_rbm.sh) |
| -12.37844           | 1.9e-4 | 0.03606162            | 10  | 0    | Jastrow baseline           | [code](https://github.com/varbench/methods/blob/main/scripts/TFIsing/chain_10_O_1/vmc_jastrow.sh) |
| -12.38133801299217  |        | 0.0007985776929899657 | 10  | 0    | VQE HV (d = 24)            | [code](https://github.com/varbench/methods/blob/main/programs/pqc_ising_1d/pqc_HamVar.py) |
| -12.380038028233812 |        | 0.007944439359960143  | 10  | 0    | VQE R-CX (d = 10)          | [code](https://github.com/varbench/methods/blob/main/programs/pqc_ising_1d/pqc_RYCNOT.py) |
