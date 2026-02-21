La **regulación de tráfico** es cuando los emisores ajustan sus transmisiones para enviar un tráfico que la red pueda soportar.
La congestión se da en los enrutadores (y no en los hosts).
¿Como se puede enterar un host de que hay congestión?
Bueno pues, se le avisa de la congestión
Una vez que un enrutador tiene una línea de salida en estadod e advertencia puede avisar a los hosts responsables de los paquetes que llegan a esa línea congestionada

**Método de paquetes reguladores:**
1. Usar *paquetes reguladores* si la línea de salida esta en estado de advertencia. El enrutador regresa un *paquete regulador (PR)* al host de origen, proporcionándole el destino encontrado en el paquete
2. Para que el paquete original no genere más PR más adelante en la ruta, en el paquete original se activa un bit del encabezado y despúes se reenvía
3. El PR le pide al host de origen que reduzca en un porcentaje X el tráfico enviado al destino especificado
4. El host ignora los PR que se refieran a ese destino por un intervalo fijo
5. Una vez que haya expirado ese tiempo, el host escucha más PR durante un intervalo I. Si llega alguno, el host reduce el flujo aún más y comienza a ignorar nuevamente los PR. Si no llega ningun PR durante I, el host incrementa el flujo

Lo malo del método de paquetes reguladores es que a altas velocidades o distancias grandes, el envío de un paquete regulador a los hosts de origen no funciona bien porque la reacción es muy lenta

La solución es el *Método de paquetes reguladores de salto por salto*. Hacer que el paquete regulador ejerza su efecto en cada salto que da, de modo que:
- Cuando el paquete regulador llega a un enrutador F, se le obliga a F a reducir el flujo al siguiente enrutador D (F deberá destinar más buferes al flujo)
- Luego el paquete regulador llega al enrutador E anterior a F e indica a E que reduzca el flujo a F. Esto impone una mayor carga a los buferes de E, pero da un alivio inmediato a F. Y se sigue así sucesivamente


**Método de bit de advertencia**. Señalar el estado de advertencia activando un bit especial en el encabezado del paquete. Cuando el paquete llega a su destino, la entidad transportadora copia el bit en la siguiente confirmación de recepción que se regresa al origen. A continuación el origen reduce el trafico. Mientras el enrutador está en estadod e advertencia, continua activando el bit de advertencia, lo que significa que el origen continua obteniendo confirmaciones de reepción con dicho bit activado.
El origen monitorea la fracción de confirmacipnes de recepción con el bit activado y ajusta su tasa de transmisión de manera acorde. En tanto los bits de advertencia continuan fluyendo, el origen continua disminuyendo su tasa de transmisión.
Cuando la tasa de transmisión disminuye lo suficiente, el origen incrementa su tasa de transmisión. Debido a que cada enrutador a lo largo de la ruta puede activar el bit de advertencia, el tráfico se incrementa solo cuando no había enrutadores con problemas

Una implementación de bit de advertencia usada por TCP es *ECN (Explicit Congestion Notification):*
- Se usa en TCP/IP
- Se marcan 2 bits en el encabezado IP con distintos fines
- 	00: transporte no capaz en ECN
- 	10: transporte capaz de ECN, ECT(0)
- 	01: transporte capaz de ECN, ECT(1)
- 	11: congestión encontrada, CE
- Si ambos extremos soportan ECN mandan sus paquetes con ECT(0) y ECT(1) respectivamente
- Si el paquete atraviesa una cola congestionada y el enrutador soporta ECN, se cambia código en el paquete CE para avisar al receptor de la congestión
- El uso de ECN en conexión TCP es opcional
- Para usar ECN, debe ser negociado al establecer la conexión TCP incluyendo opciones adecuadas en segmentos SYN y SYN-ACK
- Se usan dos banderas en encabezado TCP para soportar ECN:
- 	ECE(ECN echo): se usa para mandar indicación de congestión al emisor
- 	CWR (ventana de congestión reducida): es usada para confirmar que la indicación ECE fue recibida

**Secuencia de ejecución de ECN típica:**
1. Se negocia ECN en conexión TCP
2. Emisor manda paquete IP P con ECT(0)
3. P llega a enrutador congestionado que soporta ECN y enrutador marca P con CE
4. Receptor recibe P con CE y manda segmento Q(con ACK P) de vuelta usando bandera ECE prendida
5. Emisor recibe Q con ECE prendido, entonces emisor reduce la ventana de congestión
6. Emisor manda siguiente segmento al otro extremo usando la bandera CWR prendida para confirmar recepción de aviso de congestión
Se continúa transmitiendo segmentos con ECE prendido hasta recibirse un segmento con CWR prendido