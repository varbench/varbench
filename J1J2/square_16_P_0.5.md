| Energy             | Sigma   | Energy Variance | DOF | Einf | Method                                                  | Reference |
|--------------------|---------|-----------------|-----|------|---------------------------------------------------------|-----------|
| -33.83169340557936 |         |                 | 16  | 0    | Exact diagonalization                                   | TODO: own code (ED) |
| -33.8315064        |         | 7e-3            | 16  | 0    | VQE + symm. circuit (64 pars., exact grad, statevector) | TODO: ask Nikita |
| -33.83169340557946 |         | 1e-15           | 16  | 0    | DMRG (bond dimension = 256)                             | TODO: own code (DMRG) |
| -33.0219           | 0.0036  | 12.9877         | 16  | 0    | RBM (alpha = 1)                                         | TODO: own code (RBM) |
| -32.5106           | 0.0015  | 2.20818         | 16  | 0    | Jastrow baseline                                        | TODO: own code (Jastrow) |
| -33.831039193      | 0.00031 | 0.01741932679   | 16  | 0    | ClebschTree                                             | [paper](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.104.045123) |
