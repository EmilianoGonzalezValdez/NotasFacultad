
# Sintaxis

Primero cabe recalcar que un programa no es mas que la descripción de un proceso dinámico siendo del mismo la:

- Sintaxis: El texto del programa

- Semántica: Las cosas que hace el programa

Esto refiere a que podemos tener programas con la misma Semántica, pero distinta Sintaxis. Ejemplos:



```c
int fact (int n) return (n==0)? 1: n*fac(n-1)

  
```



```haskell
fact: integer -> integer
fact 0 = 1
fact n = n * fact(n-1)
```



Donde ambos programas hacen lo mismo, pero su sintaxis es distinta.

La implementación de un lenguaje de programación debe traducir esta sintaxis para que la ejecución del programa sea la que pretendemosa 

Es decir, el lenguaje de programación no es mas que un conjunto de abstracciones y empaquetamientos  del código maquina. Por ende es necesario traducir el lenguaje de programación a código maquina para ejecutarlo

De esta traducción se encarga el [[Compilador]]. Mientras que un interprete traduce y ejecuta al mismo tiempo


