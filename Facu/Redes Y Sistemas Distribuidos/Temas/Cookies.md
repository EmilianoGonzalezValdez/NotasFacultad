
# Cookies



Una coockie es un pequeño archivo oc adena de texto(a lo sumo 4 kb). Su contenido toma la faorma "nombre = valor". Se utilizan para enviar en los pedidos y respuestas HTTP información de estado de sesión

**Estructura de una cookie:**

Además de su contenido hay otros campos en una cookie:

- **Dominio:** Nombre del dominio destino de la cookie(cada dominio puede almacenar hasta 20 cookies)

- **Ruta** en la estructuradel directorio del servidor, esta identifica qué partes del árbol de archivos del servidor podrían usar el cookie

- El **campo contenido** toma la forma **nombre = valor**

- El campo **expira**: Si este campo está ausente, el navegador descarta la cookie cuando sale. SI se proporciona una fecha y hora se mantiene la cookie hasta que expira el horario

- El campo **seguro:** Se usa para indicar que el navegador solo puede retornar la cookie a un servidor usando un transporte seguro. Estos se usa para aplicaciones seguras



Las cookies se almacenan en el disco duro de la máquina cliente en un **directorio de cookies** y en una base de datos al recibir las cookies en un servidor. Para eliminar una cookie e servidor simplemente la envía nuevamente con la fecha caducada.

Cuando un cliente solicita una página web, el servidor puede proporcionar una cookie junto con la página solicitada



Antes que un navegador solicite una página a un sitio web, verifica su directorio de cookies para ver si el dominio al  que está solicitando la página ya colocó alguna cookie. De ser así, todas las cookies para ese dominio se incluyn en el mensaje de la solicitud. Cuando el servidor las obtiene, puede interpretarlas de la forma que desee

