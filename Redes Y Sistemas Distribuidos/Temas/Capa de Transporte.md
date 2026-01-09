
# Capa de Transporte



En la capa de transporte se provee la comunicación entre procesos, mejorando así los servicios de la [[Capa de Red]], todo esto ejecutándose por completo en los host y a través de las Entidades de transporte(ET) las cuales son el nombre que se les da al software y hardware de la CT



**Problemas que deberia solucionar la CT:**

- Uso de temporizadores y retransmisiones de paquetes

- Uso de buferes y control de flujo

- Evitar congestionar la red poniendo demasiados paquetes en ella

- Perdida de paquetes de la CR



# *Capa de transporte:TCP/IP*

La capa de transporte de internet tiene 2 protocolos:

1. **TCP:** Divide el flujo en bytes entrantes en mensajes discretos y pasa cada uno de ellos a la capa de interred. TCP proporciona entrega confiable y en orden de los mensajes reensamblando los mensajes recibidos en el receptor. Ademas maneja el control de flujo y de congestion

2. **UDP:** Proporciona una entrega de mensajes no confiable y desordenada. Tampoco utiliza confirmaciones de recepcion para los mensajes ni tiene control de lfujo, congestion o retransmision al recibir un mensaje erroneo.

    ¿Para que se usa entonces?

    Bueno pues se usa para aplicaciones que no usan el control de flujo ni la secuenciacion de mensajes o que involucran consultas de solicitud-respuesta o aplicaciones de voz y vídeo



