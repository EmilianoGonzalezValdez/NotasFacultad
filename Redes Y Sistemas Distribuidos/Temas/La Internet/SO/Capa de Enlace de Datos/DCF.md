<img width="759" height="242" alt="imagen" src="https://github.com/user-attachments/assets/909c9a4f-29fd-46a5-a00f-f5db9edadbfa" />

En la imagén podemos ver el protocolo CSMA/CA de 802.11 para redes ad hoc **DCF** donde:
- A desea envíar a B
- C es una estación que está dentro del alcance de A
- D esta dentro del alcance de B pero no dentro del de A

1. A decide enviar datos a B. A le envia una trama *RTS* a B en la que le solicita permiso para enviarle una trama
2. Cuando B recibe esta solicitud, podría decidir otorgarle el permiso, en cuyo caso le regresa una trama *CTS*
3. Al recibir la CTS A envía su trama y comienza su temporizador de ACK. Si el temporizador de ACK de A termina antes de que el ACK regrese, todo el protocolo se ejecuta de nuevo
4. Al recibir correctamente la trama de datos, B responde con una trama de ACK

**Comportamiento de la estaciones C y D:**
- C recibe la trama RTS y desiste de transmitir cualquier cosa hasta que el intercambio esté completo
- A partir de la información en RTS C estima cuánto tardará la secuencia, incluyendo el ACK final e impone para si misma un canal virtual ocupado *NAV (vector de asignación de red)*
- D escucha el CTS y también impone un canal NAV para si misma

En general las tramas de control se transmiten a menor tasa de transferencia que las tramas de datos (menos probable que ocurran errores de transmisión)

El tiempo entre tramas puede ser:
- *DIFS:* DCF
- *SIFS* 


*Colisiones:* Dos nodos pueden detectar un enlace ocioso y tratar de enviar un RTS al mismo tiempo, causando que esos RTS colisionen. Los emisores asumen que ocurrió colisión porque no reciben el CTS luego de un cierto intervalo de tiempo.

*Manejo de la colisión:* Cada emisor espera una cantidad de tiempo aleatoria antes de tratar de nuevo. Esta cantidad de tiempo es definida por el algoritmo de retroceso exponencial binario

*Estación oculta:* El CTS probablemente va a ser escuchado por una estación oculta (establece el NAV). Esto dice a los nodos dentro del rango del receptor que no deberían enviar nada por un tiempo incluido en el RTS y CTS. Luego de ese tiempo más un pequeño intervalo el canal puede ser asumido disponible otra vez y otro nodo es libre de intentar enviar

DCF  no resuelve el problema de estación expuesta