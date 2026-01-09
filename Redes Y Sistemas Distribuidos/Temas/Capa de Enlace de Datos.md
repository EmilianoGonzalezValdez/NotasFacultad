
# Capa de Enlace de Datos



El objetivo de la capa de enlace de datos es transformar un medio de transmision puro en una linea de comunicacion que parezca libre de errores de transmision

**Problemas de diseño que se consideran:**

- Fragmentacion de paquetes en tramas cuando un paquete es demaciado grande

- Tramas de confirmacion de recepcion

- Control de flujo

- Control de acceso a un canal compartido



**Control de errores:**

Puede pasar que los mensajes lleguen con errores debido al imperfecto medio físico de comunicación. para lograr solucionarlo los mensajes deben llevar cierta información extra


