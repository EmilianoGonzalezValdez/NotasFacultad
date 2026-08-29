from scipy.stats import expon, uniform

# datos reales
N_obs = expon.rvs(size=30)
N_obs.sort()
n = len(N_obs)

d_KS = 0
for j in range(n):
    exp_j = expon.cdf(N_obs[j])
    d_KS = max(d_KS, (j + 1) / n - exp_j, exp_j - j / n)

# simulando
Nsim = 10000
pvalor = 0
for _ in range(Nsim):
    uniformes = uniform.rvs(size=30)
    uniformes.sort()

    d_j = 0
    for j in range(n):
        u_j = uniformes[j]
        d_j = max(d_j, (j + 1) / n - u_j, u_j - j / n)

    if d_j >= d_KS:
        pvalor += 1

pvalor = pvalor / Nsim


print(f"El valor observado es: {d_KS}")
print(f"El p-valor te juro que es: {pvalor}")
