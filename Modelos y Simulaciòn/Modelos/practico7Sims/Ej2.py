import random
from scipy import stats


def Binomial(n, p):
    c = p / (1 - p)
    prob = (1 - p) ** n
    F = prob
    i = 0
    U = random.random()
    while U >= F:
        prob *= c * (n - i) / (i + 1)
        F += prob
        i += 1
    return i


def Ej2():
    n = 1000
    n_real = [158, 172, 164, 181, 160, 165]
    p_teorica = 1 / 6
    t_obs = 0
    for i in range(6):
        t_obs += ((n_real[i] - n * p_teorica) ** 2) / (n * p_teorica)
    # Usamos la formula de las binomiales
    lamda1 = 1 / 6
    lamda2 = p_teorica / (1 - p_teorica)
    lamda3 = p_teorica / (1 - p_teorica * 2)
    lamda4 = p_teorica / (1 - p_teorica * 3)
    lamda5 = p_teorica / (1 - p_teorica * 4)

    n_simulaciones = 10000
    exitos_p_valor = 0
    for _ in range(n_simulaciones):
        n1_sim = Binomial(n, lamda1)
        n2_sim = Binomial(n - n1_sim, lamda2)
        n3_sim = Binomial(n - n1_sim - n2_sim, lamda3)
        n4_sim = Binomial(n - n1_sim - n2_sim - n3_sim, lamda4)
        n5_sim = Binomial(n - n1_sim - n2_sim - n3_sim - n4_sim, lamda5)
        n6_sim = n - n1_sim - n2_sim - n3_sim - n4_sim - n5_sim

        frecuencias_sim = [n1_sim, n2_sim, n3_sim, n4_sim, n5_sim, n6_sim]

        t_sim = 0
        for i in range(6):
            t_sim += ((frecuencias_sim[i] - n * p_teorica) ** 2) / (n * p_teorica)

        if t_sim >= t_obs:
            exitos_p_valor += 1

    p_valor = exitos_p_valor / n_simulaciones
    print(f"Estadistico observado(t0): {t_obs:.4f}")
    print(f"p-valor simulado: {p_valor:.4f}")


Ej2()
