import random
import math


def intensidad_arribos(t):
    """λ(t) según el enunciado (ciclo de 10h) [1]"""
    t_rel = t % 10
    if t_rel < 5:
        return 4 + 3 * t_rel
    else:
        return 19 - 3 * (t_rel - 5)


def generar_proximo_arribo(t_actual):
    """Algoritmo de Adelgazamiento (Thinning) [10]"""
    t = t_actual
    lam_max = 19
    while True:
        t += -math.log(1 - random.random()) / lam_max
        if t > 100:
            return math.inf  # No más arribos después de T=100 [11]
        if random.random() < intensidad_arribos(t) / lam_max:
            return t


def simulacion_ej7():
    """Simula una jornada de 100 horas y devuelve los datos para b y c [2]"""
    t = n = 0
    tA = generar_proximo_arribo(0)
    tD = math.inf
    tiempos_llegada = []
    esperas_totales = []  # Para el inciso (b)
    hubo_completitud_tardia = 0  # Para el inciso (c)

    # El servidor sigue trabajando hasta que el sistema quede vacío [4, 11]
    while tA < math.inf or n > 0:
        t_evento = min(tA, tD)
        t = t_evento

        if t_evento == tA:  # --- ARRIBO ---
            n += 1
            tiempos_llegada.append(t)
            if n == 1:  # Servidor libre: atiende de inmediato [4, 5]
                tD = t - math.log(1 - random.random()) / 13
            tA = generar_proximo_arribo(t)

        else:  # --- SALIDA ---
            llegada = tiempos_llegada.pop(0)
            esperas_totales.append(t - llegada)  # permanencia en el sistema
            if t > 100:
                hubo_completitud_tardia = 1

            n -= 1
            if n > 0:  # Hay gente en cola: sigue atendiendo [5]
                tD = t - math.log(1 - random.random()) / 13
            else:
                tD = math.inf

    avg_permanencia = (
        sum(esperas_totales) / len(esperas_totales) if esperas_totales else 0
    )
    return avg_permanencia, hubo_completitud_tardia


# --- BLOQUE ESTADÍSTICO (Inciso B) ---
def estimacion_b():
    n_sim = 1
    val, _ = simulacion_ej7()
    M = val
    S2 = 0
    while n_sim < 100 or math.sqrt(S2 / n_sim) >= 0.01:  # Criterio de parada [2, 9]
        n_sim += 1
        X, _ = simulacion_ej7()
        MAnt = M
        M = MAnt + (X - MAnt) / n_sim
        S2 = S2 * (1 - 1 / (n_sim - 1)) + n_sim * (M - MAnt) ** 2  # [7]
    return M, n_sim


# --- 3. ANÁLISIS ESTADÍSTICO RECURSIVO (INCISO C) ---
def estimacion_inciso_c(d_objetivo=0.01):
    """
    Estima la proporción p aplicando las fórmulas recursivas
    de la media muestral para variables Bernoulli [1].
    """
    n_sim = 0
    p = 0  # Estimador de la proporción

    # Condición de parada: n >= 100 y desvío estándar del estimador < 0.01 [1, 4]
    # El desvío de la proporción es sqrt( p*(1-p) / n )
    while n_sim < 100 or math.sqrt(p * (1 - p) / n_sim) >= d_objetivo:
        n_sim += 1
        _, X = simulacion_ej7()  # Obtenemos el éxito/fracaso de una simulación

        # Actualización recursiva de la proporción [1]
        p = p + (X - p) / n_sim

    return p, n_sim


print(simulacion_ej7())
print(f"B) Tiempo promedio en sistema: {estimacion_b()}")
probabilidad, total_sims = estimacion_inciso_c()
print(f"Probabilidad estimada (p): {probabilidad:.4f}")
print(f"Número de simulaciones realizadas: {total_sims}")
