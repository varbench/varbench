| Energy              | Sigma   | Energy Variance    | DOF | Einf | Method                                                       | Reference |
|---------------------|---------|--------------------|-----|------|--------------------------------------------------------------|-----------|
| -198.060            | 0.009   | 11.6               | 100 | 0    | VMC with projected BCS (Z2 spin liquid)                      | TODO: ask Francesco |
| -199.05174          | 0.00044 | 0.79(3)            | 100 | 0    | RBM+PP with momentum (K=0), spin-parity (even S), and point-group (A1) projections, 16 hidden units | [paper](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.11.031034) |
| -198.1570           | 0.0030  | 1.6237             | 100 | 0    | RNN                                                          | TODO: own code (RNN) |
| -198.239            | 0.017   | 4.671              | 100 | 0    | RNN + translational symmetry                                 | TODO: own code (RNN) |
| -196.55931995563643 |         | 16.657353288515882 | 100 | 0    | DMRG (bond dimension = 1024)                                 | [code](https://github.com/https://github.com/varbench/methods/blob/main/scripts/J1J2/square_100_P_0.5/dmrg.sh) |
| -190.8007           | 0.0084  | 71.58155           | 100 | 0    | RBM (alpha = 1)                                              | TODO: own code (RBM) |
| -189.5607           | 0.0084  | 71.68267           | 100 | 0    | Jastrow baseline                                             | TODO: own code (Jastrow) |
