# Hubbard Model

The model is defined on the edges of an arbitrary graph and reads
$ H = -t \sum_{<i,j>,{\sigma}} \left ( c^{\dagger}_{i,\sigma} c^_{j,\sigma} + c^{\dagger}_{j,\sigma} c^_{i,\sigma} \right )  + U \sum_{i} n_{i,\uparrow} n_{i,\downarrow}  $,
where $c_{i,\sigma}$ are fermionic annihiliation operators.
It is assumed that the units of energy are $ t=1 $.

## Naming

The name of the data files follows the convention in the canonical ensemble `lattice_Nup_Ndown_U.md`

---

`lattice` is the name of the lattice, also containing its extent/further information needed to specify the specific lattice, including its periodic boundary conditions. See `lattice.md` in the main repository for further information and examples.

`Nup` is the total number of electrons with up spin

`Ndown` is the total number of electrons with down spin

`U` is the on-site interaction
