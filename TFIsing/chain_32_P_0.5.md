| Energy             | Sigma   | Energy Variance | DOF | Einf | Method                                           | Reference |
|--------------------|---------|-----------------|-----|------|--------------------------------------------------|-----------|
| -34.03342111916819 | 0       | 0               | 32  | 0    | Exact Solution                                   | TODO: own code (exact solution) |
| -34.03338          | 1.9e-05 | 3.5e-04         | 32  | 0    | Symmetric FFN, Relu, 32 features per translation | TODO: own code (symmetric FFN) |
| -34.033633         | 5.6e-5  | 0.0032365571    | 32  | 0    | RBM (alpha = 1)                                  | TODO: own code (baseline RBM) |
| -34.03342111914689 |         | 1.6e-10         | 32  | 0    | DMRG (bond dimension = 24)                       | TODO: own code (DMRG) |
| -34.01752          | 3.3e-4  | 0.1166148       | 32  | 0    | Jastrow baseline                                 | TODO: own code (baseline Jastrow) |
