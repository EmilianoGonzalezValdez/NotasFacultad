import numpy as np
from scipy.stats import chi2, binom


def Ej5():
    datos = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
    n = len(datos)

    p_est = np.mean(datos) / 8  # estimador de p
    N = np.array([datos.count(k) for k in range(9)])  # construye las frecs observadas
    # tambièn puede ser: np.bincount(datos, minlength=9)

    prob = np.array(
        [binom.pmf(k, 8, p_est) for k in range(9)]
    )  # calcula las probs teòricas de la binomial(n, p^)

    E = n * prob  # frecuecias esperadas

    T = np.sum((N - E) ** 2 / E)  # estadístico (N-np)^2
    pvalor = chi2.sf(T, df=7)  # P(χ^2_7 ​≥ T)

    print("p estimado =", p_est)
    print("T =", T)
    print("p-valor =", pvalor)

    Nsim = 10000
    count = 0

    for _ in range(Nsim):
        muestra = np.random.binomial(n=8, p=p_est, size=n)  # muestra simulada bajo H0
        p_sim = np.mean(muestra) / 8  # reestimar p

        # frecuencias observadas
        # N_sim = np.bincount(muestra, minlength=9)
        N_sim = np.array([np.sum(muestra == k) for k in range(9)])

        # frecuencias esperadas
        prob_sim = np.array([binom.pmf(k, 8, p_sim) for k in range(9)])

        E_sim = n * prob_sim  # E = np
        T_sim = np.sum((N_sim - E_sim) ** 2 / E_sim)  # estadìstico

        if T_sim >= T:
            count += 1

    pvalor_sim = count / Nsim

    print("p-valor simulado =", pvalor_sim)


Ej5()
