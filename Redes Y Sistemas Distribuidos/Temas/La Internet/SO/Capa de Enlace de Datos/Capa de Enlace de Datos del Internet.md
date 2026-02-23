**Limitaciones de los canales de comunicación:**
- Cometen errores ocasionales
- Tienen una tasa de datos finita
- Hay retardo de propagación

**Meta necesaria:**
- Lograr una comunicación confiable y eficiente entre dos máquinas adyacentes, o sea conectadas por un canal de comunicaciones
¿Cómo cumplir este requisito?

Para ello se debe definir una capa debajo de la capa de red que se encargue de esto. Dicha capa se llama *Capa de Enlace de Datos (CED)*. Un protocolo de CED hace que las líneas de comunicación parezcan perfectas o al menos bastante buenas

**Funciones de la CED:**
- *Comunicación confiable:* que las tramas envíadas lleguen. Se usan protocolos de tubería o parada y espera
- *Control de flujo:* evitar que el emisor rápido sature al receptor lento
- *Entramado:* en el canal de difusión solo hay un stream de bits. Usualmente se usa un patrón especial de bits para detectar el inicio y fin de cada trama llamado bandera
- *Detección y corrección de errores:* estudiada la teoria con Penazzi en Matematica Discreta 2
- *Manejo de colisiones:* ocurren en canales de difusión usados por varias máquinas. Cuando dos máquinas intentan transmitir tramas al mismo tiempo ocurre una colisión

¿Por qué estudiar la capa de enlace de datos?
- Saber sobre la CED ayuda a comprender el funcionamiento de las LAN, las cuales están en todos lados.
- Hay que diseñar, configurar y administrar esas redes LAN.
- Para comprender los protocolos que resuelven los problemas de diseño de las LAN. Para control de flujo, control de colisiones, control de errores 

**Aprenderemos:**
1. Tramas de CED y su manejo
2. Fundamentos de comunicación de tramas en CED
3. Necesidad de canales de difusión
4. Necesidad de control de colisiones