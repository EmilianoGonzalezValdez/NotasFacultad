import random
import math


def generar_composicion_continua_ej4():
    # 1. Generar Y ~ Exp(1)
    Y = -math.log(random.random())
    # 2. Generar X dado Y usando F(x|y) = x^y (Transformada inversa: X = U^(1/Y))
    U = random.random()
    return U ** (1 / Y)
