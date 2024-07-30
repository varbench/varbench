| Energy              | Sigma  | Energy Variance    | DOF | Einf | Method                           | Reference |
|---------------------|--------|--------------------|-----|------|----------------------------------|-----------|
| -200.276            | 0.004  | 5.032              | 100 | 0    | RNN                              | TODO: own code (RNN) |
| -205.90673107198964 |        | 11.224306962726814 | 100 | 0    | DMRG (bond dimension = 4096)     | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/triangular_100_O/dmrg.sh) |
| -195.8572           | 0.0089 | 80.60808           | 100 | 0    | 1D MPS-RNN (bond dimension = 40) | [paper](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.5.L032001) [code](https://github.com/cqsl/mps-rnn) |
| -203.2108           | 0.0050 | 25.73127           | 100 | 0    | 2D MPS-RNN (bond dimension = 40) | [paper](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.5.L032001) [code](https://github.com/cqsl/mps-rnn) |
| -205.5452           | 0.0035 | 12.31392           | 100 | 0    | Tensor-RNN (bond dimension = 40) | [paper](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.5.L032001) [code](https://github.com/cqsl/mps-rnn) |
| -193.8193           | 0.0082 | 69.24535           | 100 | 0    | RBM (alpha = 1)                  | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/triangular_100_O/vmc_rbm.sh) |
| -190.6983           | 0.0093 | 87.62059           | 100 | 0    | Jastrow baseline                 | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/triangular_100_O/vmc_jastrow.sh) |
