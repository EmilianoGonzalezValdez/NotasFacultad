¿Cómo conviene organizar un SA muy grande?
Para ello vamos a considerar un SA como una red jerárquica. Ya analizamos anteriormente los costos en que se incurre si no se hace esto


**Organización de una SA en OSPF:**
- OPSF divide los SAs en *áreas* numeradas
- *Un área puede contener varias redes adentro de ella*
- Cada enrutador está configurado para conocer qué otros enrutadores están en su área
- Las áreas no se traslapan

**Tipos de áreas en un SA:**
- Hay  un área que es la red dorsal y tiene el número es 0
- Hay áreas que se conectan a la red dorsal. *Se puede entrar desde un área en el SA a cualquier otra área en el SA mediante la red dorsal*
- La topología de la red dorsal no es visible desde fuera de esta

**Clasificación de los enrutadores de un SA:**
- *Enrutadores internos:* yacen completamente dentro de un área
- *Enrutadores dorsales:* enrutadores en un área dorsal
- *Enrutadores de borde de área (EBA)*, son parte de una red dorsal y a la vez de una o más áreas
- *ENrutador de borde de SA (EBSA):* inyecta en el área rutas a destinos externos en otros SA. Ya lo veremos con cuidado cuando estudiemos BGP
