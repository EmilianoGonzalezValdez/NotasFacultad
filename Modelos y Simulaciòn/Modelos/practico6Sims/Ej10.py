import math 
import random 


def intensidad(t):
    return 7 - 1 / (t + 1)

def proximo_arribo(t_actual):
    t = t_actual
    lam_max = 7
    while True:
        t += -math.log(1 - random.random()) / lam_max
        if random.random() < intensidad(t) / lam_max:
            return t

def simular_jornada_1000():
    t = n1 = n2 = ND = NA = 0
    tA = proximo_arribo(0)
    t1 = t2 = math.inf
    
    tiempos_llegada = {} # Diccionario para rastrear cada cliente
    permanencias = []
    servicios_S1 = 0 # Contador para inciso C
    
    while ND < 1000:
        evento = min(tA, t1, t2)
        t = evento
        
        if evento == tA: # Arribo
            NA += 1
            tiempos_llegada[NA] = t
            if n1 <= n2: # Elige S1
                n1 += 1
                if n1 == 1: t1 = t - math.log(1-random.random())/3
            else: # Elige S2
                n2 += 1
                if n2 == 1: t2 = t - math.log(1-random.random())/4
            tA = proximo_arribo(t)
            
        elif evento == t1: # Salida de S1
            ND += 1
            servicios_S1 += 1
            # El cliente que sale de S1 es el primero que entró a S1 (FIFO)
            # Para simplificar, usamos una lista/cola para cada servidor
            ... logic de tracking ...
            n1 -= 1
            t1 = t - math.log(1-random.random())/3 if n1 > 0 else math.inf
            
        elif evento == t2: # Salida de S2
            ND += 1
            ... logic de tracking ...
            n2 -= 1
            t2 = t - math.log(1-random.random())/4 if n2 > 0 else math.inf
            
    return sum(permanencias)/1000, servicios_S1
