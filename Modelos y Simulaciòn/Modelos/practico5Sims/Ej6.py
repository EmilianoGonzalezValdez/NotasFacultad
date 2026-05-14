import random
import math


def ej6_transformada_inversa(n):
    return random.random() ** (1 / n)


def ej6_aceptacion_rechazo(n):
    while True:
        Y = random.random()  # Soporte Uniforme(0,1)
        U = random.random()
        if U < Y ** (n - 1):  # Condición simplificada: U < (n*Y^(n-1))/(n*1)
            return Y


def ej6_maximo_uniformes(n):
    # Basado en Ejercicio 5: el máximo de n uniformes tiene acum. x^n
    maximo = 0
    for _ in range(n):
        maximo = max(maximo, random.random())
    return maximo
