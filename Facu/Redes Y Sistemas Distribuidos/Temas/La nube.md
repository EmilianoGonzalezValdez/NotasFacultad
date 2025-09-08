
# La nube



#### La nube permite el acceso remoto a un conjunto de recursos informáticos a través de una red de servidores interconectados

- Estos servidores utilizan protocolos para comunicarse entre si y con los usuarios

- Los recursos se asignan y usan dinamicamente según las necesidades de los servicios ofrecidos permitiendo a las organizaciones optimizar su infraestructura tecnológica sin necesidad de gestionar físicamente el hardware

- Los usuarios pueden acceder a estos recursos desde cualquier lugar conectándose a [[La Internet]]




Estas nubes se pueden clasificar de la siguiente manera:

1. Nube publica: Donde los recursos de la infraestructura compartida proporcionada por los proveedores son compartidos entre múltiples usuarios

2. Nube privada: Infraestructura dedicada a una sola organización oara mantener el control y la seguridad

3. Nube híbrida: Le permite a las empresas aprovechar lo mejor de ambos mundos




# Estructura de la Nube



Podemos considerar a la nube como una red jerárquica de 4 niveles 

- **Regiones:** ubicaciones geográficas donde los proveedores de servicios en la nube tienen centros de datos

- **Zonas de disponibilidad**, Centros de datos aislados dentro de una región que operan independientemente 

- **Nube privada Virtual(VPC),** es una red virtual lógicamente aislada dentro de una nube publica, esta red privada puede controlarse totalmente. Una VPC puede abarcar varias zonas de disponibilidad

- **Subredes:** son divisiones dentro de una VPC que permiten organizar y aislar los recursos

# Tipos de Nodos en una Nube

- **Servidores Web**: manejan las solicitudes HTTP/HTTPS y sirven
contenido web.

- **Servidores de aplicaciones:** Procesan la lógica de la aplicación y
acceden a la base de datos.

- **Servidores de bases de datos:** maneja las bases de datos (por ejemplo
relacional).

- **Almacenamiento de objetos:** utilizado para almacenar archivos
estáticos como imágenes, videos y archivos de configuración.

- **Balanceadores de carga:** distribuyen el tráfico entre múltiples
servidores para optimizar el uso de los recursos y mejorar la
disponibilidad.

    - **Balanceador de carta externo:** Se usa para distribuir tráfico
    de clientes externos hacia los servidores web (los usuarios
    externos envían solicitudes al balanceador de carga).

    - **Balanceador de carga interno:** se usa para distribuir el tráfico
    entre servidores internos, como entre servidores web y
    servidores de aplicaciones o bases de datos, sin exponer estos
    recursos al público. Solo está accesible desde una VPC.



# Tipos de enrutadores en la Nube

- **Enrutador de la VPC:**  se encarga de la comunicación entre las subredes dentro de la misma VPC y de dirigir el trafico hacia y desde internet a través de la puerta de enlace a internet, o hacia otras VPC a traves de la puerta de enlace VPC

- **Puerta de enlace a Internet:** se conecta a la internet y permite que los
servidores en las subredes publicas envíen y reciban trafico de internet.

- **Puerta de enlace de VPCs:** se usan para comunicar diferentes VPCs entre si.

- 


