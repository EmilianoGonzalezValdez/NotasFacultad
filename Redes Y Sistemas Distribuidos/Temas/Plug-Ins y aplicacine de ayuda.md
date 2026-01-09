
# Plug-Ins y aplicacine de ayuda



Hay 2 posibilidades para desarrollar **visores:** plug-ins y aplicaciones auxiliares

## Plug-ins

#### ¿Que es un plugin?

Un plug-in es un módulo de código. El navegador obtiene los plug-in de un directorio especial del disco y lo instala como extensión de si mismo. Estos se ejecutan dentro del proceso del navegador. 

A causa de esto los plug-in tienen acceso a la página actual y pueden modificar su apariencia

**Interfaz del plug-in:** Conjunto de procedimientos que todos los plug-in tienen que implementar a fin de que el navegador pueda llamarlos

**Interfaz del navegador:** Conjunto de procedimientos del navegador que el plug-in puede llamar

Una vez que el plug-in ha completado su trabajo se lo elimina de la memoria del navegador



## Aplicaciones auxiliares

Tambien es un modulo de codigo pero estos se ejecutan en un proceso separado del browser. No ofrecen interfaz al navegador ni usan servicios de este. Suelen aceptar el nombre de un archivo, lo abren y despliegan



