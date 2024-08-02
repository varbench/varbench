| Energy             | Sigma | Energy Variance | DOF | Einf | Method                                  | Reference |
|--------------------|-------|-----------------|-----|------|-----------------------------------------|-----------|
| -32.19308309416487 |       |                 | 18  | 0    | Exact Diagonalization                   | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/kagome-2x3_18_P/ed_netket.sh) |
| -32.1645862        |       | 1.20            | 18  | 0    | VQE (SR + symm. + 108 variational pars) | TODO: ask Nikita |
| -32.19308309416483 |       | 1e-14           | 18  | 0    | DMRG (bond dimension = 368)             | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/kagome-2x3_18_P/dmrg.sh) |
| -29.1114           | 0.0032 | 10.5339        | 18  | 0    | Jastrow baseline                        | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/kagome-2x3_18_P/vmc_rbm.sh) |
| -31.5125           | 0.0024 | 6.16589        | 18  | 0    | RBM (alpha = 1)                         | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/kagome-2x3_18_P/vmc_jastrow.sh) |
