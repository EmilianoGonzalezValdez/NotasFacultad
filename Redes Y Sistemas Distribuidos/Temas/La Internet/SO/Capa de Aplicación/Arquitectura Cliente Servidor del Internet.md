En el modelo cliente-servidor hay dos procesos que se comunican, uno en la maquina cliente y otra en la maquina servidor. La forma de comunicación es:
- El proceso cliente manda solicitud al proceso servidor
- El proceso cliente espera un mensaje de respuesta
- Luego el proceso servidor recibe y procesa la solicitud
- El proceso servidor manda mensaje de respuesta al proceso cliente

Los servidores se caracterizan por siempre estar en un host con dirección IP permanente y se pueden usar centros de datos para la escalabilidad.
Mientras que los clientes se caracterizan por podes estar conectados intermitentemente usando direcciones IP dinámicas. Además los clientes no se comunican entre si 


Ahora vamos a ver los pasos de una aplicación usando **UDP:**
1. Cliente crea datagrama con IP y puerto del servidor y envía el datagrama aunque este pueda perderse
2. Si llega, el servidor lee el datagrama
3. El servidor envía respuesta especificando dirección y puerto de cliente. Tambien puede perderse esta respuesta
4. Si llega, el cliente lee el datagrama de respuesta 
5. Cliente finaliza
En este caso no se especifica que pasa si la respuesta llega o no al cliente. Esto es responsabilidad de la red 

Ahora veremos los pasos pero usando **TCP:**
1. Se ejecuta proceso del servidor
2. Servidor espera por pedido de conexión entrante
3. El cliente requiere pedido de conexión al servidor
4. El servidor acepta la conexión con el cliente
5. El cliente envía su pedido al servidor
6. El servidor lee el pedido
7. El servidor envía la respuesta
8. El cliente lee la respuesta
9. Si hay mas pedidos al servidor se vuelve al paso 5
10. El cliente cierra la conexión
11. El servidor cierra la conexión 
