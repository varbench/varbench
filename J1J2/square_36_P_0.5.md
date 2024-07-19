| Energy             | Sigma   | Energy Variance   | DOF | Einf | Method                                                       | Reference |
|--------------------|---------|-------------------|-----|------|--------------------------------------------------------------|-----------|
| -72.548590160286   |         |                   | 36  | 0    | Exact diagonalization                                        | TODO: own code (ED) |
| -72.54722          | 0.00016 | 0.037(1)          | 36  | 0    | RBM+PP with momentum (K=0), spin-parity (even S), and point-group (A1) projections, 16 hidden units | [paper](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.11.031034) |
| -72.54140          | 0.00009 | 0.1905(3)         | 36  | 0    | RBM with momentum (K=0), spin-parity (even S), and point-group (A1) projections, 72 hidden units | [paper](https://iopscience.iop.org/article/10.1088/1361-648X/abe268) |
| -72.167            | 0.003   | 5.42              | 36  | 0    | VMC with projected BCS (Z2 spin liquid)                      | TODO: ask Francesco |
| -72.37403751679382 |         | 2.253085463868047 | 36  | 0    | DMRG (bond dimension = 2048)                                 | [code](https://github.com/https://github.com/varbench/methods/blob/main/scripts/J1J2/square_36_P_0.5/dmrg.sh) |
| -70.1176           | 0.0035  | 12.3053           | 36  | 0    | RBM (alpha = 1)                                              | TODO: own code (RBM) |
| -68.8603           | 0.0052  | 27.4161           | 36  | 0    | Jastrow baseline                                             | TODO: own code (Jastrow) |
