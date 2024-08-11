| Energy             | Sigma     | Energy Variance | DOF | Einf | Method                                | Reference |
|--------------------|-----------|-----------------|-----|------|---------------------------------------|-----------|
| -35.61754611950579 | 0         | 0               | 20  | 0    | Exact diagonalization                 | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/chain_20_P/ed_netket.sh) |
| -35.6174890        | 0.0000072 | 0.0001278       | 20  | 0    | RNN                                   | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/chain_20_P/vmc_rnn.sh) |
| -35.6175098        | 0.0000046 | 0.0000534       | 20  | 0    | RNN + translational symmetry          | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/chain_20_P/vmc_rnn.sh) |
| -35.61452          | 0.00033   | 0.0488          | 20  | 0    | VMC with projected fermions + Jastrow | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/chain_20_P/vmc_gutzwiller.sh) |
| -35.6175461195     |           | 1.2E-10         | 20  | 0    | DMRG (max truncation error ~ 1.0E-13) | [code](https://github.com/varbench/methods/blob/main/programs/dmrg_itensors_heisenberg/chain_20_P.jl) |
| -35.60392          | 0.00041   | 0.1757833       | 20  | 0    | RBM (alpha = 1)                       | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/chain_20_P/vmc_rbm.sh) |
| -35.55179          | 0.00049   | 0.2419342       | 20  | 0    | Jastrow baseline                      | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/chain_20_P/vmc_jastrow.sh) |
