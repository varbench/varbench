| Energy      | Sigma | Energy Variance | DOF | Einf | Method                                                  | Reference |
|-------------|-------|-----------------|-----|------|---------------------------------------------------------|-----------|
| -44.9139328 |       |                 | 16  | 0    | Exact diagonalization                                   | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/square_16_P/vqe.sh) |
| -44.9116731 |       | 0.1064          | 16  | 0    | VQE + symm. circuit (64 pars., exact grad, statevector) | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/square_16_P/vqe.sh) |
| -44.9104126 |       | 0.1599          | 16  | 0    | VQE + symm. circuit (64 pars., 2^14 samples/grad)       | [code](https://github.com/varbench/methods/blob/main/scripts/Heisenberg/square_16_P/vqe_noisy.sh) |
