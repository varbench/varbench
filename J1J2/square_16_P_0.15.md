| Energy      | Sigma | Energy Variance | DOF | Einf | Method                                                  | Reference |
|-------------|-------|-----------------|-----|------|---------------------------------------------------------|-----------|
| -40.9307425 |       |                 | 16  | 0    | Exact diagonalization                                   | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_16_P_0.15/ed_netket.sh) |
| -40.9284231 |       | 0.0964          | 16  | 0    | VQE + symm. circuit (64 pars., exact grad, statevector) | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_16_P_0.15/vqe.sh) |
| -40.9286848 |       | 0.0848          | 16  | 0    | VQE + symm. circuit (64 pars., 2^14 samples/grad)       | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_16_P_0.15/vqe_noisy.sh) |
