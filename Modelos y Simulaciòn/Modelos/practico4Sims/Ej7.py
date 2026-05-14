import random
import math
import time


def poisson(tasa):
    U = random.random()
    i = 0
    p = math.exp(-tasa)
    F = p
    while U >= F:
        i += 1
        p *= tasa / i
        F += p
    return i


def poissonMejor(tasa):
    p = math.exp(-tasa)
    F = p
    for j in range(1, int(tasa) + 1):
        p *= tasa / j
        F += p
    U = random.random()
    if U >= F:
        j = int(tasa) + 1
        while U >= F:
            p *= tasa / j
            F += p
            j += 1
        return j - 1
    else:
        j = int(tasa)
        while U < F:
            F -= p
            p *= j / tasa
            j -= 1
        return j + 1


def ejercicio7(Nsim):
    suma1 = 0
    suma2 = 0
    for _ in range(Nsim):
        prob_poisson1 = poisson(10)
        prob_posisson2 = poissonMejor(10)

        if prob_poisson1 > 2:
            suma1 += 1
        if prob_posisson2 > 2:
            suma2 += 1

    return suma1 / Nsim, suma2 / Nsim


print(ejercicio7(1000))
