| Energy      | Sigma | Energy Variance | DOF | Einf | Method                                                  | Reference |
|-------------|-------|-----------------|-----|------|---------------------------------------------------------|-----------|
| -46.8799267 |       |                 | 16  | 0    | Exact diagonalization                                   | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_16_P_0.95/ed_netket.sh) |
| -46.878747  |       | 0.0488          | 16  | 0    | VQE + symm. circuit (64 pars., exact grad, statevector) | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_16_P_0.95/vqe.sh) |
| -46.8750185 |       | 0.1943          | 16  | 0    | VQE + symm. circuit (64 pars., 2^14 samples/grad)       | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_16_P_0.95/vqe_noisy.sh) |
