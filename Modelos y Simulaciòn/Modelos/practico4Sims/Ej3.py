import random
import math

def simular_N_lanzamientos():
	# Simula una relación del experimento: lanzar un par de datos hasta que salgan todas las sumas del 2 al 12

	sumas_vistas = set()
	lanzamientos = 0

	while len(sumas_vistas) < 11: #Hay 11 sumas posibles: (2, 3, ..., 12)
		lanzamientos += 1
		#Generación de variables aleatorias uniformes discretas 
		dado1 = int(random.random() * 6) + 1
		dado2 = int(random.random() * 6) + 1
		suma = dado1 + dado2
		sumas_vistas.add(suma)



	return lanzamientos


def realizar_estimación(Nsim):

	suma_N = 0
	suma_N_cuad = 0
	cont_15 = 0
	cont_9 = 0

	for _ in range(Nsim):
		n_obtenido = simular_N_lanzamientos()

		suma_N += n_obtenido
		suma_N_cuad += n_obtenido**2

		if n_obtenido >= 15:
			cont_15 +=1
		if n_obtenido <= 9:
			cont_9 += 1


	esperanza = suma_N / Nsim
	esperanza_cuad = suma_N_cuad / Nsim
	varianza = esperanza_cuad - esperanza**2
	desvio_estandar = math.sqrt(varianza)

	prob_15 = cont_15/Nsim
	prob_9 = cont_9/Nsim


	return esperanza, desvio_estandar, prob_15, prob_9


valores_N = [100,1000,10000,100000,1000000]


print(f"{'N_sim':>8} | {'Media':>8} | {'Desvío':>8} | {'P(N >= 15)':>11} | {'P(N <= 9)':>11}")
print("-" * 58)

for n in valores_N:
    media, desvio, p15, p9 = realizar_estimación(n)
    print(f"{n:8} | {media:8.2f} | {desvio:8.2f} | {p15:11.4f} | {p9:11.4f}")




