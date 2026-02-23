**Fenómenos sucediendo en un canal que una estación podría detectar:**
- Detectar que el canal está en uso (o sea, alguna estación enviando una trama)
- Detectar que hay una colisión en el canal
- En las LAN actuales cada estación puede detectar si el canal está en uso. En realidad, detecta si están llegando bits de alguna trama a la máquina que hace detección. Los protocolos que pueden hacer esto se llaman *Protocolos de detección de portadora (CSMA)* La gran ventaja de poder hacer detección de portadora es que se evita generar colisión poniendo tramas en el canal cuando están llegando bits de alguna trama
- En las LAN actuales cada estación puede detectar si está ocurriendo una colisión cuando está transmitiendo una trama. Para ello el hardware de una estación escucha el cable mientras transmite. Si lo que lee es distinto de lo que puso él, sabe que está ocurriendo una colisión
- Si una estación que está transmitiendo una trama detecta que está ocurriendo una colisión, no tiene sentido seguir enviando la trama; por lo tanto es mejor que las estaciones aborten sus transmisiones tan pronto como detecten una colisión
- Ventajas de la detección de colisiones: ahorra tiempo y ancho de banda. Sin esta tecnología cuando ocurre una colisión, la estación no va a recibir la confirmación de recepción y va a tener que retransmitir la trama y esta espera va a llevar mucho más rapido

En conclusión, para definir las PAMs conviene que una estación pueda detectar lo que está pasando en el canal.
