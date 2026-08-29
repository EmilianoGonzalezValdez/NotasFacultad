import math
import random


def ejercicio_3_simulacion():
    d_obs = 0.24  # Calculado arriba
    n = 10
    n_sim = 10000
    exitos = 0
    for _ in range(n_sim):
        u = []
        # Generamos muestra de U(0,1) y ordenamos
        for i in range(n):
            u.append(random.random())
        u.sort()

        # Calculamos el estadístico D para esta simulación
        d_sim = 0
        for j in range(1, n + 1):
            dist_salto = j / n - u[j - 1]
            dist_base = u[j - 1] - (j - 1) / n
            d_sim = max(d_sim, dist_salto, dist_base)

        if d_sim >= d_obs:
            exitos += 1

    print(f"p-valor estimado: {exitos / n_sim}")


ejercicio_3_simulacion()
