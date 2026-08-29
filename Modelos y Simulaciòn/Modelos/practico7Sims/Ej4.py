import math
import random


# 1. Definimos la FUNCIÓN de probabilidad acumulada (CDF)
# Esta es la que "funcion_F" usará adentro de calcular_D
def F_exponencial_teorica(x):
    lamda = 1 / 50.0  # Media 50 -> lamda = 1/50 [1, 5]
    return 1 - math.exp(-lamda * x)


def calcular_D(datos, funcion_F):
    n = len(datos)
    datos_ordenados = sorted(datos)
    d_max = 0
    for j in range(1, n + 1):
        y_j = datos_ordenados[j - 1]

        # Evaluamos el dato en la fórmula teórica
        f_teorica = funcion_F(y_j)

        dist_salto = j / n - f_teorica
        dist_base = f_teorica - (j - 1) / n
        d_max = max(d_max, dist_salto, dist_base)
    return d_max


def ejercicio4_resolucion():
    datos_reales = [
        86.0,
        133.0,
        75.0,
        22.0,
        11.0,
        144.0,
        78.0,
        122.0,
        8.0,
        146.0,
        33.0,
        41.0,
        99.0,
    ]

    # CALCULAMOS EL D OBSERVADO (La distancia real)
    # Pasamos la función por su NOMBRE, sin los paréntesis ()
    d_obs = calcular_D(datos_reales, F_exponencial_teorica)

    # SIMULACIÓN DEL P-VALOR
    # Por el Teorema 8.1, como el parámetro está fijo, la distribución de D
    # es independiente de F. Podemos simular con Uniformes(0,1) [6, 7].
    n = 13
    n_sim = 10000
    exitos = 0

    for _ in range(n_sim):
        # Generamos muestra de Uniformes (mundo ideal de H0)
        u = [random.random() for _ in range(n)]
        u.sort()

        d_sim = 0
        for j in range(1, n + 1):
            # Para una U(0,1), la CDF es F(x) = x.
            # Por eso restamos directamente u[j-1]
            dist_salto = j / n - u[j - 1]
            dist_base = u[j - 1] - (j - 1) / n
            d_sim = max(d_sim, dist_salto, dist_base)

        if d_sim >= d_obs:
            exitos += 1

    print(f"Estadístico D observado: {d_obs:.4f}")
    print(f"p-valor estimado: {exitos / n_sim:.4f}")


ejercicio4_resolucion()
