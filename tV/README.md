# Spinless t-V model

The model is defined on the edges of an arbitrary graph and reads
$$H = -t \sum_{\langle i, j \rangle} \left( c^\dagger_i c_j + c^\dagger_j c_i \right) + V \sum_{\langle i, j \rangle} n_i n_j$$
where $c_i$ are fermionic annihiliation operators.
It is assumed that the unit of energy is $t = 1$.

## Naming

The names of the data files follow the convention `lattice_Nf_V.md` in the canonical ensemble.

* `lattice` is the name of the lattice, also containing its extent, boundary conditions, and further information needed to specify the lattice. See `lattice.md` in the main repository for the convention and examples
* `Nf` is the number of spinless fermions
* `V` is the repulsive interaction
