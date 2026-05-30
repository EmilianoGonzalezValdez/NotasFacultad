import math
import random


def simularnormal():
    while True:
        Y1 = -math.log(1 - random.random())
        Y2 = -math.log(1 - random.random())
        if Y2 >= (Y1 - 1) ** 2 / 2:
            if random.random() < 0.5:
                return Y1 * 1 + 0
            return -Y1 * 1 + 0


def ejercicio1(n_min, d):
    x = simularnormal()
    media = simularnormal()
    scuad = 0
    datosesperados = 0
    n = 1
    while n < n_min or math.sqrt(scuad / n) > d:
        n += 1
        x = simularnormal()
        media_ant = media
        media = media_ant + (x - media_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (media - media_ant) ** 2
        datosesperados += n
    return datosesperados / n, n, media, scuad


n_min = 100
d = 0.1

datosesperados, n, media, scuad = ejercicio1(n_min, d)

print("Datos esperados: ", datosesperados)
print("Cantidad de datos generados: ", n)
print("Estimación integral:", media)
print("Desviación estándar muestral: ", math.sqrt(scuad / n))
