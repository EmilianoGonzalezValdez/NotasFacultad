import random
import time
import math


def probabilidadX(j):
    return ((1 / 2) ** (j + 1)) + (((1 / 2) * (2 ** (j - 1))) / 3**j)


def transformadaInversaX():
    F = probabilidadX(0)
    U = random.random()
    i = 0
    while U >= F:
        i += 1
        F += probabilidadX(i)
    return i


def ejercicio10(Nism):
    suma = 0
    for _ in range(Nism):
        suma += transformadaInversaX()
    return suma / Nism


print(ejercicio10(10000))
