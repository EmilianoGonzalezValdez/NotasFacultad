import math
import random
import time


def generarBinY(n, p):
    c = p / (1 - p)
    prob = (1 - p) ** n
    F = prob
    i = 0
    U = random.random()
    while U >= F:
        prob *= c * (n - i) / (i + 1)
        F += prob
        i += 1
    return i


def probabilidadY(n, p):
    prob_y = [0] * (n + 1)
    for j in range(n + 1):
        prob_y[j] = math.comb(n, j) * (p**j) * ((1 - p) ** (n - j))
    return prob_y


def transformadaInversa():
    U = random.random()
    if U < 0.35:
        return 3
    elif U < 0.55:
        return 1
    elif U < 0.75:
        return 4
    elif U < 0.9:
        return 0
    else:
        return 2


def aceptacion_rechazo(p, q, c):
    Y = generarBinY(4, 0.45)
    U = random.random()

    if U < p[Y] / (c * q[Y]):
        return Y


def ejercicio6(Nsim):
    prob_x = [0.15, 0.2, 0.1, 0.35, 0.2]
    prob_y = probabilidadY(4, 0.45)
    temp_array = [0] * (len(prob_x))
    for j in range(len(prob_x)):
        temp_array[j] = prob_x[j] / prob_y[j]
    c = max(temp_array)

    inicio1 = time.time()
    for _ in range(Nsim):
        transformadaInversa()
    fin1 = time.time()

    inicio2 = time.time()
    for _ in range(Nsim):
        aceptacion_rechazo(prob_x, prob_y, c)
    fin2 = time.time()

    return (fin1 - inicio1), (fin2 - inicio2)


print(ejercicio6(10000))
