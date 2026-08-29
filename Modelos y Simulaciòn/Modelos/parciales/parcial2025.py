from random import random
import math
from scipy.stats import expon, uniform


print(f"EJERCICIOOOOO 2 --------------------------------------")
D_obs = [
    15.22860536,
    40.60145536,
    33.67482894,
    44.03841737,
    15.69560109,
    16.2321714,
    25.02174735,
    30.34655637,
    3.3181228,
    5.69447539,
    10.1119561,
    49.10266584,
    3.6536329,
    35.82047148,
    3.37816632,
    36.72299321,
    50.67085322,
    3.25476304,
    20.12426236,
    20.2668814,
    17.49593589,
    2.70768636,
    14.77332745,
    1.72267967,
    23.34685662,
    8.46376635,
    9.18330789,
    9.97428217,
    2.33951729,
    137.51657441,
    9.79485269,
    10.40308179,
    1.57849658,
    6.26959703,
    4.74251574,
    1.53479053,
    34.74136011,
    27.47600572,
    9.1075566,
    1.88056595,
    27.59551348,
    6.82283137,
    12.45162807,
    28.01983651,
    0.36890593,
    7.82520791,
    3.17626161,
    46.91791271,
    38.08371186,
    41.10961135,
]
n = len(D_obs)
D_obs.sort()

# b
d_KS = 0
for j in range(n):
    F_exp = expon.cdf(D_obs[j], scale=(1 / 0.05))
    d_KS = max(d_KS, (j + 1) / n - F_exp, F_exp - j / n)

# c
Nsim = 10000
pvalor = 0
for _ in range(Nsim):
    uniformes = uniform.rvs(size=n)
    uniformes.sort()

    d_j = 0
    for j in range(n):
        u_j = uniformes[j]
        d_j = max(d_j, (j + 1) / n - u_j, u_j - j / n)

    if d_j >= d_KS:
        pvalor += 1

pvalor = pvalor / Nsim

if pvalor < 0.04:
    print(f"Se rechaza la H0 pq el p-valor es: {pvalor * 100:.2f}%")
else:
    print(f"Se acepta la H0 pq el p-valor es: {pvalor * 100:.2f}%")


print(f"INCISO D---------------------------------------------")

D_obs = [
    15.22860536,
    40.60145536,
    33.67482894,
    44.03841737,
    15.69560109,
    16.2321714,
    25.02174735,
    30.34655637,
    3.3181228,
    5.69447539,
    10.1119561,
    49.10266584,
    3.6536329,
    35.82047148,
    3.37816632,
    36.72299321,
    50.67085322,
    3.25476304,
    20.12426236,
    20.2668814,
    17.49593589,
    2.70768636,
    14.77332745,
    1.72267967,
    23.34685662,
    8.46376635,
    9.18330789,
    9.97428217,
    2.33951729,
    137.51657441,
    9.79485269,
    10.40308179,
    1.57849658,
    6.26959703,
    4.74251574,
    1.53479053,
    34.74136011,
    27.47600572,
    9.1075566,
    1.88056595,
    27.59551348,
    6.82283137,
    12.45162807,
    28.01983651,
    0.36890593,
    7.82520791,
    3.17626161,
    46.91791271,
    38.08371186,
    41.10961135,
]
n = len(D_obs)
D_obs.sort()

# b
d_KS = 0
for j in range(n):
    F_exp = expon.cdf(D_obs[j], scale=(1 / 0.05))
    d_KS = max(d_KS, (j + 1) / n - F_exp, F_exp - j / n)

# c
Nsim = 10000
pvalor = 0
for _ in range(Nsim):
    exponenciales = expon.rvs(size=n, scale=1 / 0.05)
    exponenciales.sort()

    d_j = 0
    for j in range(n):
        u_j = expon.cdf(exponenciales[j], scale=1 / 0.05)
        d_j = max(d_j, (j + 1) / n - u_j, u_j - j / n)

    if d_j >= d_KS:
        pvalor += 1

pvalor = pvalor / Nsim

if pvalor < 0.0004:
    print(f"Se rechaza la H0 pq el p-valor es: {pvalor * 100:.2f}%")
else:
    print(f"Se acepta la H0 pq el p-valor es: {pvalor * 100:.2f}%")
