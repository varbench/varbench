| Energy       | Sigma   | Energy Variance | DOF | Einf | Method                                                       | Reference |
|--------------|---------|-----------------|-----|------|--------------------------------------------------------------|-----------|
| -251.46248   |         |                 | 100 | 0    | QMC                                                          | [paper](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.90.064425) |
| -251.4430    | 0.0010  | 0.1102          | 100 | 0    | RNN                                                          | TODO: own code (RNN) |
| -251.4595    | 0.0007  | 0.0195          | 100 | 0    | RNN + translational symmetry                                 | TODO: own code (RNN) |
| -251.4534    |         | 0.3203          | 100 | 0    | DMRG (MaxTruncError ~1.87E-6, MaxBondDim=10000, Extrapolated Energy = - 251.4628 +/- 0.0019) | TODO: ask Max |
| -251.45538   | 0.00044 | 0.19397         | 100 | 0    | 2D Gated RNN                                                 | [paper](https://arxiv.org/abs/2207.14314) [code](https://github.com/mhibatallah/RNNWavefunctions) |
| -251.4404(8) | ?       | ?               | 100 | 0    | PEPS (bond dimension = 10)                                   | [paper](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.95.195154) |
| -250.3460    | 0.0041  | 16.83691        | 100 | 0    | 1D MPS-RNN (bond dimension = 40)                             | [paper](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.5.L032001) [code](https://github.com/cqsl/mps-rnn) |
| -251.0788    | 0.0022  | 4.928276        | 100 | 0    | 2D MPS-RNN (bond dimension = 40)                             | [paper](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.5.L032001) [code](https://github.com/cqsl/mps-rnn) |
| -251.4112    | 0.0015  | 2.289447        | 100 | 0    | Tensor-RNN (bond dimension = 40)                             | [paper](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.5.L032001) [code](https://github.com/cqsl/mps-rnn) |
| -249.1033    | 0.0051  | 26.13060        | 100 | 0    | RBM (alpha = 1)                                              | TODO: own code (RBM) |
| -248.1073    | 0.0056  | 31.73600        | 100 | 0    | Jastrow baseline                                             | TODO: own code (Jastrow) |
