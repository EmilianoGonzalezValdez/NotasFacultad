## El pseudocodigo genera 2 variables aleatorias con distribucion geometrica
# con probabilidades p1 y p2 y retorna el minimo entre ellas.
# De esta forma como la distribucion geometrica representa la cantidad
# de sucesos hasta un acierto, su minimo me calculara el numero de simulaciones hasta
# el acierto de alguna de ambas. por lo cual tambien es geometrica su distribucion
# Ademas siendo 2 variables indeendientes tenemos que
# P(min(X,Y)>n)=P(Y>n) * P(X>n) = (1-p1)**n (1-p2)**n = [(1-p1)(1-p2)]**n
# Lo cual tambien es la funcion de probabilidad de la geometrica con un nuevo parametro
#


import random
import math


def simulacion_optimizada():
    p_total = 0.24
    U = random.random()
    return int(math.log(1 - U) / math.log(1 - p_total)) + 1
