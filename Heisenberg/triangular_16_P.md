| Energy              | Sigma  | Energy Variance | DOF | Einf | Method                      | Reference |
|---------------------|--------|-----------------|-----|------|-----------------------------|-----------|
| -34.22205967006502  | 0      | 0               | 16  | 0    | Exact diagonalization       | TODO: own code (ED) |
| -34.1780764         | 0      | 0.424225        | 16  | 0    | VQE (SR + symm. + 64 par)   | TODO: ask Nikita |
| -34.222059670065036 |        | 1e-15           | 16  | 0    | DMRG (bond dimension = 256) | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/triangular_16_P/dmrg.sh) |
| -33.5469            | 0.0034 | 12.0932         | 16  | 0    | RBM (alpha = 1)             | TODO: own code (RBM) |
| -33.0945            | 0.0027 | 7.37471         | 16  | 0    | Jastrow baseline            | TODO: own code (Jastrow) |
