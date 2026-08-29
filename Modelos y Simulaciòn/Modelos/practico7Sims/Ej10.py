import numpy as np
from scipy.stats import norm

# datos reales
N_obs = [91.9, 97.8, 111.4, 122.3, 105.4, 95.0, 103.8, 99.6, 96.6, 119.3, 104.8, 101.7]
n = len(N_obs)
N_obs.sort()

mu = np.mean(N_obs)
sigma = np.std(N_obs, ddof=1)
d_KS = 0
for j in range(n):
    F_exp = norm.cdf(N_obs[j], loc=mu, scale=sigma)
    d_KS = max(d_KS, (j + 1) / n - F_exp, F_exp - j / n)

# simulo
Nsim = 10000
pvalor = 0
for _ in range(Nsim):
    muestra_sim = norm.rvs(loc=mu, scale=sigma, size=n)
    muestra_sim.sort()
    mu_sim = np.mean(muestra_sim)
    sigma_sim = np.std(muestra_sim, ddof=1)

    d_sim = 0
    for j in range(n):
        f_sim = norm.cdf(muestra_sim[j], loc=mu_sim, scale=sigma_sim)
        d_sim = max(d_sim, (j + 1) / n - f_sim, f_sim - j / n)

    if d_sim >= d_KS:
        pvalor += 1

pvalor = pvalor / Nsim
print(f"D observado: {d_KS:.4f}")
print(f"p-valor aproximado por simulacion del test de KS: {pvalor}")
