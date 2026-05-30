import random
import math


def varianza_muestral(muestra):
    n = len(muestra)
    if n < 2:
        return 0
    media = sum(muestra) / n
    suma_cuadrados = sum((x - media) ** 2 for x in muestra)
    return suma_cuadrados / (n - 1)


def ejercicio6A_ideal():
    datos_originales = [1, 3]
    n = len(datos_originales)

    replicaciones_S2 = []

    for x1 in datos_originales:
        for x2 in datos_originales:
            muestra_bootstrap = [x1, x2]

            valor_S2 = varianza_muestral(muestra_bootstrap)
            replicaciones_S2.append(valor_S2)

    print("Replicaciones bootstrap del estimador S^2:", replicaciones_S2)

    media_de_replicaciones = sum(replicaciones_S2) / len(replicaciones_S2)
    varianza_bootstrap = sum(
        (r - media_de_replicaciones) ** 2 for r in replicaciones_S2
    ) / len(replicaciones_S2)

    return varianza_bootstrap


def ejercicio6B():
    datos_originales = [5, 4, 9, 6, 21, 17, 11, 20, 7, 10, 21, 15, 13, 16, 8]
    n = len(datos_originales)
    varianzas_muestrales = []

    for i in range(10000):
        muestra = random.choices(datos_originales, k=n)
        varianza = varianza_muestral(muestra)
        varianzas_muestrales.append(varianza)
    media_Estimador = sum(varianzas_muestrales) / (10000)
    varianza_bootstrap = sum(
        (var - media_Estimador) ** 2 for var in varianzas_muestrales
    ) / (10000 - 1)
    return varianza_bootstrap


resultadoA = ejercicio6A_ideal()
print("Estimación Bootstrap Ideal de Var(S²):", resultadoA)
resultadoB = ejercicio6B()
print("Estimación Bootstrap con montecarlo: ", resultadoB)
