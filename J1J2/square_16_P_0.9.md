| Energy      | Sigma | Energy Variance | DOF | Einf | Method                                                  | Reference |
|-------------|-------|-----------------|-----|------|---------------------------------------------------------|-----------|
| -44.5994005 |       |                 | 16  | 0    | Exact diagonalization                                   | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_16_P_0.9/ed_netket.sh) |
| -44.5949902 |       | 0.1649          | 16  | 0    | VQE + symm. circuit (64 pars., exact grad, statevector) | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_16_P_0.9/vqe.sh) |
| -44.5896339 |       | 0.3595          | 16  | 0    | VQE + symm. circuit (64 pars., 2^14 samples/grad)       | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_16_P_0.9/vqe_noisy.sh) |
