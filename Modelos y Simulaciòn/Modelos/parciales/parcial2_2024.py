import random
import math
import time


def algo_x(p):
    while True:
        U = random.random()
        Y = int(random.random() * 4)
        # el max c que me sirve para f(y) / g(y) es c = 1.4
        if U < p[Y] / (1.4 * 1 / 4):
            return Y


def ejercicio2():
    U = random.random()
    if U < 2 / 3:
        return ((3 * U) / 2) ** (3 / 2)
    else:
        return (3 * U) - 1


def area(N):
    hits = 0
    area_rectangulo = 9

    for _ in range(N):
        x = random.random() * 3 - 1.5
        y = random.random() * 3 - 1.5

        if x**2 + (y - abs(x) ** 1.5) ** 2 <= 1:
            hits += 1
    estimacion = (hits / N) * area_rectangulo
    return estimacion


N_sim = 10000
resultado = area(N_sim)
print(resultado)
