En el estándar 802.11 (Wi-Fi), los intervalos SIFS, PIFS y DIFS son períodos de tiempo que las estaciones deben esperar antes de transmitir tramas
Estos intervalos son cruciales para la coordinación del acceso al medio inalámbrico y para evitar colisiones, especialmente en el modo de contención (DCF)
Funcionan como mecanismos de prioridad, donde intervalos más cortos significan mayor prioridad para acceder al canal

SIFS (*intervalo entre tramas en el mismo diálogo*) de 28 us
- Se puede usar para enviar tramas: ACK, CTS, trama de datos, transmitir el próximo fragmento de ráfaga de fragmentos
- Solo una estación puede responder a intervalo SIFS
PIFS (*intervalo entre diálogos diferentes*) de 78 us
- El periodo libre de contención en el que se usa PCF se divide en diálogos
- Pra división entre esos diálogos se usa un intervalo PIFS
DIFS (*intervalo luego de período PCF*) de 128 us
- Intervalo entre tramas asumido por nodos que ejecutan DCF (CSMA/CA)

Dentro de un diálogo se usan intervalos *SIFS (short interframe space):*
- Se utiliza para asegurar que las tramas de alta prioridad, que forman parte de una secuencia de intercambio, puedan transmitirse con la mínima demora. Esto permite una comunicación eficiente y confiable durante una transacción en curso
- Hacen falta los SIFs para cosas como calcular suma de verificación, entramado de la proxima trama.
- Hay solo una estación que puede responder luego de un intervalo SIFS
- Si falla en hacer uso de su chance y ocurre un tiempo PIFS, el AP puede mandar una trama
- **Uso común:**
	- ACK: Después de recibir una trama de datos exitosamente, la estación receptora espera un SIFS antes de enviar la trama ACK ára confirmar la recepción. Esto asegura que el ACK tenga prioridad y la estación transmisora sepa rápidamente si su trama llegó correctamente
 - CTS: En el mecanismo RTS/CTS, la estación receptora responde a una trama RTS con una trama CTS después de un SIFS, indicando a la estación transmisora que puede comenzar a enviar sus datos
 - Fragmentación: Cuando una trama grande se fragmenta, los fragmentos consecutivos se envían con un intervalo SIFS entre ellos. Esto asegura que la ráfaga de fragmentos no sea interrumpida por otras estaciones

Entre dos diálogos diferentes se usa un *PIFS* (dentro de PCF), PCF intergrame space:
- El PIFS se utiliza en el modo acceso controlado por el punto de acceso (AP) llamado PCF. El AP, que actúa como coordinador, utiliza el PIFS para ganar prioridad sobre las estaciones que operan en modo de contención (DCF)
- El AP espera un PIFS antes de transmitir una trama Beacon que inicia el periodo libre de contención.
- Al ser más corto que el DIFS, el AP tiene prioridad para comenzar el período donde controla el acceso al medio mediante sondeo

El AP puede hacer sondeo en forma de round-robin a todas las estaciones configuradas para polling:
- Cuando se emite un sondeo, la estación afectada responde usando un SIFS
- Si el AP recibe una respuesta a un poll, puede hacer otro poll usando PIFS. Si no se recibe respuesta al poll, el AP puede ahcer poll

Luego de un período de PCF, viene un DCF (con CSMA/CA), cuyas conversaciones se rigen por un *DIFS* (DCF interframe space):
- El DIFS se utiliza en el modo de acceso fundamental y distribuido de 802.11 llamado DCF. Una estación que desea transmitir en el modo de contención debe asegurarse de que el medio inalámbrico ha estado inactivo durante al menos un período DIFS antes de intentar transmitir.
- **Uso comun:**
	- Acceso inicial al medio: cuando una estación tiene datos para enviar y el medio está inactivo, debe esperar un intervalo DIFS. Si el medio permanece inactivo durante este tiempo, la estación puede intentar transmitir
 - Después de una transmisión exitosa: Después de que una estación (que no está respondiendo con un ACK o CTS) termina de transmitir, cualquier otra estación que desee transmitir debe esperar un intervalo DIFS para asegurar un tiempo de silencio adecuado en el medio
 - Mecanismo de Backoff: Si una estación detecta que el medio está ocupado mientras espera el DIFS, o si ocurre una colisión, la estación entre en un período de "backoff" aleatorio después de que el medio se vuelve inactivo durante un DIFS. Este backoff ayuda a reducir la probabilidad de colisiones futuras 