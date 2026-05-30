import random
import math


def ejercicio5():
    valoresORG = [56, 101, 78, 67, 93, 87, 64, 72, 80, 69]
    mediaORG = 0
    n = 0
    count = 0
    for x in valoresORG:
        mediaORG += x
    while n < 100000:
        n += 1
        newMuestra = random.choices(valoresORG, k=10)
        media = 0
        for x in newMuestra:
            media += x
        if media / 10 - mediaORG / 10 < 5 and media / 10 - mediaORG / 10 > -5:
            count += 1
    return count / n


print(ejercicio5())
