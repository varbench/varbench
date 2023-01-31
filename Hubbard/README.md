# Hubbard Model

The model is defined on the edges of an arbitrary graph and reads
$$H = -t \sum_{\langle i, j \rangle, \sigma} \left( c^\dagger_{i, \sigma} c_{j, \sigma} + c^\dagger_{j, \sigma} c_{i, \sigma} \right) + U \sum_i n_{i, \uparrow} n_{i, \downarrow}$$
where $c_{i, \sigma}$ are fermionic annihiliation operators.
It is assumed that the unit of energy is $t = 1$.

## Naming

The names of the data files follow the convention `lattice_Nup_U.md` in the canonical ensemble.

* `lattice` is the lattice geometry (see `lattice.md`)
* `Nup` is the number of electrons with spin up, and we assume `Nup = Ndown`
* `U` is the on-site interaction
