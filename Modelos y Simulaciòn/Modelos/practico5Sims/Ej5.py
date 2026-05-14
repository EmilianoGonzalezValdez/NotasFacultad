import random
import math


def generar_M_y_m_ej5():
    # Generar las tres variables independientes
    x1 = -math.log(random.random()) / 1
    x2 = -math.log(random.random()) / 2
    x3 = -math.log(random.random()) / 3

    M = max(x1, x2, x3)
    m = min(x1, x2, x3)
    return M, m
