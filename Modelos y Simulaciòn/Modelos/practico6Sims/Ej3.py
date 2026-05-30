import random
import math
from scipy import stats


def calculo_z(alpha):
    return stats.norm.ppf(1 - alpha / 2)


def g(x):
    return math.sin(x) / x


def g2(x):
    return 3 / (3 + x**4)


def fun(x):
    return g(math.pi + ((2 * math.pi) - (math.pi)) * x) * ((math.pi * 2) - (math.pi))


def fun2(x):
    return 1 / x**2 * g2(1 / x - 1)


def snapshot(media, scuad, n, s):
    print("-----------------------------------")
    print("Estimación integral:", media)
    print("Estimación varianza del estimador:", s)
    print("Semi-ancho IC: ", stats.norm.ppf(1 - alpha / 2) * math.sqrt(scuad / n))
    print("Cantidad de datos generados N_s: ", n)
    print("-----------------------------------")


def ejercicio3_a(fun, n_min, alpha, L):
    z_alpha2 = calculo_z(alpha)
    d = L / (2 * z_alpha2)
    media = fun(random.random())
    scuad = 0
    n = 1
    while n < n_min or math.sqrt(scuad / n) > d:
        n += 1
        if n == 1000 or n == 5000 or n == 7000:
            snapshot(media, scuad, n, math.sqrt(scuad))
        x = fun(random.random())
        media_ant = media
        media = media_ant + (x - media_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (media - media_ant) ** 2

    return media, scuad, n, math.sqrt(scuad)


def ejercicio3_b(fun, n_min, alpha, L):
    z_alpha2 = calculo_z(alpha)
    d = L / (2 * z_alpha2)
    media = fun(random.random())
    n = 1
    scuad = 0
    while n < n_min or math.sqrt(scuad / n) > d:
        n += 1
        if n == 1000 or n == 5000 or n == 7000:
            snapshot(media, scuad, n, math.sqrt(scuad))
        x = fun(random.random())
        media_ant = media
        media = media_ant + (x - media_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (media - media_ant) ** 2
    return media, scuad, n, math.sqrt(scuad)


n_min = 100
alpha = 0.05
L = 2 * 0.001
media, scuad, n, s = ejercicio3_a(fun, n_min, alpha, L)

print("Estimación integral:", media)
print("Estimación varianza del estimador:", s)
print("Semi-ancho IC: ", stats.norm.ppf(1 - alpha / 2) * math.sqrt(scuad / n))
print("Cantidad de datos generados N_s: ", n)

print("----------------------------------------")
print("----------------------------------------")
print("----------------------------------------")
print("----------------------------------------")


media, scuad, n, s = ejercicio3_b(fun2, n_min, alpha, L)

print("Estimación integral:", media)
print("Estimación varianza del estimador:", s)
print("Semi-ancho IC: ", stats.norm.ppf(1 - alpha / 2) * math.sqrt(scuad / n))
print("Cantidad de datos generados N_s: ", n)
