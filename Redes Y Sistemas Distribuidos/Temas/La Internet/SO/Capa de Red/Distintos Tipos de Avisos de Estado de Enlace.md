Un tipo de *aviso de estado de enlace (AEE)* contiene el costo de un enrutador a todos sus vecinos, este tipo de paquetes fue visto en el protocolo de estado de enlace.
Como un SA es jerárquico, un área no puede conocer la topología de otra área A, pero sí información resumida de A. Dicha *información resumida de área* es otro tipo de aviso de estado de enlace.
Los EBA *resumen* información de enrutamiento aprendida de un área para hacerla disponible en sus AEE que envían a las otras áreas


¿Cómo definir la información resumida de un área no dorsal?
Un EBA E recibe avisos de estado de enlace de todos los enrutadores de una de sus áreas A y con esa información determina el costo de alcanzar cada LAN de A.
La información resumida de A contiene el costo de alcanzar cada LAN de A. Este paquete es puesto por el EBA E en la red dorsal para que llegue a las demás áreas

La información resumida de un área dorsal se define por medio de un grafo donde:
- Todos los arcos unen pared de EBA
- El peso de cada uno de estos arcos es el costo de camino óptimo (en el área dorsal) que une el par de EBAs


<img width="590" height="324" alt="imagen" src="https://github.com/user-attachments/assets/fc389c21-cfba-4618-be86-99c93130aa8c" />

En esta red dorsal, asumiendo que todos los arcos tienen pero 1, la información resumida del área dorsal es:
- Arco de R1 a R2 con costo 2
- Arco de R1 a R3 con costo 4
- Arco de R2 a R3 con costo 2
- Arco de R2 a R1 con costo 2
- Arco de R3 a R1 con costo 4
- Arco de R3 a R2 con costo 2


Información del área dorsal que recibe un área A por medio de un EBA E:
- Resúmenes de las áreas no dorsales distintas de A
- Resumen del área dorsal

**Consecuencias/impacto que tiene el envío de resúmenes por un EBA para los enrutadores:**
- Esto permite que todos los enrutadores del área dorsal aprendan el costo de alcanzar todas las redes de cada área
- Todos los enrutadores aprenden a alcanzar todas las redes en el SA
- Cada enrutador tiene una topología de su área detallada y solo conoce el costo del camino más corto a las redes en las otras áreas