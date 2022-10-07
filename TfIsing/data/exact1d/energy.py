import math


def Epsilon(k, h):
    eps = 1.0 + h**2 + 2 * h * math.cos(k)
    return 2.0 * math.sqrt(eps)


L = 32
# Gamma is in units of the interaction srength
Gamma = 1
# V=1

pi = math.pi

energy = 0
for i in range(L):
    k = pi * (2.0 * i + 1.0) / float(L)
    energy += Epsilon(k, Gamma)


print(-0.5 * energy)
