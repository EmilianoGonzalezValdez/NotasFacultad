import random
import math
import time


def generadorProbaPoisson(k, lamda):
    return math.exp(-lamda) * (lamda**k) / math.factorial(k)


def generadorPoisson(lamda):
    U = random.random()
    i = 0
    p = math.exp(-lamda)
    F = p
    while U >= F:
        i += 1
        p *= lamda / i
        F += p
    return i


def transformadaInversa(lamda, k):
    C = sum(generadorPoisson(j, lamda) for j in range(k + 1))
    U = random.random()
    i = 0
    p = math.exp(-lamda) / C
    F = p

    while U >= F and i < k:
        i += 1
        p *= lamda / i
        F += p
    return i


def rechazo(lamda, k):
    Y = generadorPoisson(lamda)
    if Y <= k:
        return Y


def ejercicio8b(Nsim, lamda, k):
    exitos = 0

    for _ in range(Nsim):
        X = rechazo(lamda, k)
        if X > 2:
            exitos += 1

    return exitos / Nsim


print(ejercicio8b(10000, 0.7, 10))
