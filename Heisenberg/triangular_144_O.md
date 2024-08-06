| Energy             | Sigma  | Energy Variance   | DOF | Einf | Method                       | Reference |
|--------------------|--------|-------------------|-----|------|------------------------------|-----------|
| -294.896           | 0.060  | 37.824            | 144 | 0    | 2D Gated RNN                 | [paper](https://arxiv.org/abs/2207.14314) [code](https://github.com/mhibatallah/RNNWavefunctions) |
| -296.677327164     |        | 37.53968          | 144 | 0    | DMRG (Bond dimension = 3000) | ITensor |
| -294.6224149903317 |        | 56.34376540512312 | 144 | 0    | DMRG (bond dimension = 1024) | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/triangular_144_O/dmrg.sh) |
| -278.5075          | 0.0094 | 89.67089          | 144 | 0    | RBM (alpha = 1)              | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/triangular_144_O/vmc_rbm.sh) |
| -274.157           | 0.011  | 127.347           | 144 | 0    | Jastrow baseline             | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/triangular_144_O/vmc_jastrow.sh) |
