| Energy             | Sigma | Energy Variance | DOF | Einf | Method                                                       | Data Repository |
|--------------------|-------|-----------------|-----|------|--------------------------------------------------------------|-----------------|
| -50.16239379527527 |       |                 | 24  | 0    | Exact diagonalization                                        |                 |
| -50.0930476        |       | 0.99            | 24  | 0    | VQE + symm. circuit (96 pars., Ns = 2^14 per par, statevector) |                 |
| -50.1019006        |       | 0.95            | 24  | 0    | VQE + symm. circuit (96 pars., exact grads & metric, statevector) |                 |
| -50.16239379503101 |  | 3.916126117129898e-8 | 24  | 0    | DMRG (bond dimension = 4096)                                 |                 |
| -48.6662           | 0.0026 | 7.36838        | 24  | 0    | Jastrow baseline                                             |                 |
| -49.2730           | 0.0031 | 9.76602        | 24  | 0    | RBM (alpha = 1)                                              |                 |
