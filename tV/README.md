# Spinless $t$-$V$ model

The model is defined on the edges of an arbitrary graph and reads
$$H = -t \sum_{\langle i, j \rangle} \left( c^\dagger_{i} c_{j} + c^\dagger_{j} c_{i} \right) + V \sum_{\langle i, j \rangle} n_{i}n_{j}$$
where $c_{i}$ are fermionic annihiliation operators.
It is assumed that the unit of energy is $t = 1$.

## Naming

The name of the data files follows the convention in the canonical ensemble `lattice_N_V.md`

---

`lattice` is the name of the lattice, also containing its extent/further information needed to specify the specific lattice, including its periodic boundary conditions. See `lattice.md` in the main repository for further information and examples.

`N` is the number of spinless fermions.

`V` is the interaction.
