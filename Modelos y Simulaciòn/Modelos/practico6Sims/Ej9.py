import random
import math


# --- GENERACIÓN DE ARRIBOS (THINNING) ---
def intensidad_lambda(t):
    t_rel = t % 8
    if t_rel < 4:
        return 4 + 2.5 * t_rel
    else:
        return 14 - 2.5 * (t_rel - 4)


def proximo_arribo(t_actual):
    t = t_actual
    lam_max = 14
    while True:
        t += -math.log(1 - random.random()) / lam_max
        if t > 16:
            return math.inf  # No entran pacientes tras las 16hs
        if random.random() < intensidad_lambda(t) / lam_max:
            return t


# --- MOTOR DE UNA JORNADA (UNA CORRIDA) ---


def simular_jornada():
    t = n1 = n2 = 0
    tA = proximo_arribo(0)
    t1 = t2 = math.inf

    # Registros para métricas b, c y d
    tiempos_llegada = []
    permanencias = []
    quedaron_a_las_16 = 0
    t_final_atencion = 0

    while tA < math.inf or n1 > 0 or n2 > 0:
        evento_proximo = min(tA, t1, t2)
        t = evento_proximo

        # CASO 1: tA es el mínimo (Arribo a S1)
        if evento_proximo == tA:
            n1 += 1
            tiempos_llegada.append(t)
            if n1 == 1:
                t1 = t - math.log(1 - random.random()) / 15  # Tasa 15
            tA = proximo_arribo(t)

        # CASO 2: t1 es el mínimo (Salida S1 -> Entrada S2)
        elif evento_proximo == t1:
            n1 -= 1
            if n1 > 0:
                t1 = t - math.log(1 - random.random()) / 15
            else:
                t1 = math.inf

            n2 += 1
            if n2 == 1:
                t2 = t - math.log(1 - random.random()) / 12  # Tasa 12

        # CASO 3: t2 es el mínimo (Salida total del sistema)
        elif evento_proximo == t2:
            n2 -= 1
            permanencias.append(t - tiempos_llegada.pop(0))
            if n2 > 0:
                t2 = t - math.log(1 - random.random()) / 12
            else:
                t2 = math.inf

        # Registro para inciso C y D
        if t <= 16 and (n1 + n2 > 0):
            quedaron_a_las_16 = 1
        t_final_atencion = t

    media_perm = sum(permanencias) / len(permanencias) if permanencias else 0
    tiempo_extra = max(0, t_final_atencion - 16)
    return media_perm, quedaron_a_las_16, tiempo_extra


def resolver_ejercicio_9():
    n = 0
    # Inicialización para Inciso B (Media Permanencia)
    mb = 0.0
    s2b = 0.0
    # Inicialización para Inciso C (Proporción Bernoulli)
    pc = 0.0
    # Inicialización para Inciso D (Media Tiempo Extra)
    md = 0.0
    s2d = 0.0

    while True:
        n += 1
        xb, xc, xd = simular_jornada()

        # --- Actualización Recursiva ---
        # Inciso B
        mb_ant = mb
        mb = mb_ant + (xb - mb_ant) / n
        if n > 1:
            s2b = s2b * (1 - 1 / (n - 1)) + n * (mb - mb_ant) ** 2

        # Inciso C (Simplificado para Bernoulli)
        pc = pc + (xc - pc) / n

        # Inciso D
        md_ant = md
        md = md_ant + (xd - md_ant) / n
        if n > 1:
            s2d = s2d * (1 - 1 / (n - 1)) + n * (md - md_ant) ** 2

        # --- Verificación de Criterios de Parada ---
        if n >= 100:
            err_b = math.sqrt(s2b / n)
            err_c = math.sqrt(pc * (1 - pc) / n)  # Desvío proporción
            err_d = math.sqrt(s2d / n)

            if err_b < 0.01 and err_c < 0.005 and err_d < 0.01:
                break

    # --- Resultados Finales con Intervalos de Confianza (z=1.96 para 95%) ---
    print(f"Simulaciones totales: {n}")
    print(f"B) Permanencia: {mb:.4f} ± {1.96 * math.sqrt(s2b / n):.4f} horas")
    print(
        f"C) Prob. pacientes al cierre: {pc:.4f} ± {1.96 * math.sqrt(pc * (1 - pc) / n):.4f}"
    )
    print(
        f"D) Tiempo adicional: {md * 60:.2f} ± {1.96 * math.sqrt(s2d / n) * 60:.2f} minutos"
    )


resolver_ejercicio_9()
