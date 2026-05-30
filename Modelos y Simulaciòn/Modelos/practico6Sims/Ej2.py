import random
import math


def funcion_i(x):
    return math.exp(x) / math.sqrt(2 * x)


def ejercicio_2(fun, n_min, d):
    media = fun(random.random())
    Scuad = 0
    n = 1
    while (
        n < n_min or math.sqrt(Scuad / n) > d
    ):  # mientras no se cumpla alguna de las condiciones mencionadas
        n = n + 1
        x = fun(random.random())  # Simular X --> genero un valor de la función
        media_ant = media
        media = media_ant + (x - media_ant) / n
        Scuad = Scuad * (1 - 1 / (n - 1)) + n * (media - media_ant) ** 2
    return media, Scuad, n


def g(x):
    return 2 * (x**2) * math.exp(-(x**2))


def h(x):
    x_val = (1 / x) - 1
    return g(x_val) * (1 / (x**2))


def ejercicio_2_b(h, n_min, d):
    media = h(random.random())
    scuad = 0
    n = 1
    while n < n_min or math.sqrt(scuad / n) > d:
        n += 1
        x = h(random.random())
        media_ant = media
        media = media_ant + (x - media_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (media - media_ant) ** 2
    return media, scuad, n


n_min = 100
d = 0.01
media, Scuad, n = ejercicio_2(funcion_i, n_min, d)

print("Valor real: ", 2.0685)
print("Estimación integral:", media)
print("Desviación estándar muestral: ", math.sqrt(Scuad / n))
print("Cantidad de datos generados: ", n)


media, Scuad, n = ejercicio_2_b(h, n_min, d)

print("Valor real: ", 2.0685)
print("Estimación integral:", media)
print("Desviación estándar muestral: ", math.sqrt(Scuad / n))
print("Cantidad de datos generados: ", n)
