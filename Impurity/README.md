# Impurity Hamiltonians

A typical Anderson impurity Hamiltonian $\hat{H}_\text{A}$ contains two parts

$$\hat{H}_\text{A} = \hat{H}_\text{loc} + \hat{H}_\text{bath},$$

$$\hat{H}_\text{loc} = \sum_{\\{\alpha\\}} \epsilon^0_{\alpha_1 \alpha_2} \hat{d}^{\dagger}_{\alpha_1} \hat{d}_{\alpha_2} + \sum_{\\{\alpha\\}} U_{\alpha_1 \alpha_2 \alpha_3 \alpha_4} \hat{d}^{\dagger}_{\alpha_1} \hat{d}^{\dagger}_{\alpha_2} \hat{d}_{\alpha_3} \hat{d}_{\alpha_4},$$

$$\hat{H}_\text{bath} = \sum_{\\{\alpha\\}, l = 1}^{l = N_b} \epsilon^l_{\alpha_1 \alpha_2} \hat{c}^{\dagger}_{l \alpha_1} \hat{c}_{l \alpha_2} + \sum_{\\{\alpha\\}, l = 1}^{l = N_b} \left( \nu^l_{\alpha_1 \alpha_2} \hat{d}^\dagger_{\alpha_1} \hat{c}_{l \alpha_2} + \text{h.c.} \right),$$

where a locally interacting impurity is coupled to a non-interacting bath. Here, we consider two types of interactions that are frequently encountered in DMFT calculations: the single-band Hubbard interaction

$$\hat{H}_\text{loc} = U \hat{n}_{\uparrow} \hat{n}_{\downarrow} + \epsilon^0 \left( \hat{n}_{\uparrow} + \hat{n}_{\downarrow} \right),$$

and the three-band rotationally invariant Kanamori interaction

$$\hat{H}_\text{loc} = \hat{H}_\text{DD} + \hat{H}_\text{SF} +\hat{H}_\text{PH},$$

$$\hat{H}_\text{DD} = U \sum_m \hat{n}_{m \uparrow} \hat{n}_{m \downarrow} + (U - 2 J) \sum_{m' > m, \sigma} \hat{n}_{m \sigma} \hat{n}_{m' \bar{\sigma}} + (U - 3 J) \sum_{m' > m, \sigma} \hat{n}_{m \sigma} \hat{n}_{m' \sigma},$$

$$\hat{H}_\text{SF} = J \sum_{m' m} \left( \hat{d}^\dagger_{m \uparrow} \hat{d}_{m \downarrow} \hat{d}_{m' \uparrow} \hat{d}^\dagger_{m' \downarrow} + \text{h.c.} \right),$$

$$\hat{H}_\text{PH} = -J \sum_{m' > m} \left( \hat{d}^\dagger_{m \uparrow} \hat{d}^\dagger_{m \downarrow} \hat{d}_{m' \uparrow} \hat{d}_{m' \downarrow} + \text{h.c.} \right),$$

with $m \in \\{1, 2, 3\\}$ being the orbital index, and **DD**, **SF**, and **PH** denote the density-density, the spin-flip, and the pair-hopping interactions respectively.

We have constructed the following models one might need to solve in typical DMFT calculations:
(**SB_Imp**) single-band Anderson impurity model with a semielliptic spectral function, i.e., $-\frac{1}{\pi} \mathrm{Im} \Delta(\omega) = \frac{2}{\pi D} \sqrt{1 - \left( \frac{\omega}{D} \right)^2}$ with $D$ being the half-bandwidth and $U = D$;
(**SB_DMFT_MT_HF**) DMFT metal solution of the single band Hubbard model on the Bethe lattice with $U = 2 D$ at half-filling $n = 1$ and
(**SB_DMFT_MT_AHF**) doped case $n = 0.8$;
(**SB_DMFT_MI_HF**) DMFT Mott-insulator solution of the single band Hubbard model on the Bethe lattice with $U = 4 D$ at half-filling $n = 1$;
three-band models with Kanamori interaction $U = 2.3\ \text{eV}$ and $J = 0.4\ \text{eV}$ that are based on the material-realistic DMFT solutions of the archetypal Hund's metal Sr<sub>2</sub>RuO<sub>4</sub> in the $t_{2 g}$ subspace (**TB_DMFT_SOC**) with and (**TB_DMFT**) without spin-orbit coupling.

# Naming

The names of the data files follow the convention `model_Nb.md`

* `model` is the name of the model
* `Nb` is the number of bath sites per spin-orbital
