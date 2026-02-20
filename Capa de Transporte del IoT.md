La capa de transporte Asegura la transmisión de datos confiable y ordenada entre dispositivos. Problemas:
- *Fiabilidad de la transmisión:* asegurar que los datos lleguen de manera confiable, en especial en redes con alta tasa de pérdida de paquetes
- *Control de flujo y congestión*
- *Compatibilidad de protocolo:* integración con protocolos específicos de IoT

Protolocos:
- *De internet:* TCP, UDP
- *MQTT:* optimizado para redes con ancho de banda limitada, diseñado para minimizar el consumo de energía durante la transmisión de datos, proporciona varios niveles de calidad de servicio para garantizar la entrega de mensajes. Usa formato de mensaje compacto para minimizar el tamaño de los datos enviados, esto reduce el consumo de energía. MQTT usa TCP como base para la transmisión de datos. Se centra en la comunicación en tiempo real
- *CoAP:* optimizado para dispositivos con recursos limitados, como baja capacidad de procesamiento y memoria. Proporciona confirmaciones de entrega y retransmisión de mensajes perdidos. Esta optimizado para minimizar el uso de ancho de banda, también usa formato binario de mensaje compacto. Generalmente se implementa sobre UDP 