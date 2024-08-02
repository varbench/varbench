| Energy             | Sigma    | Energy Variance      | DOF | Einf | Method                              | Reference |
|--------------------|----------|----------------------|-----|------|-------------------------------------|-----------|
| -457.041866        | 0.000027 | 0.001429             | 144 | 0    | 2D Recurrent Neural Network (2DRNN) | [paper](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.2.023358) [code](https://github.com/mhibatallah/RNNWavefunctions) |
| -457.0417309784141 |          | 0.009210997202899307 | 144 | 0    | DMRG (bond dimension = 1024)        | [code](https://github.com/varbench/methods/blob/main/scripts/TFIsing/square_144_O_3/dmrg.sh) |
| -457.02705         | 0.00060  | 0.36743321           | 144 | 0    | RBM (alpha = 1)                     | [code](https://github.com/varbench/methods/blob/main/scripts/TFIsing/square_144_O_3/vmc_rbm.sh) |
| -457.01444         | 0.00073  | 0.54852065           | 144 | 0    | Jastrow baseline                    | [code](https://github.com/varbench/methods/blob/main/scripts/TFIsing/square_144_O_3/vmc_jastrow.sh) |
