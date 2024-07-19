| Energy              | Sigma | Energy Variance | DOF | Einf              | Method                          | Reference |
|---------------------|-------|-----------------|-----|-------------------|---------------------------------|-----------|
| -15.946847944277561 |       |                 | 16  | 7.741935483870968 | Exact diagonalization           | TODO: own code (ED) |
| -15.94684764968563  |       |                 | 16  | 7.741935483870968 | DMRG (maxbonddim = 200)         | [code](https://github.com/https://github.com/varbench/methods/blob/main/scripts/tV/chain_32_P_16_1/dmrg.sh) |
| -15.946847944066832 |  | 2.23852225644805e-09 | 16  | 7.741935483870968 | DMRG (maxbonddim = 573)         | [code](https://github.com/https://github.com/varbench/methods/blob/main/scripts/tV/chain_32_P_16_1/dmrg_B1024.sh) |
| -15.946206847643403 |       | 1.01e-3         | 16  | 7.741935483870968 | QMC (continuous-time expansion) | [paper](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.93.155117) [code](https://github.com/wangleiphy/SpinlesstV-LCT-INT) |
