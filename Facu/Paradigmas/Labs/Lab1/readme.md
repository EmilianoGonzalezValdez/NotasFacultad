# Laboratorio 1 Paradigmas
## Integrantes:
  - Cassano Ludmila
  - Gonzalez Valdez Emiliano
  - Olivera Serena
  - Varas Maria Luz

> El objetivo del laboratorio fue implementar un DSL para especificar la composición de dibujos geométricos. He aquí nuestra experiencia relatada:

## Primer paso: Implementar el DSL en Haskell

Para ello tuvimos que modificar dos archivos: Dibujo.hs y Pred.hs

### Dibujo.hs
Aquí definimos la sintaxis de nuestro lenguaje junto con sus funciones.

En si las primeras funciones fueron bastante fáciles de implementar, excepto las funciones mapDib y foldDib que nos dieron un dolor de cabeza en su desarrollo. Sabíamos los conceptos de una función 'map' (aplicar una función a cada elemento) y una 'fold' (devolver un resultado que combina/utiliza todos los elementos de la clase de alguna forma), pero el como se iba a aplicar en las figuras (sobre todo en foldDib) nos era un misterio.
Asustaba que fueran tantos parámetros en este, pero fue precisamente eso lo que nos dió la pista, ya que cada "función" que necesitaba, correspondía con los parámetros del tipo 'Dibujo' que estábamos definiendo. Asumimos que la entenderíamos por completo en su uso posterior, y nos abstraímos de teorías, pudiendo finalmente implementarlas a ambas.

### Pred.hs
El objetivo de este archivo era que dado un predicado, pudiesemos relacionarlo con nuestro dibujo.

El reto aquí fue entender que quería que hicieramos. Estuvimos toda una tarde intentando entender qué era y a qué se refería con 'predicado' hasta que dimos con la iluminación divina.

Por otro lado, ninguno sabía usar lambda notation, e intentamos implementar las cosas sin ella, lo que terminó siendo irónicamente una complicación, y tuvimos que curtirnos y aprender.
Ayudó a no tener que definir tantos auxiliares, y poder utilizar las funciones de mapDib y foldDib a nuestro beneficio! (Finalmente pudimos entender como sacarles provecho)


## Segundo paso: Utilizar el DSL para “expresar o dibujar algo”.

En esta instancia sólo modificamos el archivo **Interp.hs**, y luego para hacer el dibujo de Escher, otros main (desarrollado más adelante)


El interp supone darle una semántica a la sintaxis antes propuesta en Dibujo.hs, de manera que se puedan dar un sentido a nuestras figuras. Para esto debimos de usar la librería Gloss con los tipos 'ImagenFlotante' e 'Interpretación', que dificultaron la implementación de las funciones pues no entendíamos muy bien como funcionaban.

Una vez realizadas algunas pruebas y entendiendo su funcionamiento muy vagamente, simplemente fue cuestión de guiarnos de la consigna del lab. Al principio la implementación no fue la que debería, por lo cual leímos nuevamente la documentación de Gloss descubriendo así, que podíamos manejar los vectores directamente con el "V." dado que antes tomabamos cada vector como una tupla de Float.

Luego basto con leer el main un poco para entender como compilarlo. Al hacerlo logramos dibujar la F al revés, pero el dibujo de Escher aún daba problemas, lo cual fue solucionado tocando un poco las funciones de interp_apilar y interp_juntar de Interp.hs para que fueran interpretadas correctamente.

> Para correr los ejemplos de Escher y Basica doble se deben ejecutar los comandos:
>
> ghci Ejemplos/Main_BasicaDoble.hs
> 
>ghci Ejemplos/Main_Escher.hs
>
>Una vez abierto el interprete se debe escribir: main