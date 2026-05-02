import random
import math
import time

def Bernoulli(p):
	U = random.random()
	if U < p:
		return 1
	else:
		return 0

def Binomial(n,p):
	c = p/(1-p)
	prob = (1-p)**n
	F = prob; i = 0
	U = random.random()
	while U >= F:
		prob *= c * (n-i) / (i+1)
		F += p
		i += 1





	suma = 0
	for _ in range(n):
		suma += Bernoulli(p)
	return suma



def ejercicio5(Nsim):
	inicioBin = time.time()
	for _ in range(Nsim):
		Binomial(10,0.3)
	finBin = time.time()

	inicioBer = time.time()
	for _ in range(Nsim):
		NBernoulli(10,0.3)
	finBer = time.time()
		
	return (finBin - inicioBin), (finBer - inicioBer)

print(Binomial(10,0.5))
print(Bernoulli(0.5))
prit(NBernoulli(10,0.5))
