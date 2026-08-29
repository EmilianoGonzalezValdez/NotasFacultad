import random
import math
from scipy.stats import norm, uniform, binom, chi2
import numpy as np


def mediana_muestral(datos):
    return (datos[7] + datos[8]) / 2


print("---------------------------------------------------------")

print(
    "Ejercicio 2 incompleto, me falto terminar de comparar la mediana original con las estimadas y luego retocar para que me calcule bien la varianza del estimador"
)
print("---------------------------------------------------------")


def ejercicio2():
    datos_originales = [27, 25, 80, 79, 61, 55, 31, 35, 60, 8, 87, 89, 41, 90, 96, 63]
    n = len(datos_originales)
    mediana_muestrales = []
    mediana_obs = mediana_muestral(datos_originales)
    ECM_estimadores = []
    for i in range(5000):
        muestra = random.choices(datos_originales, k=n)
        muestra.sort()
        mediana = mediana_muestral(muestra)
        mediana_muestrales.append(mediana)
        ECM_estimadores.append((mediana - mediana_obs) ** 2)
    ECM_estimador = sum(ECM_estimadores) / 5000
    media_Estimador = sum(mediana_muestrales) / (5000)
    varianza_bootstrap = sum(
        (var - media_Estimador) ** 2 for var in mediana_muestrales
    ) / (10000 - 1)
    return varianza_bootstrap, ECM_estimador


def ejercicio3():

    datos = [
        491.455,
        496.387,
        491.175,
        502.551,
        509.838,
        491.708,
        501.39,
        496.717,
        494.769,
        503.901,
        502.351,
        503.617,
        501.754,
        497.783,
        501.019,
        501.494,
        502.689,
        501.762,
        509.541,
        504.808,
        507.551,
        498.701,
        501.114,
        504.87,
        506.344,
        511.543,
        496.488,
        498.155,
        501.201,
        507.446,
    ]
    tamaño = len(datos)
    datos.sort()
    d_KS = 0
    for j in range(tamaño):
        norm_j = norm.cdf(datos[j], loc=500, scale=5)
        d_KS = max(d_KS, (j + 1) / tamaño - norm_j, norm_j - j / tamaño)
    print(f"El estadistico observado D_obs es: {d_KS}")

    Nsim = 10000
    pvalor = 0
    for _ in range(Nsim):
        uniformes = uniform.rvs(size=tamaño)
        uniformes.sort()

        d_j = 0
        for j in range(tamaño):
            u_j = uniformes[j]
            d_j = max(d_j, (((j + 1) / tamaño) - u_j), u_j - (j / tamaño))

        if d_j >= d_KS:
            pvalor += 1
    pvalor = pvalor / Nsim
    print(f"El pvalor es: {pvalor}")

    if pvalor > 0.05:
        print(f"La hipotesis nula es aceptada para un error del 5%")
    else:
        print(f"La hipotesis nula es rechazada para un error del 5%")


def ejercicio4():
    n = 200
    frecuencias_obs = [25, 68, 70, 37]

    p_est = 0
    for j in range(4):
        p_est += frecuencias_obs[j] * j
    p_est = p_est / n  # Aca calculamos el estimador X barra
    p_est = p_est / 3  # Aca lo dividimos por n=3 por la n de la distribucion binomial

    prob = np.array(
        [binom.pmf(k, 3, p_est) for k in range(4)]
    )  # calcula las probs teòricas de la binomial(n, p^)

    E = n * prob  # frecuecias esperadas

    T = np.sum((frecuencias_obs - E) ** 2 / E)  # estadístico (N-np)^2
    pvalor = chi2.sf(T, df=2)

    print("p estimado =", p_est)
    print("T =", T)
    print("p-valor =", pvalor)

    Nsim = 10000
    count = 0

    for _ in range(Nsim):
        muestra = np.random.binomial(n=3, p=p_est, size=n)  # muestra simulada bajo H0
        p_sim = np.mean(muestra) / 3  # reestimar p

        N_sim = np.array([np.sum(muestra == k) for k in range(4)])

        # frecuencias esperadas
        prob_sim = np.array([binom.pmf(k, 3, p_sim) for k in range(4)])

        E_sim = n * prob_sim  # E = np
        T_sim = np.sum((N_sim - E_sim) ** 2 / E_sim)  # estadìstico

        if T_sim >= T:
            count += 1

    pvalor_sim = count / Nsim

    print("p-valor simulado =", pvalor_sim)

    if pvalor_sim < 0.2:
        print("La hipotesis nula es rechazada con un error del 20%")
    else:
        print("L hipotesis nula es aceptada con un error del 20%")


print(f"--------------ejercicio2-------------------")
print(ejercicio2())
print(f"--------------ejercicio3-------------------")
ejercicio3()
print(f"--------------ejercicio4-------------------")
ejercicio4()
