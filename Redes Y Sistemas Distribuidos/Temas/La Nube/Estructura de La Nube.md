Una nube se la puede considerar una red jerárquica compuesta por 4 niveles:
- *Regiones:* Son ubicaciones geográficas donde los proveedores de servicios en la nube tienen centros de datos, aunque cada región puede albergar múltiples zonas de disponibilidad 
- *Zonas de disponibilidad:* Son centros de datos aislados dentro de una región que están diseñados para operar independientemente, proporcionando redundancia y alta disponibilidad, ya que si una zona falla, las aplicaciones pueden seguir funcionando en otra 
- *Nube privada virtual (VPC):* Una VPC es una red virtual lógicamente aislada dentro de una nube pública que permite a los usuarios definir su propio entorno de red. Dentro de una VPC se pueden crear subredes públicas y privadas, lo que permite un control granular sobre el acceso a los recursos 
- *Subredes:* Las subredes son divisiones dentro de una VPC que permiten organizar y aislar recursos. Estas pueden ser públicas o privadas en relación al acceso al internet, lo cual facilita la gestión del trafico y la seguridad 


Hay diferentes tipos de nodos en una nube:
- *Servidores web:* Manejan las solicitudes HTTP/HTTPS y sirven contenido web
- *Servidores de aplicaciones:* Procesan la lógica de la aplicación y acceden a la base de datos 
- *Servidores de bases de datos:* Manejan las bases de datos
- *Almacenamiento de Objetos:* Utilizado para almacenar archivos estáticos como imágenes, vídeos y archivos de configuración
- *Balanceadores de carga:* Distribuyen el trafico entre múltiples servidores para optimizar el uso de los recursos y mejorar la disponibilidad 

Existe una **clasificación de los balanceadores de carga:**
- *Balanceador de carga Externo:* Se usa para distribuir tráfico de clientes externos hacia los servidores web
- *Balanceador de carga Interno:* Se usa para distribuir el tráfico entre servidores internos, como entre servidores web y entre servidores de aplicaciones o bases de datos, sin exponer estos recursos al público. Solo está accesible desde una VPC 

**Tipos de enrutadores en la nube:**
- *Enrutador de la VPC:* Se encarga de la comunicación entre las subredes dentro de la misma VPC y de dirigir el tráfico hacia y desde internet o hacia otras VPCs. De esta forma los servidores de diferentes subredes dentro de una misma VPC se comunican a través del enrutador de la VPC
- *Puerta de enlace de internet:* Se conecta a la internet y permite que los servidores en las subredes publicas envíen y reciban trafico de internet 
- *Puerta de enlace de VPCs:* Se usan para comunicar diferentes VPCs entre si