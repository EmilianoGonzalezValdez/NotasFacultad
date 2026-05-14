import random
import math


def generar_composicion_ej3():
    U = random.random()
    # Selector de índices (p = 0.5, 0.3, 0.2)
    if U < 0.5:
        return -3 * math.log(random.random())  # Exp media 3
    elif U < 0.8:
        return -5 * math.log(random.random())  # Exp media 5
    else:
        return -7 * math.log(random.random())  # Exp media 7
