# Hubbard Model

The model is defined on the edges of an arbitrary graph and reads
$$H = -t \sum_{\langle i, j \rangle, \sigma} \left( c^\dagger_{i, \sigma} c_{j, \sigma} + c^\dagger_{j, \sigma} c_{i, \sigma} \right) + U \sum_i n_{i, \uparrow} n_{i, \downarrow}$$
where $c_{i, \sigma}$ are fermionic annihiliation operators.
It is assumed that the unit of energy is $t = 1$.

## Naming

The names of the data files follow the convention `lattice_Nup_Ndown_U.md` in the canonical ensemble.

* `lattice` is the name of the lattice, also containing its extent, boundary conditions, and further information needed to specify the lattice. See `lattice.md` in the main repository for the convention and examples
* `Nup` is the number of electrons with up spin
* `Ndown` is the number of electrons with down spin
* `U` is the on-site interaction
