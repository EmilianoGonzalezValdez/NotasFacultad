La capa de enlace de datos es responsable de la transmisión de datos entre dispositivos dentro de la misma red local. Los problemas considerados son:
- *Control de errores:* igual que antes
- *Control de acceso al medio:* igual que antes
- *Retrasos y variaciones en el tiempo de transmisión:* pueden afectar a las aplicaciones en tiempo real. Una idea de solución es ajustar el tamaño y la estructura de las tramas para minimizar la latencia
- *Desconexiones frecuentes:* los dispositivos IoT al ser móviles o ubicarse en áreas con mala cobertura pueden sufrir desconexiones frecuentes
- *Seguridad de la comunicación:* los datos transmitidos no deben ser interceptados ni alterados. Se puede aplicar cifrado y autenticación en la capa de enlace de datos para asegurar la comunicación  

Los protocolos usados son: 
- *Ya vistos o conocidos:* Wi-Fi, Ethernet, Bluetooth
- *También en capa física:* Zigbee, LoRaWAN
- *Bluetooth Low Energy(BLE):* muy eficiente en consumo de energía, ideal para dispositivos que necesitan durar mucho tiempo con baterías pequeñas. Tiene un menor costo de implementación en comparación con otras tecnologías 
- *6LoWPAN:* permite encapsular y enviar paquetes IPv6 sobre redes de baja potencia. Se puede usar en sensores y actuadores. Implementa técnicas de comprensión de encabezado y fragmentación para permitir que los paquetes IPv6 se transmitan eficientemente en redes WPAN de baja potencia 