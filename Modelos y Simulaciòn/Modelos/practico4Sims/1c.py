from random import random
from math import factorial

def EdeX(N):
    acum = 0
    for _ in range(N):
        acum2 = 0
        M = int(random() * 100) + 1
        for i in range(N-M):
            H = int(random() * 100) + 1
            acum2 += (-1)**H / factorial(H)
        acum += M * (1 / factorial(M)) * acum2
    return acum

print(f"Estimacion de E[X] con 100: {EdeX(100)}")
print(f"Estimacion de E[X] con 1000: {EdeX(1000)}")
print(f"Estimacion de E[X] con 10000: {EdeX(10000)}")
print(f"Estimacion de E[X] con 100000: {EdeX(100000)}")
