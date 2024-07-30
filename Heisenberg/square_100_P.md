| Energy             | Sigma  | Energy Variance | DOF | Einf | Method                                | Reference |
|--------------------|--------|-----------------|-----|------|---------------------------------------|-----------|
| -267.741           | 0.004  | 12.2            | 100 | 0    | VMC with fermions (flux+neel+Jastrow) | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/square_100_P/vmc_gutzwiller.sh) |
| -268.4538          | 0.0005 | 0.5409          | 100 | 0    | RNN                                   | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/square_100_P/vmc_rnn.sh) |
| -268.560           | 0.005  | 0.092           | 100 | 0    | RNN + translational symmetry          | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/square_100_P/vmc_rnn.sh) |
| -265.9424657801722 |        | 42.496814964441 | 100 | 0    | DMRG (bond dimension = 1024)          | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/square_100_P/dmrg.sh) |
| -265.7726          | 0.0060 | 37.11238        | 100 | 0    | RBM (alpha = 1)                       | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/square_100_P/vmc_rbm.sh) |
| -265.6846          | 0.0056 | 31.98062        | 100 | 0    | Jastrow baseline                      | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/square_100_P/vmc_jastrow.sh) |
