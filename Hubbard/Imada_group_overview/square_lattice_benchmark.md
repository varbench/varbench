# 8x8 cases
t = 1.0
U = 4 or 8
boundary condition: PP

| Energy     | Sigma    | Energy Variance | S(qmax) / Ns | qmax         | Method                                                                                  | RBM network choice              |
|------------|----------|-----------------|--------------|--------------|-----------------------------------------------------------------------------------------|---------------------------------|
| -72.344(4) | 0.000331 | 0.59(2)         | 0.00494(1)   | (3*pi/4, pi) | mVMC with SU(2) and momentum projections (gamma point) + RBM + Lanczos, (U=4) (Ne = 50) | alpha = 8, with 1x1 subblattice |
| -58.549(1) | 0.001031 | 2.58(1)         | 0.00636(2)   | (3*pi/4, pi) | mVMC with SU(2) and momentum projections (gamma point) + RBM + Lanczos, (U=8) (Ne = 50) | alpha = 8, with 1x1 subblattice |
| -54.986(3) | 0.00049  | 0.47(1)         |              | (pi, pi)     | mVMC with SU(2) and momentum projections (gamma point) + RBM + Lanczos, (U=4) (Ne = 64) | alpha = 4                       |
| -33.574(4) | 0.00061  | 0.62(3)         |              | (pi, pi)     | mVMC with SU(2) and momentum projections (gamma point) + RBM + Lanczos, (U=8) (Ne = 64) | alpha = 4                       |

# 16x16 cases
t = 1.0
U = 8
boundary condition: AP

| Energy     | Sigma  | Energy Variance | Method                                                                                   | RBM network choice              |
|------------|--------|-----------------|------------------------------------------------------------------------------------------|---------------------------------|
| -204.48(7) | 0.0175 | 49.7(16)        | mVMC with SU(2) and momentum projections (gamma point) + RBM + Lanczos, (U=4) (Ne = 214) | alpha = 1, full network         |
| -132.86(2) | 0.0044 | 8.1(3)          | mVMC with SU(2) and momentum projections (gamma point) + RBM + Lanczos, (U=4) (Ne = 256) | alpha = 2, with 4x4 subblattice |

# 16x16 cases (t1 and t2)
t1 = 1.0
t2 = -0.25
U = 8
boundary condition: AP

| Energy     | Sigma  | Energy Variance | Method                                                                                                | RBM network choice              |
|------------|--------|-----------------|-------------------------------------------------------------------------------------------------------|---------------------------------|
| -204.64(4) | 0.0095 | 43.6(11)        | mVMC with SU(2) and momentum projections (gamma point) + RBM + Lanczos (4x4 SC initial WF) (Ne = 214) | alpha = 1, with 4x4 subblattice |

# 16x16 cases (t1,t2,V1,V2)
t1 = 1.0
t2 = -0.25
U = 8
V1 = 1.0
V2 = 0.5
boundary condition: AP

| Energy    | Sigma   | Energy Variance | Method                                                                                                | RBM network choice              |
|-----------|---------|-----------------|-------------------------------------------------------------------------------------------------------|---------------------------------|
| 322.35(6) | 0.00696 | 44.71(6)        | mVMC with SU(2) and momentum projections (gamma point) + RBM + Lanczos (4x4 SC initial WF) (Ne = 214) | alpha = 2, with 1x1 subblattice |

NOTE:
alpha describes the "hidden variable density" defined as
alpha = (number hidden neurons in hidden layer) / (number of physical variables)
