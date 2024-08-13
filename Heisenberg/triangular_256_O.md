| Energy      | Sigma | Energy Variance | DOF | Einf | Method                       | Reference |
|-------------|-------|-----------------|-----|------|------------------------------|-----------|
| -529.080    | 0.088 | 75.088          | 256 | 0    | 2D Gated RNN                 | [paper](https://arxiv.org/abs/2207.14314) [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/triangular_256_O/vmc_2DgatedtensorizedRNN.sh) |
| -520.160985 |       | 159.85312       | 256 | 0    | DMRG (Bond dimension = 2000) | [code](https://github.com/varbench/methods/blob/main/programs/dmrg_itensor_cpp/dmrg_triangular_heisenberg_16x16.cc) |
| -488.934    | 0.018 | 340.191         | 256 | 0    | RBM (alpha = 1)              | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/triangular_256_O/vmc_rbm.sh) |
| -487.225    | 0.015 | 237.059         | 256 | 0    | Jastrow baseline             | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/triangular_256_O/vmc_jastrow.sh) |
