import random
import math


def varY():
    U = random.random()
    Impar = [1, 3, 5, 7, 9]
    Par = [2, 4, 6, 8, 10]
    if U < 0.2:
        return Impar[int(random.random() * 5) + 1]
    else:
        return Par[int(random.random() * 5) + 1]


def generar_exponencial(lamda):

    U = 1 - random.random()
    # Usamos 1 - U para evitar el logaritmo de 0,
    # aunque random() suele generar [0.0, 1.0)
    return -math.log(1 - U) / lamda


def rechazoX():
    while True:
        y = generar_exponencial(1)
        U = random.random()
        if U < (y**2) / math.exp(-y):
            return y


## No se si llego a terminarlo pero esta explicado en la hoja, creo que me olvide de los cambios de variable


def jugador(p, lamda):
    tiempo = 0
    contador = 0
    while True:
        U = random.random()
        tiempo += generar_exponencial(lamda)
        contador += 1
        if U >= p:
            return (contador, tiempo)


def promedioTiempo(Nsim):
    tiempo = 0
    contador3 = 0
    for _ in range(Nsim):
        player = jugador(0.4, 0.5)
        tiempo += player[1]
        if player[0] >= 3:
            contador3 += 1

        return (contador3 / Nsim, tiempo / Nsim)


print(promedioTiempo(10000))
print(jugador(0.4, 0.5))
