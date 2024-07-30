| Energy             | Sigma    | Energy Variance | DOF | Einf | Method                                | Reference |
|--------------------|----------|-----------------|-----|------|---------------------------------------|-----------|
| -34.72989333759587 | 0        | 0               | 20  | 0    | Exact diagonalization                 | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/chain_20_O/ed_netket.sh) |
| -34.729829         | 0.000014 | 0.000506        | 20  | 0    | RNN                                   | TODO: own code (RNN) |
| -34.7298933375     |          | 6.3E-10         | 20  | 0    | DMRG (max truncation error ~ 1.0E-12) | TODO: ask Max |
| -34.72711          | 0.00021  | 0.04559541      | 20  | 0    | RBM (alpha = 1)                       | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/chain_20_O/vmc_rbm.sh) |
| -34.69100          | 0.00031  | 0.1008130       | 20  | 0    | Jastrow baseline                      | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/chain_20_O/vmc_jastrow.sh) |
