import math
from random import gauss, gammavariate
from math import erf, sqrt
from scipy.stats import uniform


def rt(df):  # df grados de libertad
    x = gauss(0.0, 1.0)
    y = 2 * gammavariate(0.5 * df, 2.0)
    return x / (sqrt(y / df))


def acumulada_normal(x):
    return math.erf(x / math.sqrt(2.0)) / 2.0 + 0.5


def ejercicio(tamaño):
    datos = []
    for i in range(tamaño):
        datos.append(rt(11))
    datos.sort()

    d_KS = 0
    for j in range(tamaño):
        norm_j = acumulada_normal(datos[j])
        d_KS = max(d_KS, (j + 1) / tamaño - norm_j, norm_j - j / tamaño)

    # simulando
    Nsim = 10000
    pvalor = 0
    for _ in range(Nsim):
        uniformes = uniform.rvs(size=tamaño)
        uniformes.sort()

        d_j = 0
        for j in range(tamaño):
            u_j = uniformes[j]
            d_j = max(d_j, (j + 1) / tamaño - u_j, u_j - j / tamaño)

        if d_j >= d_KS:
            pvalor += 1

    pvalor = pvalor / Nsim

    print(f"El p-valor te juro que es: {pvalor}")


ejercicio(10)
ejercicio(20)
ejercicio(100)
ejercicio(1000)
