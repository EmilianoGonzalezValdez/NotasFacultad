import random
import math
import time


def ejercicio1_a():
    U = random.random()
    if U < 0.24:
        return 0
    elif U < 0.33:
        return 1
    elif U < 0.64:
        return 2
    else:
        return 3


def ejercicio2_b():
    U = random.random()
    if U < 0.5:
        return 4 * U
    else:
        return 1 / U - 1


def generar_Y_geometrica(p):
    U = random.random()
    return int(math.log(1 - U) / math.log(1 - p)) + 1


def ejercicio_aceptacion_rechazo():
    p = 0.6
    prob_truncamiento = 1 - (1 - p) ** 20
    c = 1 / prob_truncamiento

    while True:
        # 1. Simular la variable de soporte Y ~ Geom(0.6) [2]
        Y = generar_Y_geometrica(p)

        # 2. Generar una uniforme U ~ U(0, 1) [2]
        U = random.random()

        # 3. Definir f(Y) y g(Y) para la condición [2]
        # g(Y) es la PMF de la Geométrica: p * (1-p)^(Y-1)
        g_Y = p * (1 - p) ** (Y - 1)

        # f(Y) es la PMF de la truncada [Conversación previa]
        if 1 <= Y <= 20:
            f_Y = g_Y / prob_truncamiento
        else:
            f_Y = 0  # Fuera del rango de X la probabilidad es nula

        # 4. Condición de aceptación: U < f(Y) / (c * g(Y)) [2]
        # Esta división se simplifica a 1 si 1 <= Y <= 20
        if U < f_Y / (c * g_Y):
            return Y


def generar_monto_exponencial(media):
    """
    Genera un valor de una distribución exponencial usando el
    Método de la Transformada Inversa: X = -media * ln(U) [2].
    """
    U = random.random()
    # Usamos 1 - U para evitar el logaritmo de 0,
    # aunque random() suele generar [0.0, 1.0)
    return -media * math.log(1 - U)


def simular_un_mes(n_clientes, p_reclamo, media_monto):
    """
    Simula el total de reclamos de una compañía en un mes.
    Identifica variables Bernoulli para cada cliente e indica el monto [3].
    """
    suma_reclamos = 0
    for _ in range(n_clientes):
        # Variable Bernoulli(p): El cliente hace un reclamo con prob p [4, 5]
        if random.random() < p_reclamo:
            # Si reclama, generamos el monto exponencial
            monto = generar_monto_exponencial(media_monto)
            suma_reclamos += monto
    return suma_reclamos


def ejercicio4():
    """
    Punto b: Implementación del método de Monte Carlo para estimar la probabilidad
    de que la suma exceda los $50,000 con 10,000 simulaciones [3].
    """
    N_simulaciones = 10000
    n_clientes = 1000
    p_reclamo = 0.05
    media_monto = 800
    umbral_critico = 50000

    exitos = 0

    for _ in range(N_simulaciones):
        total_mes = simular_un_mes(n_clientes, p_reclamo, media_monto)
        # Verificamos si la suma total excede el valor crítico
        if total_mes > umbral_critico:
            exitos += 1

    # La probabilidad estimada es la proporción de éxitos (Ley de los Grandes Números) [6, 7]
    probabilidad_estimada = exitos / N_simulaciones

    print(f"Probabilidad estimada (N={N_simulaciones}): {probabilidad_estimada:.4f}")
