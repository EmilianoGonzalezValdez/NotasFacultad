import random

# Snippet de permutación aleatoria equiprobable (Sección 5.1.1, pág. 74)
def permutacion(a):
    N = len(a)
    for j in range(N-1, 0, -1):
        # Generación de una uniforme discreta para el índice (Sección 5.1.1)
        indice = int((j + 1) * random.random())
        a[j], a[indice] = a[indice], a[j]

def ejercicio1_c_montecarlo(N_sim):
    n = 100  # Número de cartas
    mazo_base = list(range(1, n + 1))
    
    # Acumuladores para el cálculo de promedios (Capítulo 4 y Sección 5.1.2)
    suma_x = 0   # Para estimar E[X]
    suma_x2 = 0  # Para estimar E[X^2]

    for _ in range(N_sim):
        # 1. Realizar el experimento: Barajar (Sección 5.1.1)
        mazo = mazo_base[:]
        permutacion(mazo)
        
        # 2. Contar coincidencias (X): éxito si mazo[j] == j+1 [5, 6]
        exitos = 0
        for j in range(n):
            if mazo[j] == j + 1:
                exitos += 1
        
        # 3. Acumular valores para Monte Carlo [2, 7]
        suma_x += exitos
        suma_x2 += exitos**2

    # 4. Cálculo de estimadores finales por promedio simple
    esperanza_estimada = suma_x / N_sim
    esperanza_x2_estimada = suma_x2 / N_sim
    
    # Varianza = E[X^2] - (E[X])^2 (Sección 1.2.5, pág. 18)
    varianza_estimada = esperanza_x2_estimada - (esperanza_estimada**2)
    
  return esperanza_estimada, varianza_estimada

# Ejecución para los distintos valores de N solicitados [8]
print(f"{'N':>8} | {'E[X] Estima':>12} | {'Var(X) Estima':>12}")
print("-" * 45)
for N in [9]:
    esp, var = ejercicio1_c_montecarlo(N)
    print(f"{N:8} | {esp:12.4f} | {var:12.4f}")
