import random
import math
import time


def Bernoulli(p):
    U = random.random()
    if U < p:
        return 1
    else:
        return 0


def Binomial(n, p):
    c = p / (1 - p)
    prob = (1 - p) ** n
    F = prob
    i = 0
    U = random.random()
    while U >= F:
        prob *= c * (n - i) / (i + 1)
        F += p
        i += 1
    return i


def NBernoulli(n, p):
    suma = 0
    for _ in range(n):
        suma += Bernoulli(p)
    return suma


def ejercicio5(Nsim):
    valores = [0] * (10 + 1)
    inicioBin = time.time()
    for _ in range(Nsim):
        valores[Binomial(10, 0.3)] += 1
    finBin = time.time()

    inicioBer = time.time()
    for _ in range(Nsim):
        valores[NBernoulli(10, 0.3)] += 1
    finBer = time.time()

    return (
        (finBin - inicioBin),
        (finBer - inicioBer),
        valores.index(max(valores)),
        valores[10] / Nsim,
        valores[0] / Nsim,
    )


print(Binomial(10, 0.5))
print(Bernoulli(0.5))
print(NBernoulli(10, 0.5))
print(ejercicio5(10000))
