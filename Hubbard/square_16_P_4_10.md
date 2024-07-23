| Energy                | Sigma  | Energy Variance | DOF | Einf | Method                                                       | Reference |
|-----------------------|--------|-----------------|-----|------|--------------------------------------------------------------|-----------|
| -16.14320817020241350 |        |                 | 8   | 10   | Exact diagonalization                                        | [code](https://github.com/varbench/methods/blob/main/scripts/Hubbard/square_16_P_4_10/ed_lattice_symmetries.sh) |
| -16.1383              | 0.0001 | 0.078(3)        | 8   | 10   | VMC Hidden Fermion Determinant State Ansatz (N_hidden = 8. Single hidden layer fully connected net with alpha = 32) | TODO: ask Javier |
| -16.14320807          |        | 1.81e-7         | 8   | 10   | DMRG (MaxBondDim = 3200)                                     | TODO: ask Max |
