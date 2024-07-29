| Energy                | Sigma  | Energy Variance | DOF | Einf    | Method                                                       | Reference |
|-----------------------|--------|-----------------|-----|---------|--------------------------------------------------------------|-----------|
| -16.50915482526514211 |        |                 | 8   | 7.74264 | Exact diagonalization                                        | [code](https://github.com/varbench/methods/blob/main/scripts/Hubbard/square_16_P_4_7.74264/ed_lattice_symmetries.sh) |
| -16.505               | 0.0001 | 0.055(1)        | 8   | 7.74264 | VMC Hidden Fermion Determinant State Ansatz (N_hidden = 8. Single hidden layer fully connected net with alpha = 32) | TODO: ask Javier |
| -16.5091541           |        | 1.331e-7        | 8   | 7.74264 | DMRG (MaxBondDim ~3200)                                      | TODO: ask Max |
