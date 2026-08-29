import numpy as np
from scipy.stats import expon, uniform


def Ej9_Corregido():
    datos = [
        1.6,
        10.3,
        3.5,
        13.5,
        18.4,
        7.7,
        24.3,
        10.7,
        8.4,
        4.9,
        7.9,
        12.0,
        16.2,
        6.8,
        14.7,
    ]
    datos.sort()
    n = len(datos)

    # 1. ESTIMAR PARÁMETRO REAL
    media_obs = np.mean(datos)  # Da 11.0

    # 2. CALCULAR D OBSERVADO (Usando la media estimada)
    d_KS = 0
    for j in range(n):
        # scale = media (1/lambda)
        exp_j = expon.cdf(datos[j], scale=media_obs)
        dist_salto = (j + 1) / n - exp_j
        dist_base = exp_j - j / n
        d_KS = max(d_KS, dist_salto, dist_base)

    # 3. SIMULACIÓN "CERTERA" (Re-estimando en cada vuelta)
    Nsim = 10000
    exitos = 0
    for _ in range(Nsim):
        # Generamos una muestra Exponencial con la media que imaginamos
        muestra_sim = expon.rvs(scale=media_obs, size=n)
        muestra_sim.sort()

        # CLAVE: Re-estimamos la media para esta muestra sintética
        media_sim = np.mean(muestra_sim)

        d_sim = 0
        for j in range(n):
            f_sim = expon.cdf(muestra_sim[j], scale=media_sim)
            d_sim = max(d_sim, (j + 1) / n - f_sim, f_sim - j / n)

        if d_sim >= d_KS:
            exitos += 1

    p_valor_final = exitos / Nsim
    print(f"D observado: {d_KS:.4f}")
    print(f"p-valor simulado: {p_valor_final:.4f}")


Ej9_Corregido()
