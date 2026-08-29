import math
import random


def fx(x):
    return 30 * (x**2) * ((1 - x) ** 2)


def variableX_rechazo():
    while True:
        Y = random.random()
        if random.random() < fx(Y) / 7.6:
            return Y, 7.6


def estimar_Ex():
    media, _ = variableX_rechazo()
    x_menor_a_4 = 0
    for n in range(5000):
        x, y = variableX_rechazo()
        media += x
        if x < 0.4:
            x_menor_a_4 += 1
    return media / 5000, x_menor_a_4 / 5000


def area(N):
    bajoCUrva = 0.0
    for _ in range(N):
        x = 10 * random.random() - 5
        y = 8 * random.random() - 4
        if (x**2) / 2 + y**2 < 10 and abs(x) + abs(y) > 3:
            bajoCUrva += 1
    return bajoCUrva / N


print(f"--------------Ejercicio 2-----------\t")
print(
    f"El valor generado de X y la cantidad de iteraciones para hacerlo son: {variableX_rechazo()}"
)
print(f"valor de la media, P(x<4) son: {estimar_Ex()}")
print(f"--------------Ejercicio 4-----------\t")

print(f"Estimacion del area bajo la curva: {area(100000):.6f}")
