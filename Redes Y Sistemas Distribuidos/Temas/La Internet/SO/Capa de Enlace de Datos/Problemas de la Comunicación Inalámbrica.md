Los nodos inalámbricos usualmente no pueden transmitir y recibir al mismo tiempo. La potencia generada por el emisot es mucho más alta que el rango de sensibilidad del receptor. A menos que se implementen aislaciones o técnicas avanzadas (difíciles en dispositivos pequeños) se satura el circuito receptor

No se puede aplicar un protocolo como el de Ethernet. Porque no se puede comparar lo que se transmite con lo que se escucha para detectar colisiones.
En lugar de CSMA/CD (Acceso múltiple con Detección de Portadora y Detección de Colisiones) (Ethernet) se usa CSMA/CA (Acceso múltiple con Detección de Portadora y Evitación de colisiones) (WiFi 802.11)


**Problema de la estación oculta:**
- La estación C transmite a la estación B
- Si A detecta el canal no escuchara nada y concluirá erróneamente que ahora puede comenzar a transmitir a B, si lo hace, ¡colisión!

<img width="412" height="280" alt="imagen" src="https://github.com/user-attachments/assets/04fefecc-7642-45c6-b658-b39d3f838ebd" />


**Problema de la estación expuesta:**
- Supongamos que B está transmitiendo a A. C desea enviar a D por lo que escucha el canal.
- Cuando escucha una transmisión concluye erróneamente que no debería transmitir a nadie porque escucha la transmisión de B-
- Pero no hay problema si C transmite a D, porque no va a interferir con la habilidad de A de recibir de B (si puede interferir con A enviando a B, cosa que no pasa en nuestro ejemplo)
 

   <img width="625" height="257" alt="imagen" src="https://github.com/user-attachments/assets/161206f2-c5a9-4b39-9cab-4237b7b0e374" />


**Protocolo de subcapa MAC 802.11:**

802.11 soporta dos modos para atacar los problemas anteriores:
- *DFC (Función de coordinación distribuida)* la cual es para redes ad hoc
- *PCF (Función de coordinación puntual)*, esta es para redes basadas en infraestructura. utiliza la AP para controlar toda la actividad en su celda

