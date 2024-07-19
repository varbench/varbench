| Energy              | Sigma   | Energy Variance | DOF | Einf | Method                               | Reference |
|---------------------|---------|-----------------|-----|------|--------------------------------------|-----------|
| -1272.5724160956197 |         | 6.2083850603085 | 400 | 0    | DMRG (bond dimension = 1024)         | [code](https://github.com/varbench/methods/blob/main/scripts/TFIsing/square_400_O_3/dmrg.sh) |
| -1266.7258          | 0.0098  | 98.838660       | 400 | 0    | RBM (alpha = 1)                      | TODO: own code (RBM) |
| -1272.6319          | 0.0014  | 2.0295256       | 400 | 0    | Jastrow baseline                     | TODO: own code (Jastrow) |
| -1272.788(8)        |         | ?               | 400 | 0    | DMRG on TPU (bond dimension = 32768) | [paper](https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.4.010317) |
| -1269.6048          | 0.0082  | 70.167025       | 400 | 0    | 1D MPS-RNN (bond dimension = 64)     | [paper](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.5.L032001) [code](https://github.com/cqsl/mps-rnn) |
| -1272.7488          | 0.00058 | 0.34593595      | 400 | 0    | 2D MPS-RNN (bond dimension = 64)     | [paper](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.5.L032001) [code](https://github.com/cqsl/mps-rnn) |
| -1272.7616          | 0.00049 | 0.24804703      | 400 | 0    | Tensor-RNN (bond dimension = 64)     | [paper](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.5.L032001) [code](https://github.com/cqsl/mps-rnn) |
