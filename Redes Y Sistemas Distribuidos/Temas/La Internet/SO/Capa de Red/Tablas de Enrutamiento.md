Una máscara de una red está formada por 1s para identificar la red seguido de 0s para identificar las máquinas. ¿Cual es la máscara de la red de prefijo 128.208.0.0/24?
La máscara seria 11111111 11111111 11111111 00000000, otra forma de expresarla es 255.255.255.0

¿Como podría definirse la tabla de enrutamiento?
Para ello el enrutamiento es jerárquico y solo se representan redes de organismos- las llamadas subredes.
Cada entrada de la tabla de enrutamiento se extiende para darle una máscara de 32 bits. *Tabla de enrutamiento* para todas las redes tiene entradas: (dirección IP inicio subred, máscara, línea de salida)


**Uso de la tabla de enrutamiento cuando llega un paquete:**
1. Extrar dirección de destino IP
2. Luego analizar la tabla entrada por entrada, hacer AND de la máscara de la entrada con la dirección de destino y comparar el resultado con la dirección IP de inicio de la subread de la entrada
3. Si coinciden entradas múltiples se usa la máscara más larga (la red más pequeña)
