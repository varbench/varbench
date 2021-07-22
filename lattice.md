# Lattice naming conventions

Models specified on lattices follow a simple naming convention to specify the geometry.
Each lattice name contains information about its geometry, extent, and boundary conditions.

## Examples

`chain_32_P` is a 1d ring of 32 sites

`square_12_PP` is a 2d square lattice 12x12 with periodic boundaries in both directions

`rectangular_4x30_PO` is a rectangular lattice with periodic boundaries along the short side and open boundaries along the long side

`cubic_10_PPP` is a cubic lattice with periodic boundaries along all directions, etc...).


### TODO

A python script to convert these names into lattice points is also provided for convenience
