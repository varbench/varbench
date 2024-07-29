| Energy            | Sigma | Energy Variance | DOF | Einf              | Method                          | Reference |
|-------------------|-------|-----------------|-----|-------------------|---------------------------------|-----------|
| -7.5021616707610725 |     |                 | 16  | 30.96774193548387 | Exact diagonalization           | [code](https://github.com/varbench/methods/blob/main/scripts/tV/chain_32_P_16_4/ed_lattice_symmetries.sh) |
| -7.50216163113578 |       |                 | 16  | 30.96774193548387 | DMRG (maxbonddim = 200)         | [code](https://github.com/varbench/methods/blob/main/scripts/tV/chain_32_P_16_4/dmrg.sh) |
| -7.48840482444892 |       | 2.05e-2         | 16  | 30.96774193548387 | QMC (continuous-time expansion) | [paper](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.93.155117) [code](https://github.com/wangleiphy/SpinlesstV-LCT-INT) |
