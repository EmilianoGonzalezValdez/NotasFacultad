import random
import math


# --- 1. CONFIGURACIÓN DEL PROCESO DE ARRIBOS ---
def intensidad_lambda(t):
    return 7 - 1 / (t + 1)


def proximo_arribo(t_actual):
    """Algoritmo de Adelgazamiento (Thinning)"""
    t = t_actual
    lam_max = 7
    while True:
        t += -math.log(1 - random.random()) / lam_max
        if random.random() < intensidad_lambda(t) / lam_max:
            return t


# --- 2. MOTOR DE SIMULACIÓN (UNA CORRIDA) ---
# Adaptado para colas independientes según el enunciado
def simular_jornada_1000():
    t = n1 = n2 = ND = 0
    tA = proximo_arribo(0)
    t1 = t2 = math.inf

    # Registros para métricas
    cola_S1 = []  # Tiempos de arribo de clientes en S1
    cola_S2 = []  # Tiempos de arribo de clientes en S2
    tiempos_permanencia = []
    servicios_S1_en_la_corrida = 0

    # La simulación se detiene al completar 1000 servicios
    while ND < 1000:
        evento_proximo = min(tA, t1, t2)
        t = evento_proximo

        # --- CASO 1: ARRIBO ---
        if evento_proximo == tA:
            # Estrategia: Join the Shortest Queue
            if n1 <= n2:  # Prioridad S1 ante empate
                n1 += 1
                cola_S1.append(t)
                if n1 == 1:  # Servidor estaba libre
                    t1 = t - math.log(1 - random.random()) / 3  # Tasa mu=3
            else:
                n2 += 1
                cola_S2.append(t)
                if n2 == 1:
                    t2 = t - math.log(1 - random.random()) / 4  # Tasa mu=4
            tA = proximo_arribo(t)

        # --- CASO 2: FIN SERVICIO S1 ---
        elif evento_proximo == t1:
            ND += 1
            servicios_S1_en_la_corrida += 1
            # Permanencia = t_salida - t_arribo
            tiempos_permanencia.append(t - cola_S1.pop(0))
            n1 -= 1
            if n1 > 0:
                t1 = t - math.log(1 - random.random()) / 3
            else:
                t1 = math.inf

        # --- CASO 3: FIN SERVICIO S2 ---
        else:
            ND += 1
            tiempos_permanencia.append(t - cola_S2.pop(0))
            n2 -= 1
            if n2 > 0:
                t2 = t - math.log(1 - random.random()) / 4
            else:
                t2 = math.inf

    avg_permanencia = sum(tiempos_permanencia) / 1000
    return avg_permanencia, servicios_S1_en_la_corrida


def resolver_ejercicio_10():
    n = 0
    # Inicialización Inciso B (Media Permanencia, d < 0.01)
    mb = 0.0
    s2b = 0.0
    # Inicialización Inciso C (Servicios S1, d < 0.1)
    mc = 0.0
    s2c = 0.0

    while True:
        n += 1
        xb, xc = simular_jornada_1000()

        # --- Actualización Recursiva ---
        # Inciso B
        mb_ant = mb
        mb = mb_ant + (xb - mb_ant) / n
        if n > 1:
            s2b = s2b * (1 - 1 / (n - 1)) + n * (mb - mb_ant) ** 2

        # Inciso C
        mc_ant = mc
        mc = mc_ant + (xc - mc_ant) / n
        if n > 1:
            s2c = s2c * (1 - 1 / (n - 1)) + n * (mc - mc_ant) ** 2

        # --- Verificación de Criterio de Parada ---
        if n >= 100:
            err_b = math.sqrt(s2b / n)
            err_c = math.sqrt(s2c / n)

            if err_b < 0.01 and err_c < 0.1:
                break

    # --- Resultados Finales e Intervalos de Confianza (z = 1.64) ---
    print(f"Simulaciones totales: {n}")
    print(f"B) Permanencia media: {mb:.4f} ± {1.64 * math.sqrt(s2b / n):.4f} horas")
    print(f"C) Servicios en S1: {mc:.2f} ± {1.64 * math.sqrt(s2c / n):.2f}")


# Ejecución
resolver_ejercicio_10()
