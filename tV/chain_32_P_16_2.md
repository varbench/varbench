| Energy             | Sigma | Energy Variance | DOF | Einf              | Method                          | Reference |
|--------------------|-------|-----------------|-----|-------------------|---------------------------------|-----------|
| -12.32869972364372 |       |                 | 16  | 15.48387096774194 | Exact diagonalization           | TODO: own code (ED) |
| -12.32869928774351 |       |                 | 16  | 15.48387096774194 | DMRG (maxbonddim = 200)         | [code](https://github.com/varbench/methods/blob/main/scripts/tV/chain_32_P_16_2/dmrg.sh) |
| -12.32494350621494 |       | 5.05e-3         | 16  | 15.48387096774194 | QMC (continuous-time expansion) | [paper](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.93.155117) [code](https://github.com/wangleiphy/SpinlesstV-LCT-INT) |
