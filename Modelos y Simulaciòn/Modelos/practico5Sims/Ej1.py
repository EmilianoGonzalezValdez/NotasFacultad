import random
import math


def simular_ej1a():
    U = random.random()
    if U < 0.25:
        return 2 + 2 * math.sqrt(U)
    else:
        return 6 - math.sqrt(12 * (1 - U))


def simular_ej1b():
    U = random.random()
    if U < 21 / 35:
        return -3 + math.sqrt(9 + 35 / 3 * U)
    else:
        return math.cbrt((16 - 35 * (1 - U)) / 2)


def simular_ej1c():
    U = random.random()
    if U <= 0.0625:
        return math.log(16 * U) / 4
    else:
        return 4 * U - 0.25


def Ej1():
    n = 10000
    esp = 0
    esp2 = 0
    esp3 = 0
    for _ in range(n):
        esp += simular_ej1a()
        esp2 += simular_ej1b()
        esp3 += simular_ej1c()
    esp /= n
    esp2 /= n
    esp3 /= n

    print(f"Media estimada: {esp:.4f}")
    print(f"Media teórica:  {11 / 3:.4f}")
    print(f"Media estimada: {esp2:.4f}")
    print(f"Media estimada: {esp3:.4f}")


Ej1()
