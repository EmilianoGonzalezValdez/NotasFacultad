Un enrutador puede recibir múltiples rutas a mismo prefijo. La mejor ruta a un prefijo debe guardarse en la BIE, pero ¿Cómo escoge el enrutador una de esas rutas al mismo prefijo?

Para ello se usa el siguiente algoritmo para la selección de la mejor ruta BGP entre las rutas que están en adj-RIB-In:
1. **Verificar que el NEXT_HOP es alcanzable:** el NEXT_HOP debe poder resolverse en la tabla de enrutamiento local. Rutas con NEXT_HOP inalcanzable se descartan
2. **LOCAL_PREF:** las rutas con el mayor valor de preferencia local son elegidas. A las rutas se les asigna un *valor de preferencia local* que puede haber sido fijado por el enrutador o aprendido de otro enrutador en el mismo SA (esto lo define el administrador del SA). LOCAL_PREF es un atributo propagado dentro del AS que influye en la selección interna
3. **Longitud del AS_PATH:** de las rutas restantes, la ruta con el camino AS-PATH más corto es elegida (la métrica es la cantidad de saltos SA)
4. **MED:** se prefiere la ruta con el MED más bajo. Por defecto se compara solo entre rutas del mismo AS vecino
5. **Se prefiere la ruta aprendida vía eBGP frente a iBGP**
6. **Costo IGP al NEXT_HOP:** de las rutas restantes la ruta con el enrutador NEXT_HOP más cercano es elegida; o sea, se considera el enrutador NEXT_HOP con el camino más corto determinado por el algoritmo de enrutamiento intra-SA (a esto se lo llama *hot potato routing*)
7. **Ruta mas antigua:** para evitar fluctuasiones, se prefiere la ruta aprendida primero
8. **Router ID del vecino:** se prefiere la ruta aprendida del vecino con el router ID más bajo
9. **Dirección IP del vecino:** se prefiere la ruta aprendida del vecino con la dirección IP más baja