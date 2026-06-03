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
            return math.inf  # No más arribos después de T=100
        if random.random() < intensidad_arribos(t) / lam_max:
            return t


def simulacion_ej8():
    """Simula una jornada de 100 horas y devuelve los datos para b y c [2]"""
    t = n = 0
    tA = generar_proximo_arribo(0)
    tD = math.inf
    tF = math.inf
    tiempos_llegada = []
    esperas_totales = []  # Para el inciso (b)
    cafeecitoo = []  # Para el inciso (c)

    # El servidor sigue trabajando hasta que el sistema quede vacío
    while tA < math.inf or n > 0 or tF < math.inf:
        t_evento = min(tA, tD, tF)
        t = t_evento

        if t_evento == tA:  # --- ARRIBO ---
            n += 1
            tiempos_llegada.append(t)
            if n == 1 and (
                t >= tF or tF == math.inf
            ):  # Servidor libre: atiende de inmediato
                tD = t - math.log(1 - random.random()) / 13
            tA = generar_proximo_arribo(t)

        elif t_evento == tD:  # --- SALIDA ---
            llegada = tiempos_llegada.pop(0)
            esperas_totales.append(t - llegada)  # permanencia en el sistema

            n -= 1
            if n > 0:  # Hay gente en cola: sigue atendiendo
                tD = t - math.log(1 - random.random()) / 13
            else:
                tD = math.inf
                tF = t + random.uniform(0, 0.3)
                cafeecitoo.append(min(tF - t, 100 - t))
        elif t_evento == tF:  # ---- CAFESITO ----
            if n > 0:
                tD = t - math.log(1 - random.random()) / 13
                tF = math.inf
            else:
                tF = t + random.uniform(0, 0.3)
                cafeecitoo.append(min(tF - t, 100 - t))
        if t >= 100 and n == 0:
            tF = math.inf

    avg_permanencia = (
        sum(esperas_totales) / len(esperas_totales) if esperas_totales else 0
    )
    avg_cafecitoo = sum(cafeecitoo) if cafeecitoo else 0
    return avg_permanencia, avg_cafecitoo


# --- BLOQUE ESTADÍSTICO (Inciso B) ---
def estimacion_b():
    n_sim = 1
    val, _ = simulacion_ej8()
    M = val
    S2 = 0
    while n_sim < 100 or math.sqrt(S2 / n_sim) >= 0.05:
        n_sim += 1
        X, _ = simulacion_ej8()
        MAnt = M
        M = MAnt + (X - MAnt) / n_sim
        S2 = S2 * (1 - 1 / (n_sim - 1)) + n_sim * (M - MAnt) ** 2  # [7]
    return M, n_sim


# --- BLOQUE ESTADÍSTICO (Inciso C) ---
def estimacion_c():
    n_sim = 1
    _, val = simulacion_ej8()
    M = val
    S2 = 0
    while n_sim < 100 or math.sqrt(S2 / n_sim) >= 0.05:
        n_sim += 1
        _, X = simulacion_ej8()
        MAnt = M
        M = MAnt + (X - MAnt) / n_sim
        S2 = S2 * (1 - 1 / (n_sim - 1)) + n_sim * (M - MAnt) ** 2  # [7]
    return M, n_sim


print(f"A) Ejercicio raro: {simulacion_ej8()}")
print(f"B) Tiempo promedio en sistema: {estimacion_b()}")
print(f"C) Tiempo promedio en sistema: {estimacion_c()}")
