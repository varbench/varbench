# 16x16 cases (t1,t2,V1,V2)
## t1 = 1.0
## t2 = -0.25
## U = 8
## V1 = 1.0
## V2 = 0.5
## boundary condition: AP

| Energy    | Sigma   | Energy Variance | DOF | Einf              | Method                                                       | Reference |
|-----------|---------|-----------------|-----|-------------------|--------------------------------------------------------------|-----------|
| 322.35(6) | 0.00696 | 44.71(6)        | 214 | 894.0400735294118 | mVMC with SU(2) and momentum projections (gamma point) + RBM + Lanczos (Ne = 214), alpha = 2, with 1x1 RBM subpsace | [code](https://github.com/varbench/methods/blob/main/scripts/Hubbard/square_256_PA_107_8_t12_UV1V2/mVMC/mVMC.sh) |
