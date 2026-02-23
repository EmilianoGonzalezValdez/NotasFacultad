Las **politicas en BGP** son reglas que controlan cómo se aceptan, modifican y anuncian las rutan entre vecinos.
En conjunto, estas políticas permiten controlar el flujo de información de enrutamiento, optimizar rutas, evitar bucles, cumplir acuerdos comerciales y mantener la estabilidad y seguridad de la red

**Clasificación de las políticas BGP:**
- *Politicas de entrada:* se aplican a las rutas recibidas de un vecino BGP antes de almacenarlas en la tabla local (Loc-RIB). Su función es:
-  Filtrar rutas no deseadas:(bloquear prefijos o rutas con ciertos atributos, por ejemplo, rechazar prefijos con AS-PATH que incluye AS no confiables)
-  Modificar atributos para influir en la selección de ruta (por ejemplo, incrementar el atributo LOCAL_PREF para dar preferencia a ciertas rutas recibidas de un vecino sobre otras)
-  Clasificar rutas mediante comunidades para aplicar reglas internas
- *Políticas de salida:* se aplican a las rutas que el enrutador va a anunciar a sus vecinos. Sirven para:
-  Filtrar rutas que no se desean enviar a ciertos vecinos
-  Modificar atributos como AS_PATH: añadir el ASN local al ASN_PATH antes de anunciar rutas a un vecino externo co,o para evitar bucles y cumplir con las reglas BGP
-  Controlar anuncios mediante comunidades para segmentar el comportamiento según acuerdos o topología
