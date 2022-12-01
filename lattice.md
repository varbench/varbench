# Lattice naming convention

Hamiltonians specified on lattices follow a brief naming convention to specify the geometry.
Each lattice name contains information about its geometry, extent, and boundary conditions.

## Examples

* `chain_32_P` is a 1D ring of 32 sites
* `square_12_PP` is a 2D square lattice of 12x12 sites, with periodic boundaries in both directions
* `square_12_AP` is a 2D square lattice of 12x12 sites, with antiperiodic and periodic boundaries in x and y directions respectively
* `rectangular_4x30_PO` is a 2D rectangular lattice of 4x30 sites, with periodic boundaries in the short side and open boundaries in the long side. To avoid duplication, please order the sides from the shortest to the longest
* `cubic_10_PPP` is a 3D cubic lattice of 10x10x10 sites, with periodic boundaries in all directions, etc...

## TODO

A python script to convert these names into lattice points is also provided for convenience.
