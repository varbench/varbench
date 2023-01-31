# Lattice naming convention

Hamiltonians defined on lattices follow a brief naming convention to describe the lattice geometry: `type_size_boundary`.

* `type` is one in `chain`, `square`, `rectangular`, `triangular`, `kagome`, `shuriken` (a.k.a. square kagome), `pyrochlore`
    * The square lattice can be tilted and contain, e.g., 24 or 50 sites
    * For `rectangular`, `kagome`, and `pyrochlore`, we additionally write out the extents of unit cells in all directions, e.g., `rectangular-4x8`, and the directions are ordered from the shortest to the longest
* `size` is the number of lattice sites
    * Note that for fermionic models it is usually different from the number of fermions
* `boundary` is one in `O` (open in all directions), `P` (periodic in all directions), `PO` (periodic and open in two directions respectively, e.g., quasi-1D systems), `PA` (periodic and anti-periodic in two directions respectively)

## Examples

* `chain_32_P` is a 1D ring of 32 sites
* `square_16_P` is a 2D square lattice of `4 * 4 = 16` sites, with periodic boundaries in both directions
* `square_36_PA` is a 2D square lattice of `6 * 6 = 36` sites, with periodic and anti-periodic boundaries in x and y directions respectively
* `rectangular-4x8_32_PO` is a 2D rectangular lattice of `4 * 8 = 32` sites, with periodic boundaries in the short side and open boundaries in the long side
* `pyrochlore-2x2x2_32_P` is a 3D pyrochlore lattice of `2 * 2 * 2 = 8` unit cells, each containing `32 / 8 = 4` sites, with periodic boundaries in all directions
