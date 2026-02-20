La capa física del IoT se encarga de la transmisión de bits a partir de medios físicos. Los problemas a resolver en esta capa son:
- *El consumo energético:* hay dispositivos IoT que son alimentados por batería y necesitan ser eficientes en el uso de la energía. Implementando de esta forma técnicas como el modo sueño
- *Interferencias y ruido:* las comunicaciones inalámbricas pueden ser afectadas por interferencias y ruido. Se usan técnicas de modulación adaptativa para optimizar la transmisión según las condiciones del canal ajustando el tipo de modulación según el nivel de interferencia o ruido
- *Conectividad:* garantizar que los dispositivos pueden mantenerse conectados en entornos difíciles. Se puede implementar una *malla* de modo que todos los dispositivos se comuniquen entre sí directamente

Los protocolos de esta capa son:
- *Zigbee:* diseñado para ser eficiente en el consumo de energía, siendo ideal para dispositivos alimentados por baterías
- *LoRaWAN:* permite la comunicación de largo alcance con un bajo consumo de energía
- *NB-IoT:* permite baja potencia y larga duración de la batería