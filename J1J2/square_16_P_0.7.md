| Energy      | Sigma | Energy Variance | DOF | Einf | Method                                                  | Reference |
|-------------|-------|-----------------|-----|------|---------------------------------------------------------|-----------|
| -36.0869194 |       |                 | 16  | 0    | Exact diagonalization                                   | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_16_P_0.7/ed_netket.sh) |
| -36.0809175 |       | 0.1979          | 16  | 0    | VQE + symm. circuit (64 pars., exact grad, statevector) | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_16_P_0.7/vqe.sh) |
| -36.0813809 |       | 0.1482          | 16  | 0    | VQE + symm. circuit (64 pars., 2^14 samples/grad)       | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_16_P_0.7/vqe_noisy.sh) |
