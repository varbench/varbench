| Energy             | Sigma   | Energy Variance | DOF | Einf | Method                                           | Reference |
|--------------------|---------|-----------------|-----|------|--------------------------------------------------|-----------|
| -40.76003249419223 | 0       | 0               | 32  | 0    | Exact Solution                                   | [code](https://github.com/varbench/methods/blob/main/programs/exact_ising_1d/exact_ising_1d.py) |
| -40.760008         | 5.8e-06 | 2.0e-04         | 32  | 0    | Symmetric FFN, Relu, 32 features per translation | TODO: own code (symmetric FFN) |
| -40.75763          | 1.4e-4  | 0.01991942      | 32  | 0    | RBM (alpha = 1)                                  | TODO: own code (RBM) |
| -40.76003249394725 |         | 2.8e-9          | 32  | 0    | DMRG (bond dimension = 71)                       | [code](https://github.com/varbench/methods/blob/main/scripts/TFIsing/chain_32_P_1/dmrg.sh) |
| -40.70126          | 5.3e-4  | 0.2877156       | 32  | 0    | Jastrow baseline                                 | TODO: own code (Jastrow) |
