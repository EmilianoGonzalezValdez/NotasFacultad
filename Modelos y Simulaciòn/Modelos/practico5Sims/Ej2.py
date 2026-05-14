import random
import math


def generar_pareto(a):
    U = random.random()
    return U ** (-1 / a)


def generar_earlang(k, mu):
    producto_u = 1.0
    for _ in range(k):
        producto_u *= random.random()
    return -mu * math.log(producto_u)


def generar_weibull(lamda, beta):
    U = random.random()
    return lamda * (-math.log(U)) ** (1 / beta)
