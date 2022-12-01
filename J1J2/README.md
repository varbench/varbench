# J1-J2 Model

The model is defined on the edges of an arbitrary graph and reads
$$H = J_1 \sum_{\langle i, j \rangle} \vec\sigma_i \cdot \vec\sigma_j + J_2 \sum_{\langle\langle i, j \rangle\rangle} \vec\sigma_i \cdot \vec\sigma_j$$
where we take Pauli matrices $\sigma^{x, y, z}_i$ and the sums extend, respectively, to nearest and next-to-nearest neighbors on the given lattice.
It is assumed that the unit of energy is $J_1 = 1$.

## Naming

The names of the data files follow the convention `lattice_N_J2.md`

* `lattice` is the name of the lattice, also containing its extent, boundary conditions, and further information needed to specify the lattice. See `lattice.md` in the main repository for the convention and examples
* `N` is the number of spins
* `J2` is the next-nearest neighbor interaction
