import random
import math


# --- GENERADORES DE TIEMPOS ---
def generar_falla():
    return -math.log(1 - random.random()) / 2


def generar_reparacion():
    return -math.log(1 - random.random()) / 3


# --- MOTOR DE UNA CORRIDA (HASTA EL COLAPSO) ---
def simular_reparacion_hasta_falla():
    n = 6
    s = 4
    t = 0
    r = 0  # Máquinas averiadas

    # Inicialización: Tiempos de falla iniciales para las n máquinas
    ti = [generar_falla() for _ in range(n)]
    t_star = math.inf  # No hay nadie reparando al inicio

    while r <= s:
        # El próximo evento es el mínimo entre todas las fallas y la reparación
        proximo_evento = min(min(ti), t_star)

        # CASO 1: Falla una máquina (evento es alguno de los ti)
        if proximo_evento < t_star:
            # Encontrar qué máquina falló
            idx = ti.index(proximo_evento)
            t = ti[idx]
            r += 1

            if r > s:
                # MUERTE: No había repuestos para la máquina que falló
                break

            if r == 1:
                # Es la primera máquina en fallar, empieza reparación
                t_star = t + generar_reparacion()

            ti[idx] = t + generar_falla()

        # CASO 2: Termina una reparación (evento es t_star)
        else:
            t = t_star
            r -= 1

            if r > 0:
                # Sigue reparando la siguiente en cola
                t_star = t + generar_reparacion()
            else:
                t_star = math.inf

    return t  # Tiempo de colapso


def resolver_ejercicio_11():
    n_sim = 0

    # Acumuladores Inciso B (MTTF, d < 0.01)
    mb = 0.0
    s2b = 0.0

    # Acumuladores Inciso D (Proporción < 1.5hs, d < 0.01)
    pd = 0.0

    while True:
        n_sim += 1
        t_colapso = simular_reparacion_hasta_falla()

        # --- Actualización Inciso B (MTTF) ---
        mb_ant = mb
        mb = mb_ant + (t_colapso - mb_ant) / n_sim
        if n_sim > 1:
            s2b = s2b * (1 - 1 / (n_sim - 1)) + n_sim * (mb - mb_ant) ** 2

        # --- Actualización Inciso D (Proporción) ---
        x_d = 1 if t_colapso < 1.5 else 0
        pd = pd + (x_d - pd) / n_sim

        # --- Verificación de Criterios de Parada ---
        if n_sim >= 100:
            err_b = math.sqrt(s2b / n_sim)
            err_d = math.sqrt(pd * (1 - pd) / n_sim)

            if err_b < 0.01 and err_d < 0.01:
                break

    # --- Resultados Finales (e Intervalos 95% -> z = 1.96) ---
    print(f"Simulaciones totales: {n_sim}")

    ic_b = 1.96 * math.sqrt(s2b / n_sim)
    print(f"B) MTTF: {mb:.4f} ± {ic_b:.4f} horas")

    ic_d = 1.96 * math.sqrt(pd * (1 - pd) / n_sim)
    print(f"D) Prob. colapso < 90 min: {pd:.4f} ± {ic_d:.4f}")


resolver_ejercicio_11()
