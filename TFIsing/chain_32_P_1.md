| Energy             | Sigma   | Energy Variance | DOF | Einf | Method                                           | Data Repository              |
|--------------------|---------|-----------------|-----|------|--------------------------------------------------|------------------------------|
| -40.76003249419223 | 0       | 0               | 32  | 0    | Exact Solution                                   | data/exact1d                 |
| -40.760008         | 5.8e-06 | 2.0e-04         | 32  | 0    | Symmetric FFN, Relu, 32 features per translation | data/NQS/chain32P_32_1.mpack |
| -40.75763          | 1.4e-4  | 0.01991942      | 32  | 0    | RBM (alpha = 1)                                  |                              |
| -40.76003249394725 |         | 2.8e-9          | 32  | 0    | DMRG (bond dimension = 71)                       |                              |
| -40.70126          | 5.3e-4  | 0.2877156       | 32  | 0    | Jastrow baseline                                 |                              |
