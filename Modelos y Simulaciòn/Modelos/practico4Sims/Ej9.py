import random
import time
import math


def geometrica(p):
    U = random.random()
    return int(math.log(1 - U) / math.log(1 - p)) + 1


def geomtricaAmano(p):
    ensayos = 1
    while True:
        U = random.random()
        if U < p:
            return ensayos
        ensayos += 1


def ejercicio9(Nsim, p):
    promedioGem = 0
    promedioMano = 0
    inicio1 = time.time()
    for _ in range(Nsim):
        promedioGem += geometrica(p)
    fin1 = time.time()

    inicio2 = time.time()
    for _ in range(Nsim):
        promedioMano += geomtricaAmano(p)
    fin2 = time.time()

    return (
        (inicio1 - fin1),
        (inicio2 - fin2),
        (promedioMano / Nsim),
        (promedioGem / Nsim),
        (1 / p),
    )


print(geomtricaAmano(0.1))
print(ejercicio9(10000, 0.2))
print(ejercicio9(10000, 0.8))
