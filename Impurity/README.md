
# Impurity Hamiltonian
A typical Anderson impurity Hamiltonian $\hat{H}_{A}$ contains two parts

$$\hat{H}_\mathrm{A}  = \hat{H}_\mathrm{loc} + \hat{H}_\mathrm{bath}, $$

$$\hat{H}_\mathrm{loc}  = \sum_{\{ \alpha\} }\epsilon^0_{\alpha_1\alpha_2}\hat{d}^{\dagger}_{\alpha_1}\hat{d}_{\alpha_2} + \sum_{\{\alpha\}} U_{\alpha_1\alpha_2\alpha_3\alpha_4}\hat{d}^{\dagger}_{\alpha_1}\hat{d}^{\dagger}_{\alpha_2}\hat{d}_{\alpha_3}\hat{d}_{\alpha_4},$$

$$\hat{H}_\mathrm{bath}  = \sum_{\{\alpha\},l=1}^{l=N_b}\epsilon^{l}_{\alpha_1\alpha_2}\hat{c}^{\dagger}_{l\alpha_1}\hat{c}_{l\alpha_2} + \sum_{\{\alpha\},l=1}^{l=N_b}\left( \nu_{\alpha_1\alpha_2}^{l}\hat{d}^\dagger_{\alpha_1}c_{l\alpha_2}+ h.c. \right),$$

where a locally interacting impurity is coupled to a non-interacting bath. Here, we consider two types of interactions that are frequently encountered in DMFT calculations: the single-band Hubbard interaction

$$\hat{H}_\mathrm{loc} = U \hat{n}_{\uparrow} \hat{n}_{\downarrow} + \epsilon^0 \left(\hat{n}_{\uparrow} + \hat{n}_{\downarrow} \right),$$

and the three-band rotationally invariant Kanamori interaction

$$\hat{H}_\mathrm{loc} = \hat{H}_\mathrm{DD} + \hat{H}_\mathrm{SF} +\hat{H}_\mathrm{PH} ,$$

$$\hat{H}_\mathrm{DD} = U \sum_{m} \hat{n}_{m\uparrow} \hat{n}_{m\downarrow} + \left(U-2J\right) \sum_{m'>m,\sigma} \hat{n}_{m\sigma} \hat{n}_{m'\overline{\sigma}}
	+\left(U-3J\right) \sum_{m'>m,\sigma} \hat{n}_{m\sigma} \hat{n}_{m'\sigma},$$

$$\hat{H}_\mathrm{SF} = J \sum_{m' m}\left( \hat{d}^\dagger_{m\uparrow} \hat{d}_{m \downarrow} \hat{d}_{m'\uparrow} \hat{d}^\dagger_{m' \downarrow} + h.c.\right),$$

$$\hat{H}_\mathrm{PH} =-J\sum_{m'>m}\left( \hat{d}^\dagger_{m\uparrow}\hat{d}^\dagger_{m\downarrow}\hat{d}_{m'\uparrow}\hat{d}_{m'\uparrow} + h.c. \right),$$

with $m\in\{1,2,3\}$ being the orbital index. **DD**, **SF** and **PH** denotes the density-density, spin-flip ,and pair-hopping interaction, respectively.


We have constructed the following models one might need to solve in typical DMFT calculations: (**SB_Imp**) single-band Anderson impurity model with a semielliptic spectral function, i.e., $-\frac{1}{\pi}\mathrm{Im}\Delta(\omega) = \frac{2}{\pi D }\sqrt{1-(\omega/D)^2}$ with $D$ being the half-bandwidth and $U=D$; (**SB_DMFT_MT_HF**) DMFT metal solution of the single band Hubbard model on the Bethe lattice with $U=2D$ at half-filling $n=1$ and (**SB_DMFT_MT_AHF**) doped case $n=0.8$ ; (**SB_DMFT_MI_HF**) DMFT Mott-insulator solution of the single band Hubbard model on the Bethe lattice with $U=4D$ at half-filling $n=1$; 
three-band models with Kanamori interaction ($U=2.3$ ev and $J=0.4$ ev) that are based on the material-realistic DMFT solutions of the archetypal Hund's metal Sr$_2$RuO$_4$ in the $t_{2g}$ subspace (**TB_DMFT_SOC**) with and (**TB_DMFT**) without spin-orbit coupling.


# Naming
The names of the data files follow the convention `model_Nb.md`
* `model` is the name of the model
* `Nb` is the number of bath sites per spin-orbital



