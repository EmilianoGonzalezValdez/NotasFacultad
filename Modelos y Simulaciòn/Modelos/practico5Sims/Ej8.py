import random
import math


def ej8_suma_uniformes():
    return random.random() + random.random()


def ej8_transformada_inversa():
    U = random.random()
    if U < 0.5:
        return math.sqrt(2 * U)
    else:
        return 2 - math.sqrt(2 * (1 - U))


def ej8_aceptacion_rechazo():
    while True:
        Y = 2 * random.random()  # Soporte Uniforme(0, 2)
        U = random.random()
        # f(y) es la densidad triangular
        f_y = Y if Y < 1 else 2 - Y
        if U < f_y:  # Condición: U < f(Y)/(2 * 0.5) = f(Y)
            return Y
