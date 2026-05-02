import random
import math

N = 10000
Nsim = 100 # Solo porque lo dice el inciso b
Suma = 0

for _ in range (Nsim):
	# Generar un índice aleatorio entre 1 y 10000
	U = int(random.random() * N) + 1
	# Aplicamos la funcion del ejercicio tomando como g(x) a exp(U/N)
	Suma += math.exp(U/N)

# Hasta ahora solo tenemos la suma total, ahora debemos sacarle el promedio y multiplicar por Nsim
resultado_estimado = (Suma/Nsim) * N
print(resultado_estimado)
