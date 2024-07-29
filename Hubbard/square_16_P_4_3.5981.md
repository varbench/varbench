| Energy                | Sigma   | Energy Variance | DOF | Einf   | Method                                                       | Reference |
|-----------------------|---------|-----------------|-----|--------|--------------------------------------------------------------|-----------|
| -17.69803001870206671 |         |                 | 8   | 3.5981 | Exact diagonalization                                        | [code](https://github.com/varbench/methods/blob/main/scripts/Hubbard/square_16_P_4_3.5981/ed_lattice_symmetries.sh) |
| -17.69357             | 0.00004 | 0.033(2)        | 8   | 3.5981 | VMC Hidden Fermion Determinant State Ansatz (N_hidden = 8. Single hidden layer fully connected net with alpha = 32) | TODO: ask Javier |
| -17.69623             |         | 2.09e-6         | 8   | 3.5981 | DMRG (MaxBondDim ~3200)                                      | TODO: ask Max |
