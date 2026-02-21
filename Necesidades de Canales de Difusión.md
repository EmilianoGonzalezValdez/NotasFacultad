Es costoso e incómodo hacer que todo par de máquinas de una organización están conectadas directamente entre sí por dos canales (dedicados exclusivamente para ellas). Si hay n máquinas daría n * (n-1) conexiones

El problema es encontrar una alternativa más económica para conectar varias máquinas entre sí.
La solución es usar *canales de difusión*. En un canal de difusión están conectadas varias máquinas que quieren transmitir tramas por el canal. Si una máquina envía un mensaje, todas las demás lo reciben.
Esta es una alternativa mucho más económica. Pero según veremos los canales de difusión introducen algunos problemas nuevos de diseño

**Tipos de canales de difusión:**
- *Inalambricos:* En su forma más simple las máquinas se comunican entre sí sin uso de cables
- *Cableados:* Las máquinas se comunican entre sí por medio de cables
