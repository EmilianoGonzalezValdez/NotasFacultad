Para el enrutamiento es necesario encontrar álgun camino de SAs para el destino deseado que sea libre de ciclos. Además, los caminos deben respetar las políticas de los SA a lo largo del camino.(Las politicas son reglas que refieren a preferencias de enrutamiento y a limitaciones de enrutamiento)

Los PPEE suelen implementarse sobre *enrutadores de borde de sistema autónomos (EBSA)*. Estos EBSA se encargan de:
- Hacer una elección de varias rutas a un destino.
- Elegir la mejor ruta de acuerdo con sus propias políticas locales y esta va a ser la ruta que avisa
- Avisa a sus vecinos el camino exacto que está usando para cada destino
