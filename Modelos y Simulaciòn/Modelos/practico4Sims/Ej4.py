import random
import math
import time


def simY(n):
	Y = random.random()
	return int((Y * n) + 1)


def simularX():
	p = [0.11,0.14,0.09,0.08,0.12,0.1,0.09,0.07,0.11,0.09]
	cota =  0.14*10 
	while True:
		Y = simY(10)
		U = random.random()
		if (U < p[Y-1]/ 0.14):
			return Y

def simularX_b():
	p = [0.11,0.14,0.09,0.08,0.12,0.1,0.09,0.07,0.11,0.09]
	cota =  3 
	while True:
		Y = simY(10)
		U = random.random()
		if (U < p[Y-1]/ (3 * 0.1)):
			return Y
def ejercicio4a(Nsim):
	inicio = time.time()

	for _ in range (Nsim):
		valorX = simularX()

	return time.time() - inicio

def ejercicio4b(Nsim):
	inicio = time.time()

	for _ in range (Nsim):
		valorX = simularX_b()

	return time.time() - inicio

def ejercicio4c(Nsim):
	p = [0.11,0.14,0.09,0.08,0.12,0.1,0.09,0.07,0.11,0.09]
	inicio = time.time()
	for _ in range(Nsim):
		U = random.random()
		i,F = 0,p[0]
		while U >= F:
			i +=1; F += p[i]
		
	return time.time() - inicio

def ejercicio4d(Nsim):
	p = [0.11,0.14,0.09,0.08,0.12,0.1,0.09,0.07,0.11,0.09]
	A = []
	inicio = time.time()
	for _ in range(Nsim):
		for i in range(len(p)):
			valor = i+1
			cantidad = int(p[i]*100)
			A.extend([valor]*cantidad)

		indice = int(random.random()*100)
		return time.time() - inicio

print("TIEMPO TOTAL:")
print(ejercicio4a(10000))
print(ejercicio4b(10000))
print(ejercicio4c(10000))
print(ejercicio4d(10000))



