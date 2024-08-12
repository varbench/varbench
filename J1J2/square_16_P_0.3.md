| Energy      | Sigma | Energy Variance | DOF | Einf | Method                                                  | Reference |
|-------------|-------|-----------------|-----|------|---------------------------------------------------------|-----------|
| -37.310965  |       |                 | 16  | 0    | Exact diagonalization                                   | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_16_P_0.3/ed_netket.sh) |
| -37.3082879 |       | 0.0873          | 16  | 0    | VQE + symm. circuit (64 pars., exact grad, statevector) | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_16_P_0.3/vqe.sh) |
| -37.308939  |       | 0.0624          | 16  | 0    | VQE + symm. circuit (64 pars., 2^14 samples/grad)       | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_16_P_0.3/vqe_noisy.sh) |
