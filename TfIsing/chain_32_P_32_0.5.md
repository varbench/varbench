| Energy             | Sigma   | Energy Variance | DOF | Einf | Method                                           | Data Repository                |
|--------------------|---------|-----------------|-----|------|--------------------------------------------------|--------------------------------|
| -34.03342111916819 | 0       | 0               | 32  | 0    | Exact Solution                                   | data/exact1d                   |
| -34.03338          | 1.9e-05 | 3.5e-04         | 32  | 0    | Symmetric FFN, Relu, 32 features per translation | data/NQS/chain32P_32_0.5.mpack |
| -34.033633         | 5.6e-5  | 0.0032365571    | 32  | 0    | RBM (alpha = 1)                                  |                                |
| -34.03342111914689 |         | 1.6e-10         | 32  | 0    | DMRG (bond dimension = 24)                       |                                |
| -34.01752          | 3.3e-4  | 0.1166148       | 32  | 0    | Jastrow baseline                                 |                                |
