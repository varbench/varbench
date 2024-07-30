| Energy              | Sigma  | Energy Variance   | DOF | Einf | Method                                | Reference |
|---------------------|--------|-------------------|-----|------|---------------------------------------|-----------|
| -221.941            | 0.004  | 11.17             | 100 | 0    | VMC with fermions (flux+neel+Jastrow) | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_100_P_0.3/vmc_gutzwiller.sh) |
| -219.63545043455386 |        | 31.09655723764445 | 100 | 0    | DMRG (bond dimension = 1024)          | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_100_P_0.3/dmrg.sh) |
| -218.3978           | 0.0073 | 54.28278          | 100 | 0    | RBM (alpha = 1)                       | TODO: own code (RBM) |
| -218.1436           | 0.0068 | 47.92829          | 100 | 0    | Jastrow baseline                      | [code](https://github.com/varbench/methods/blob/main/scripts/J1J2/square_100_P_0.3/vmc_jastrow.sh) |
