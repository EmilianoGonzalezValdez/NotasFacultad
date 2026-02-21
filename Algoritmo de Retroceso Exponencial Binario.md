**Objetivo:** Comprender el algoritmo que determina en Ethernet el tiempo de espera del emisor cuando ocurre una colisión.

Para ello vamos a suponer que tras una colisión el tiempo se divide en *ranuras* cuya longitud es igual al tiempo de propagación de ida y vuelta en el peor caso en el cable (2*t). El tiempo de ranura es 512 tiempos de bit o 5,12 useg

La idea es que cuando ocurre una colisión las estaciones afectadas por la colisión eligen cada una aleatoriamente una cierta cantidad de ranuras a esperar

Si S es un conjunto formado por estaciones que colisionaron entre si, puede suceder que ocurran múltiples colisiones consecutivas de estaciones de S.
Para el manejo de colisiones consecutivas de estaciones de S hay dos opciones:
1. que el intervalo donde se elige aleatoriamente (una cantidad de ranuras a esperar) sea fijo
2. que el intervalo donde se elige aleatoriamente sea de tamaño variable (es decir que el tamaño cambie con cada nueva colisión de estaciones de S)

Permitir que el intervalo sea de tamaño variable tiene una gran **ventaja:**
- Se puede acelerar la resolución de la colisión inicial de las estaciones de S.

Para acelerar la resolución de la colisión de las estaciones de S:
- Con cada nueva colisión de estaciones de S se puede agrandar el intervalo donde se elige aleatoriamente
- Esta es la idea del algoritmo de retroceso exponencial binario

*Algoritmo de retroceso exponencial binario:*
- Tras la primera colisión cada estación espera de 0 a 1 tiempos de ranura antes de intentarlo de nuevo. Si dos estaciones entran en colisión, y ambas escogen el mismo npumero aleatorio, habrá una nueva colisión
- Después de la segunda colisión cada una escoge 0, 1, 2 o 3 al azar y espera ese npumero de tiempos de ranura
- Si ocurre una tercera colisión, entonces para la siguiente vez el npumero de ranuras a esperar se escogerá al azar en el intervalo 0 a 7
- Tras i colisiones se escoge un npumero aleatorio entre 0 y $\exp(2,i)-1$ y se sata ese número de ranuras
- Tras haberse alcanzado 10 colisiones el intervalo de aleatorización se congela en un máximo de 1023 ranuras
- Tras 16 colisiones el controlador tira la toalla y avisa de un fracaso a la computadora. La recuperación posterior es responsabilidad de las capas superiores.

**Evaluación:**
- El algoritmo asegura un retardo pequeño cuando unas cuantas estaciones entran en colisión
- El algoritmo asegura que la colisión se resuelva en un intervalo razonable cuando hay colisiones entre muchas estaciones

**Formato de trama de Ethernet:**
- Preámbulo de 8 bytes, cada uno es 10101010
- *Direcciones:*
	- Se usan direcciones de 6 bytes
	- Se escriben como 6 pares de dígitos hexadecimales separados por "-" (Ejemplo 1A-23-F9-CD-06-9B)
	- El bit de orden mayor de la dirección de destino es 0 para las direcciones ordinarias y de 1 para las direcciones de grupo
	- Una trama que consiste únicamente de bits 1 en el campo de destino se acepta en todas las estaciones de la red (Broadcasting)
- *Campo Tipo:*
	- Uso de múltiples protocolos de capa de red a la vez en la misma máquina
 	- El kernel debe saber a cual entregarle la info de la trama que llegó
  	- El campo de tipo indica al receptor a qué proceso entregarle la trama
 
- *Longitud de trama mínima:*
	- Las tramas deben tener al menos 64 bytes de largo, de la dirección de destino a la suma de verificación
 	- Cuando la porción de datos de una trama es menor a 46 bytes se usa el *campo de relleno* (para alcanzar los 64B)
 
- *Suma de verificación:*
	- Tiene 32 bits de largo
 - Se usa el método de detección de errores llamado código polinomial

Cuando IEEE estandarizó la Ethernet hizo los siguientes cambios al formato DIX:
- Reducir el preámbulo a 7 bytes y usar el último byte para un *delimitador de inicio de trama*
- Cambiar el campo de Tipo po un *campo de longitud*
- Poner un pequeño encabezado a los datos para dar información de tipo