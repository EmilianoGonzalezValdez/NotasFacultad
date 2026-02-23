**Se trabaja con:**
- Confirmaciones de recepción de tramas
- Temporización de reenvío
- Retransmisiones de tramas (perdidas o dañadas)
- Uso de números de secuencia en las tramas (para identificar tramas duplicadas)
- Llevar a caballito para aprovechar mejor el canal de comunicaciones
- Uso de protocolos como parada y espera o de tubería

La forma de actuar de la CED se puede resumir en los siguientes pasos:
- La CED toma de la CR paquetes y los encapsula en *tramas*
- Las tramas tienen una longitud máxima impuesta
- Cada paquete de la CR se divide en tramas
- En la CR de la máquina de origen hay un proceso que entrega bits a la CED para transmitirlos a la máquina de destino
- El trabajo de la CED es transmitir los bits de la máquina de destino para que puedan ser entregados a su CR

**Flujo de los enrutadores:**
1. Al llegar una trama al enrutador: el hardware verifica si está libre de errores
2. La CED comprueba si esta es la trama esperada y de ser asi, entrega el paquete dentro de la trama al software de enrutamiento
3. El software de enrutamiento elije la línea de salida adecuada y entrega el paquete a la CED para enviarlo

Aún así, ¿Cómo podemos asegurar que una trama se entregue?
Para ello, si una trama no se entregó, entonces el emisor la reenvía.

Para su implementación se toman las mismas medidas que en las capas anteriores con los ACK:
- Regresar *tramas de control* con confirmaciones de recepción positivas o negativas de las tramas que llegan.
- Método que usa *temporizador de retransmisiones* en la CED

De la misma forma para solucionar el caso donde se pierda una confirmación de recepción y se envíe la trama de nuevo y esta llega 2 veces; la solución vuelve a ser agregar *números de secuencia* a las tramas

Para transmitir datos entre dos máquinas y en ambas direcciones eficientemente se recurre al *piggybacking*.

En otras palabras, los problemas de esta capa relacionados a la comunicación con tramas, se resuelven de la misma manera que vimos estas soluciones en las capas anteriores