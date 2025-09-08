
# La Internet



> #### La internet es una red que cubre todo el globo y consiste de varias redes de área local (LAN) conectadas entre si por medio de proveedores de servicios de internet (PSI)

Cada LAN sirve como una red localizada que conecta dispositivos dentro de un área física especifica como casas, oficinas, escuelas, etc. 

Los PSI proveen servicios e infraestructura necesarios para que los usuarios conecten sus LAN a la internet usando dispositivos como enrutadores y puertas de enlace y facilitando aun mas el acceso mediante varios medios como la fibra óptica, DSL, etc.

Los mismos PSI manejan el trafico de datos entre usuarios y la red global




Cabe recalcar (aunque sea un poco obvio) que en la internet hay aplicaciones de red que nos permiten compartir recursos, comunicarnos con otras personas, hacer trabajos colaborativos, comercio electrónico, entretenimiento,etc.

Estas aplicaciones de red utilizan APIs como sockets y middlewares como la web y llamada a procedimientos remotos, estos últimos basándose en el sistema operativo de red. Este sistema operativo de red se apoya en el hardware de redes de computadoras que forman la LAN y PSI. 



# Estructura de La Internet

Los host  acceden a la internet a través de proveedores de servicio de internet de acceso(PSIs de accesos), los cuales están interconectados para que 2 personas conectadas a diferentes PSI puedan enviarse paquetes. Estas conexiones entre PSI de acceso de conoce como una malla. **Tipos de PSIs de accesos:**

- PSI residenciales

- PSI empresarial

- PSIs universitarias

- Celulares

- PSIs que proveen acceso a Internet



# ¿Como conectar a los PSI entre si?

Claramente conectar TODAS las psi de acceso entre si no es escalable ya que serian N² conexiones. ¿Entonces que se hace? Bueno, para interconectar las PSI lo que se hace es conectar las PSI  de acceso a varias PSI de transito globales o ISP de capa superior. SI bien hay lugares donde no hay acceso a una PSI global, por lo cual se crean ISP regionales, las cuales funcionan como puente entre las ISP de acceso de cierta región con las ISP  de transito global. Finalmente tenemos las redes proveedoras de contenido las cuales se conectan a las ISP regionales o de acceso, evitando (dentro de lo posible a las ISP de transito global) con el motivo de reducir pagos a las redes de transito global y para tener control de como sus servicios son entregados a sus usuarios finales. Estas redes proveedoras de contenido pueden ejecutar su propia red para traer servicios y contenido cerca de los usuarios



## Podemos pensar a la Internet como una red formada por niveles de Jerarquía  de 3 niveles

> #### Tier 1 son las ISP comerciales (cobertura nacional e internacional) y las redes proveedoras de contenido

> #### Tier 2 son las ISP regionales

> #### Tier 3 son las ISP de acceso



# ¿Como se conecta el Internet a la argentina?

- **Externo**: Por fibra óptica (red publica que se construyo con ARSAT)

- **Interno:** Por cables submarinos que salen de las toninas y van a Europa, USA y Brazil



Otra forma de ver al internet es como un conjunto de redes de diferentes tamaños que se interconectan entre si para formar redes mas grandes, **de esta forma se puede decir que el internet es la red de redes mas grande** 

###  Tipos de redes:

#### [[Redes de área amplia(WANS)]]

#### [[Redes de área Metropolitana(MAN)]]

#### [[Redes de área Local]]

#### Red Hogareña

#### Redes de Acceso empresarial

#### Redes Dorsales 









