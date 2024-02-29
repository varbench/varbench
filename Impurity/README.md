# Impurity Hamiltonians

A typical Anderson impurity Hamiltonian $\hat{H}_\text{A}$ contains two parts

```math
\hat{H}_\text{A} = \hat{H}_\text{loc} + \hat{H}_\text{bath},
```

```math
\hat{H}_\text{loc} = \sum_{\\{\alpha\\}} \epsilon^0_{\alpha_1 \alpha_2} \hat{d}^{\dagger}_{\alpha_1} \hat{d}_{\alpha_2} + \sum_{\\{\alpha\\}} U_{\alpha_1 \alpha_2 \alpha_3 \alpha_4} \hat{d}^{\dagger}_{\alpha_1} \hat{d}^{\dagger}_{\alpha_2} \hat{d}_{\alpha_3} \hat{d}_{\alpha_4},
```

```math
\hat{H}_\text{bath} = \sum_{\\{\alpha\\}, l = 1}^{l = N_\text{b}} \epsilon^l_{\alpha_1 \alpha_2} \hat{c}^{\dagger}_{l \alpha_1} \hat{c}_{l \alpha_2} + \sum_{\\{\alpha\\}, l = 1}^{l = N_\text{b}} \left( \nu^l_{\alpha_1 \alpha_2} \hat{d}^\dagger_{\alpha_1} \hat{c}_{l \alpha_2} + \text{h.c.} \right),
```

where a locally interacting impurity is coupled to a non-interacting bath. Here, we consider two types of interactions that are frequently encountered in DMFT calculations: the single-band Hubbard interaction

```math
\hat{H}_\text{loc} = U \hat{n}_{\uparrow} \hat{n}_{\downarrow} + \epsilon^0 \left( \hat{n}_{\uparrow} + \hat{n}_{\downarrow} \right),
```

and the three-band rotationally invariant Kanamori interaction

```math
\hat{H}_\text{loc} = \hat{H}_\text{DD} + \hat{H}_\text{SF} +\hat{H}_\text{PH},
```

```math
\hat{H}_\text{DD} = U \sum_m \hat{n}_{m \uparrow} \hat{n}_{m \downarrow} + (U - 2 J) \sum_{m' > m, \sigma} \hat{n}_{m \sigma} \hat{n}_{m' \bar{\sigma}} + (U - 3 J) \sum_{m' > m, \sigma} \hat{n}_{m \sigma} \hat{n}_{m' \sigma},
```

```math
\hat{H}_\text{SF} = J \sum_{m' m} \left( \hat{d}^\dagger_{m \uparrow} \hat{d}_{m \downarrow} \hat{d}_{m' \uparrow} \hat{d}^\dagger_{m' \downarrow} + \text{h.c.} \right),
```

```math
\hat{H}_\text{PH} = -J \sum_{m' > m} \left( \hat{d}^\dagger_{m \uparrow} \hat{d}^\dagger_{m \downarrow} \hat{d}_{m' \uparrow} \hat{d}_{m' \downarrow} + \text{h.c.} \right),
```

with $m \in \\{1, 2, 3\\}$ being the orbital index, and **DD**, **SF**, and **PH** denote the density-density, the spin-flip, and the pair-hopping interactions respectively.

We have constructed the following models one might need to solve in typical DMFT calculations:
(**SB-Imp**) single-band Anderson impurity model with a semielliptic spectral function, i.e., $-\frac{1}{\pi} \mathrm{Im} \Delta(\omega) = \frac{2}{\pi D} \sqrt{1 - \left( \frac{\omega}{D} \right)^2}$ with $D$ being the half-bandwidth and $U = D$;
(**SB-DMFT-MT-HF**) DMFT metal solution of the single band Hubbard model on the Bethe lattice with $U = 2 D$ at half-filling $n = 1$ and
(**SB-DMFT-MT-AHF**) doped case $n = 0.8$;
(**SB-DMFT-MI-HF**) DMFT Mott-insulator solution of the single band Hubbard model on the Bethe lattice with $U = 4 D$ at half-filling $n = 1$;
three-band models with Kanamori interaction $U = 2.3\ \text{eV}$ and $J = 0.4\ \text{eV}$ that are based on the material-realistic DMFT solutions of the archetypal Hund's metal Sr<sub>2</sub>RuO<sub>4</sub> in the $t_{2 g}$ subspace (**TB-DMFT-SOC**) with and (**TB-DMFT**) without spin-orbit coupling.

# Naming

The names of the data files follow the convention `model_Nb.md`

* `model` is the name of the impurity model
* `Nb` is the number of bath sites per spin-orbital

# Hamiltonian
The impurity Hamitonian parameters are store in `HamParams` folder. The names of the Hamiltonian follow the same convention of `model_Nb.h5`. The following example python script describes their data structure
```python 
import h5py

file_name = "TB-DMFT-SOC_19.h5"
with h5py.File(file_name, "r") as file:
    # Retrieve the local single-particle Hamiltonian on the impurity
    e0 = file['e0']
    # Retrieve the bath parameters
    bath = file['bath']

    # For non spin orbit coupling case, the spin_orb_key is ["up", "down"]
    # For spin orbit coupling case, the spin_orb_key is ["ud_0", "ud_1"]
    spin_orb_key = "ud_1"

    # Retrieve the on-site single particle Hamiltonian on the impurity
    # The shape is complex (n_orb, n_orb)
    hloc = e0['hloc'][spin_orb_key][()][:,:,0] + 1j * e0['hloc'][spin_orb_key][()][:,:,1]

    # Define the impurity and bath indices
    i_imp = 0
    i_bath = 8

    # Retrieve the hopping matrix between the i_imp impurity and the ibath bath
    # The shape is complex (n_orb)
    V = bath['bath'][spin_orb_key][f"{i_imp}"][f"{i_bath}"]["V"][()][:,0] + 1j * bath['bath'][spin_orb_key][f"{i_imp}"][f"{i_bath}"]["V"][()][:,1]


    # Retrieve the on-site energy of the i_bath bath belonging to the i_imp impurity
    # This is a real scalar value
    eps = bath['bath'][spin_orb_key][f"{i_imp}"][f"{i_bath}"]["eps"][()]

```