import numpy as np
from scipy.stats import chi2, binom

datos = [38, 144, 342, 287, 164, 25]
n = sum(datos)

N = datos  # frecs observadas

media_muestral = 0  # x barra
for i in range(len(datos)):
    media_muestral += datos[i] * i
media_muestral /= 1000

p_est = media_muestral / 5  # estimador de p
prob = np.array([binom.pmf(k, 5, p_est) for k in range(6)])  # probs teoricas
E = n * prob  # frecs esperadas

T = np.sum((N - E) ** 2 / E)  # estadistico
pvalor = chi2.sf(T, df=4)  # P(chi2_4 >= T)

print("p estimado:", p_est)
print("T:", T)
print("p-valor:", pvalor)
Nsim = 1000
exitos = 0

for _ in range(Nsim):
    muestra = np.random.binomial(n=5, p=p_est, size=n)  # muestra sim bajo H0
    p_sim = np.mean(muestra) / 5  # reestimar p

    N_sim = np.array([np.sum(muestra == k) for k in range(6)])  # frecs observadas

    prob_sim = np.array([binom.pmf(k, 5, p_sim) for k in range(6)])  # frecs esperadas

    E_sim = n * prob_sim  # E = n*p
    T_sim = np.sum((N_sim - E_sim) ** 2 / E_sim)  # estadistico

    if T_sim >= T:
        exitos += 1

pvalor_sim = exitos / Nsim

print("frecs esperadas:", E)
print("p-valor simulado:", pvalor_sim)
