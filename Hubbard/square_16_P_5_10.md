| Energy                | Sigma   | Energy Variance | DOF | Einf   | Method                                                       | Reference |
|-----------------------|---------|-----------------|-----|--------|--------------------------------------------------------------|-----------|
| -16.90355998424354667 |         |                 | 10  | 15.625 | Exact diagonalization                                        | [code](https://github.com/varbench/methods/blob/main/scripts/Hubbard/square_16_P_5_10/ed_lattice_symmetries.sh) |
| -16.90183             | 0.00002 | 0.047(1)        | 10  | 15.625 | VMC Hidden Fermion Determinant State Ansatz (N_hidden = 10. Single hidden layer fully connected net with alpha = 64). C4 and K = 0 projections | [paper](https://www.pnas.org/doi/full/10.1073/pnas.2122059119)  |
| -16.903559816         |         | 5.71e-6         | 10  | 15.625 | DMRG (MaxBondDim = 7000)                                     | TODO: ask Max |
