# Heisenberg Model

The model is defined on the edges of an arbitrary graph and reads
$$H = J \sum_{\langle i, j \rangle} \vec\sigma_i \cdot \vec\sigma_j$$
where we take Pauli matrices $\sigma^{x, y, z}_i$.
It is assumed that the unit of energy is $J = 1$.

## Naming

The names of the data files follow the convention `lattice_N.md`

* `lattice` is the name of the lattice, also containing its extent, boundary conditions, and further information needed to specify the lattice. See `lattice.md` in the main repository for the convention and examples
* `N` is the number of spins
