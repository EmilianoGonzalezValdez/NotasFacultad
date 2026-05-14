import random
import math


def ej7_transformada_inversa():
    U = random.random()
    return math.exp(U)  # x = e^U


def ej7_aceptacion_rechazo_unif():
    c = math.e - 1
    while True:
        Y = 1 + (c) * random.random()  # Soporte Uniforme(1, e)
        U = random.random()
        if U < 1 / Y:  # Condición: U < (1/Y) / (c * (1/(e-1))) = 1/Y
            return Y
