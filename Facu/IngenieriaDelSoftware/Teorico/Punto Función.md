Es una estimación similar a la métrica LOC que se determina sólo con la [[SRS]] definiendo el tamaño del proyecto en términos de la "Funcionalidad":
- Entradas externas a la aplicación
- Salidas externas que deja el sistema
- Archivos lógico internos
- Archivos de interfaz externa
- Transacciones externas 

|    ==Tipo de Funciones==     | ==Simp== | ==Prom.== | ==Comp-== |
| :--------------------------: | :------: | :-------: | :-------: |
|      Entradas Externas       |    3     |     4     |     6     |
|       Salidas externas       |    4     |     5     |     7     |
|  Archivos lógicos internos   |    7     |    10     |    15     |
| Archivos de interfaz externa |    5     |     7     |    10     |
|    Transacciones externas    |    3     |     4     |     6     |

Debemos contar cada tipo de función diferenciando según sea compleja, promedio o simple teniendo en cuanta que $C_{ij}$ denota la cantidad de funciones tipo $i$ con complejidad $j$ en la formula de Punto función no ajustado (UFP):$$\sum^5_{i=1}{\sum^3_{j=1}w_{ij}C_{ij}}$$
Luego debemos ajustar UFP de acuerdo a la complejidad del entorno. Se evalúa según las siguientes características:
1. comunicación de datos 
2. procesamiento distribuido 
3. objetivos de desempeño 
4. carga en la configuración de operación 
5. tasa de transacción 
6. ingreso de datos online 
7. eficiencia del usuario final 
8. actualización online 
9. complejidad del procesamiento lógico 
10. reusabilidad 
11. facilidad para la instalación 
12. facilidad para la operación 
13. múltiples sitios 
14. intención de facilitar cambios

El factor de ajuste de complejidad (CAF) se calcula como $$0.65+0.01*\sum^{14}_{i=1}{p_i}$$
Y los Puntos función = CAF * UFP
Luego hay que multiplicar los Puntos Función por las líneas de código respectivas en lenguaje determinado

Hay que recalcar que la calidad de la *SRS* tiene impacto directo en los costos del proyecto. Por lo cual tener buenas métricas para evaluar es algo necesario. Existen:
- Métricas de *calidad directa*: Evalúan la calidad del documento estimando el valor de los atributos de calidad de la *SRS*
- Métricas de *calidad indirecta*: Evalúan la efectividad de las métricas del control de calidad usadas en el proceso en la fase de requerimientos