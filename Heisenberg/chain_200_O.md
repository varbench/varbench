| Energy         | Sigma  | Energy Variance | DOF | Einf | Method                                | Reference |
|----------------|--------|-----------------|-----|------|---------------------------------------|-----------|
| -353.766222278 |        | 5.4E-9          | 200 | 0    | DMRG (max truncation error ~ 1.0E-14) | [code](https://github.com/varbench/methods/blob/main/programs/dmrg_itensors_heisenberg/chain_200_O.jl) |
| -350.2717      | 0.0040 | 16.35715        | 200 | 0    | RBM (alpha = 1)                       | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/chain_200_O/vmc_rbm.sh) |
| -345.9215      | 0.0044 | 19.99755        | 200 | 0    | Jastrow baseline                      | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/chain_200_O/vmc_jastrow.sh) |
