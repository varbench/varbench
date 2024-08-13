| Energy             | Sigma | Energy Variance    | DOF | Einf | Method                       | Reference |
|--------------------|-------|--------------------|-----|------|------------------------------|-----------|
| -402.804           | 0.076 | 58.816             | 196 | 0    | 2D Gated RNN                 | [paper](https://arxiv.org/abs/2207.14314) [code](https://github.com/mhibatallah/RNNWavefunctions) |
| -400.485387        |       | 93.7656            | 196 | 0    | DMRG (Bond dimension = 2000) | [code](https://github.com/varbench/methods/blob/main/programs/dmrg_itensor_cpp/dmrg_triangular_heisenberg_14x14.cc) |
| -400.1928613876728 |       | 113.97946098516695 | 196 | 0    | DMRG (bond dimension = 1024) | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/triangular_196_O/dmrg.sh) |
| -374.707           | 0.015 | 228.613            | 196 | 0    | RBM (alpha = 1)              | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/triangular_196_O/vmc_rbm.sh) |
| -373.499           | 0.013 | 177.484            | 196 | 0    | Jastrow baseline             | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/triangular_196_O/vmc_jastrow.sh) |
