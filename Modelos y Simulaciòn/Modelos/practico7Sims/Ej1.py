from scipy import stats
import random

print(1 - stats.chi2.cdf(2.1798, df=5))


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


def ejercicio_1_b():
    n = 564
    # Frecuencias observadas en el experimento real
    N_real = [141, 291, 132]
    # Probabilidades teóricas de Mendel
    p_teorico = [0.25, 0.50, 0.25]

    # 1. Calcular el estadístico observado (t_obs)
    t_obs = 0
    for i in range(3):
        esperado = n * p_teorico[i]
        t_obs += (N_real[i] - esperado) ** 2 / esperado

    # 2. Parámetros para la simulación encadenada
    # Probabilidad de ser blanca en el total
    lamda1 = p_teorico[0]
    # Probabilidad de ser rosa dado que NO fue blanca
    lamda2 = p_teorico[1] / (1 - p_teorico[0])  # 0.50 / 0.75 = 2/3

    # 3. Bucle de Simulación (Mundos paralelos)
    N_SIM = 10000
    exitos_p_valor = 0

    for _ in range(N_SIM):
        # Generamos las frecuencias directamente usando Binomiales
        n1_sim = Binomial(n, lamda1)  # Cuántas blancas
        n2_sim = Binomial(n - n1_sim, lamda2)  # Cuántas rosas de las que quedan
        n3_sim = n - n1_sim - n2_sim  # El resto son rojas

        frec_sim = [n1_sim, n2_sim, n3_sim]

        # Calcular T_sim para esta muestra de azar
        t_sim = 0
        for i in range(3):
            esperado = n * p_teorico[i]
            t_sim += (frec_sim[i] - esperado) ** 2 / esperado

        # Contamos si el azar fue igual o más extremo que la realidad
        if t_sim >= t_obs:
            exitos_p_valor += 1

    p_valor = exitos_p_valor / N_SIM
    print(f"Estadístico observado (t0): {t_obs:.4f}")
    print(f"p-valor simulado: {p_valor:.4f}")


ejercicio_1_b()
print(1 - stats.chi2.cdf(0.2685, df=2))
