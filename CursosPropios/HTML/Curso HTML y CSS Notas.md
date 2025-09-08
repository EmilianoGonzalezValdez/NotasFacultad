# HTML BÁSICO

En si con  **HTML** todo lo que hacemos es una maqueta o arquetipo ideal de nuestra pagina web, la cual normalmente es bastante fea. Con **CSS** lo que hacemos es darle diseño lindo a la misma

## Párrafos y Títulos
```html
<p>
Pepefrog amen salud
</p>

```
Se usan para describir algo sobre el tema que estamos abarcando. Tienen que tener un motivo de dexistencia donde la idea deba empezar y terminar en el mismo


El ```<h1>```se utiliza una sola vez, tiene una importancia muy grande en la búsqueda y posicionamiento web. Es la etiqueta mas importante que le dice a Google de que trata la pagina. Y el ```<h2>  ``` se utiliza mas que nada para los subtitulo

En general los ```<h>'s``` se utilizan para darle orden a las secciones de la pagina en forma jerárquica 


## Tenemos 2 tipos de listas

### Listas ordenadas
Las listas ordenadas se usan con la etiqueta ```<ol>``` de "ordered list". Cada elemento de la lista ordenada responden a la etiqueta de ```<li>``` 
### Listas desordenadas
Las listas ordenadas se usan con la etiqueta ```<ul>``` de "ordered list". Cada elemento de la lista ordenada responden a la etiqueta de ```<li>``` 

#### Uso
El uso de ambas depende totalmente del contexto del que estemos hablando. No es lo mismo star hablando sobre pasos de una receta de cocina que de un top 10 juegos de 2025


## Enlaces

Para utilizar un enlace debemos usar la etiqueta ```<a href=" link "> con esto nos vamos a tal lugar </a>``` donde apuntamos al link marcado por href, pero el texto que aparece en la pagina web es el encapsulado en el bloque entre las etiquetas. Podemos definir como queremos abrir el link provisto, puede ser en la misma pagina con ```target = _self``` o en otra pagina con ```target = _blank```. Estos son solo 2 opciones, realmente hay 4 donce la predeterminada es ```target = _self```.

### Características extras o comunes
EL ```title = "descripcion de la etiqueta" ``` sirve para poner una descripción emergente en la etiqueta donde lo estamos poniendo

## Etiqueta de bloque vs Etiqueta de Lineas

## Imágenes
Usamos la etiqueta ```<img src= "donde anda", alt ="upa">``` donde src me dice de donde sacar la foto, es decir, la ruta hacia la imagen y alt viene de alternative, es el mensaje que saldrá en caso que no se encuentre la imagen 


## Formularios
Usamos la etiqueta  ```<form>``` para abrir un formulario. Luego debemos aclarar el tipo de input que esperamos. Tenemos 4 atributos muy importantes para los inputs.
	1. Required -> ==Hace que el campo sea obligatorio== 
	2. Name -> ==Dice como se va a llamar el dato enviado(sirve para que el servidor sepa de que hablamos). Son identificadores==
	3. Placeholder -> ==Escribe un pequeño texto que se borra cuando empieza a escribir el usuario== 
	4. Value -> ==Sirve si queremos acceder a lo que el usuario escribió==

#### Otros atributos que suman a los anteriores
	1.Min -> da un tamaño minimo al input


# CSS Básico 

Los cambios de realizan en cascada normalmente, pero hay varias formas de seleccionar objetos. Primero que anda hay que separar entre atributo y propiedad. 
- Los atributos se acceden mediante HTML
- Las propiedades se acceden mediante CSS


Los *Estilos en linea* te deja cambiar las propiedades de un objeto HTML en la misma linea de su declaración. Esto no se hace ya que se mezcla todo el código. EN vez de eso se modifican las propiedades mediante un bloque llamado ```<style>```. Pero se realiza en otro archivo utilizando otra etiqueta llamada ```<link rel = "stylesheets">```

> [!NOTE] Que le estamos diciendo?
> Bueno pues lo que queremos decir con esa etiqueta es que me linkee, otro archivo con una relación de sylesheets, es decir que el nuevo archivo servirá para darle estilo al archivo actual


En este nuevo archivo primero elegimos un selector(elegimos el elemento a modificar). Luego empezamos a declarar las propiedades que queremos modificar dandole valores a nuestro gusto

## Selectores

**Selección por elemento** -> busca un elemento HTML por su nombre de etiqueta y cambia las propiedades a todos los elementos con dicho nombre
**Selección por clase** -> Creamos una class = "ClaseDicha" para hacer una plantilla en el archivo .css en la que podemos personalizarla a nuestro gusto
**Selección por id** -> Solo puede haber un elemento con un ID en toda la pagina web

## Propiedades de Texto

1. Color -> Hace lo que dice
2. font-family -> Cambia la tipografía. Podemos poner mas font separados con comas ( , ) para decir que si no encuentra la primera cargue la 2da
3. font-size -> cambia el tamaño de la letra
4. font-weight -> Cambia el ancho de la tipografía dependiendo de cual elegimos
5. font-style -> Pone estilos a la tipografía como cursiva por ejemplo
6. text-align -> alinea texto de tal manera 
7. text-decoration -> 🤓
8. line-height -> Interlineado 
9. letter-spacing -> espacio entre letras
10. text-shadow 

## Tipografías externas
Podemos descargar tipografías desde google fonts y vincularlas en nuestro archivo HTML. La otra forma de hacerlo es crear otro archivo para configurar nuestras propias tipografías