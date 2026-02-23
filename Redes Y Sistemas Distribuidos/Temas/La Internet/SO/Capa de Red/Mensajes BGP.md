Los mensajes de BGP son cuatro y cada uno cumple una función especifica dentro del establecimiento y mantenimiento de la sesión BGP y el intercambio de información de enrutamiento:
- *OPEN:* se utilizan para establecer una sesión BGP entre dos enrutadores una vez que se ha establecido la conexión TCP. En este mensaje se negocian *parametros esenciales* como: versión de BGP, número de SA local, tiempo de espera para la sesión, identificador del enrutador (Router ID)
- *UPDATE:* se usa para anunciar nuevas rutas o retirar rutas que ya no son válidas. Se envía cada vez que hay un cambio en las rutas conocidas, ya sea una nueva mejor ruta o la supresión de una existente. **Contiene** el prefijo de red que se anuncia o retira, atributos BGP que ayudan a los enrutadores a decidir la mejor ruta. **Estructura:** longitud de lista de rutas retiradas, lista de prefijos que se retiran, longitud de sección de atributos (para ruta anunciada), ruta anunciada (sus atributos BGP), prefijos de ruta anunciada
- *KEEPALIVE:* una vez establecida la sesión BGP, se envían periódicamente mensajes KEEPALIVE para confirmar que ambos extremos siguen activos y mantener viva la sesión. Estos mensajes solo sirven para mantener la conexión activa y evitar que se cierre por inactividad. El intervalo de envío se negocia en el mensaje OPEN.
- *NOTIFICATION:* se envía cuando un error que requiere cerrar la sesión BGP. Este mensaje indica la causa del error (como recepción de un mensaje mal formado, fallo en la sesión, timeout, etc.) y tras enviarlo se cierra la conexión TCP. Tambien se usa para informar condiciones inusuales o problemas en la sesión

**En resumen el flujo típico es:**
- Se establece la conexión TCP.
- Se intercambien mensajes OPEN para negociar parámetros
- Se envían KEEPALIVE periódicos para mantener la sesión
- Se intercambian UPDATE para anunciar o retirar rutas
- Si hay errores, se envía NOTIFICATION y se cierra la sesión