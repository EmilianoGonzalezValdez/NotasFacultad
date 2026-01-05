
# Evaluación de una consulta del álgebra de tablas 

Para procesar una consulta SQL, esta se puede ==traducir== a una expresión del álgebra de tablas. Luego se puede evaluar dicha consulta en términos de operadores físicos.

Una expresión del álgebra de tablas puede tener varias expresiones equivalentes. Lo cual implica que puede haber expresiones equivalentes que sean mejor que otras, por lo cual nos indica que si tenemos una consulta $Q$, puede haber una consulta $K$ equivalente a la primera la cual nos convenga mas evaluar en lugar de $Q$.
Entonces dada una consulta $C$ del álgebra de tablas, un **plan de evaluación** consiste de una expresión $E$ equivalente a $C$ y operadores físicos para los operadores lógicos de $E$.
Luego la **maquina de ejecución de consultas** toma el *plan de evaluación* de la consulta, ejecuta dicho plan y retorna las respuestas de la consulta.

Los diferentes planes de evaluación para una consulta dada pueden tener diferentes costos. El encargado de construir un plan de evaluación que minimice el costo de la evaluación de la consulta debería ser el SGBD. 

Luego existen los *optimizadores de consultas*, los cuales encuentran el plan de evaluación con menor costo entre todos los equivalentes, a esto se lo llama **optimización de consultas**. Pero para ello los optimizadores deben conocer el **costo de cada operación**.

El **árbol binario de ejecución** de una consulta es el árbol binario de una expresión de consulta donde los nodos hoja son tablas de la base de datos y los nodos internos son operadores del álgebra de tablas. Como para cada consulta tengo muchas expresiones equivalentes las cuales cada una tiene un árbol de ejecución distinto, la evaluación de un árbol binario de ejecución va a estar en términos de operadores físicos

![[EjemploArbolBinarioEjecucion.png]]


Los resultados de evaluar un operador de un nodo interno se les llama **resultados intermedios**.
Para la evaluación de uno de estos árboles hay 2 enfoques:
- **Materialización:** donde los resultados intermedios se guardan en disco en tablas temporales a las cuales tiene acceso el SGBD
- **Encausamiento:** donde a medida que se van generando los resultados intermedios se van pasando al siguiente operador (los resultados intermedios nos e guardan en disco)

La *materialización* usa mucho menos memoria principal y claramente mas espacio en disco, mientras que encausamiento usa menos espacio en disco y bastante mas memoria principal 


El ejemplo de la imagen anterior, si elegimos utilizar materialización los apsso a realizar serian los siguientes:
1. Computamos y almacenamos en disco primero a $\sigma_{\text{building} \space =\space \text{"Watson"}}(department)$ 
2. Computamos y almacenamos en disco la reunion natural del resultado intermedio anterior con la tabla $instructor$ 
3. Computamos la proyección $\prod{name}$ 

> [!important]- Con materialización:
>  - Cambiar nodos lógicos por físicos en el árbol binario de ejecución.-
>  - Si hay más de un operador físico posible, elegir el menos costoso. 
>  - Evaluamos un operador físico por vez comenzando en el nivel más bajo. 
>  - Usamos resultados intermedios en tablas temporales para evaluar los operadores físicos del siguiente nivel.

Para poder **optimizar una consulta** es necesario *elegir un buen plan de ejecución* (este seria un árbol binario de ejecución junto a los operadores físicos).
Para poder **elegir entre varios planes de ejecución** es necesario tener los costos de cada uno.
Por ende hay que poder **evaluar el costo** de un plan de ejecución usando materialización

***Para calcular el costo de evaluar un árbol binario de ejecución usando materialización vamos a necesitar comprender:*** 
- Cómo estimar el tamaño de un registro de una tabla de bytes
- Cómo estimar el tamaño del resultado de un operador físico en cantidad de tuplas
- Cómo estimar el tamaño en bloques del resultado de un operador físico si tenemos una estimación de la cantidad de tuplas del mismo
- Cómo estimar la cantidad de claves de búsqueda en un nodo de índice de un árbol B+

###### Estimación del tamaño de un registro de una tabla de bytes:
- Asumimos que tenemos el esquema de la tabla
- Primero estimamos el **costo de cada atributo** de la tabla de bytes
- Para una organización de archivo secuencial, en cada fila de registro hay que contar también el **tamaño en bytes de un puntero** a disco (suelen ser 8 bytes para un SO con direccionamiento de 64 bits)
- Para calcular el tamaño de una fila de bytes de un archivo secuencial se suman los tamaños de los atributos de una tupla + el tamaño del puntero a disco 

###### Estimación del tamaño del resultado de un operador físico en cantidad de tuplas:
- La proyección tiene la misma cantidad de tuplas que la tabla a la que se aplica
- El producto cartesiano $r \times s$ tiene tamaño $|r\times s1 = |r| \cdot |s|$ registros
- La ordenación de una tabla preserva la cantidad de tuplas en el resultado 
- La concatenación de tablas  $r\space \text{++}\space s$   tiene tamaño $r\space \text{++}\space s = |r| + |s|$ 
- Se proveen cotas superiores para las estimaciones de las cantidades de tuplas de los siguientes operadores: 
	- Para $r \cap s = min(|r|,|s|)$ 
	- Para $r-s = |r|$
	- Para $V(r)=|r|$

###### Tamaño de resultado intermedio de operador físico de selección

Para la selección y la reunión selectiva se nos complica la cosa por la misma naturalidad de estos.
Para la selección se utilizara una función de probabilidad llamada **factor de selectividad** para calcular la cantidad de registros del resultado del operador físico. Luego a partir de la cantidad de registros, calcular la cantidad de bloques del resultado intermedio.
Supongamos que el operador de selección usa un predicado $P$ y el input del operador es $r$, denotamos al factor de selectividad mediante $fs(P,r)$ 
Entonces podemos calcular la cantidad de registros del resultado intermedio = $|r| \cdot fs(P,r)$ donde $|r|$ es la cantidad de registros de $r$.
Una forma de calcular el *factor de selectividad* es asumir **uniformidad e independencia** donde:
- **Uniformidad:** todos los valores de un atributo son igualmente probables(recordamiento de Probabilidad y Estadística, si tengo $N$ elementos equiprobables, su probabilidad es $1/N$ como en un dado)
- **Independencia:** condiciones sobre diferentes atributos son independientes 

###### Factor de selectividad para la selección 
> [!danger]- Creo que Durán esta mal de la cabeza, pero el dejo esto]
> Teniendo esto en claro vamos a ver un par de reglas para el factor de selectividad asumiendo $r$ una tabla, $A,A'$ atributos de $r$ y $c,c'$ constantes:
> - Regla 1: Asumiendo uniformidad:
> 	- $fs(A==c,r)=1/{V(A,r)}$ donde $V(A,r)$ es el número de distintos valores que aparecen en $r$ para $A$
> - Regla 2: Asumiendo uniformidad, $A$ con valor numérico(usando valores consecutivos):
> 	- $fs(A\ge c,r)=(\max (A,r)-c)/{(\max(A,r)-\min(A,r))}$ 
> - Regla 3:
> 	- Asumiendo uniformidad, $A$ con valor numérico:
> 		- $fs(A < c,r)=(c-\min(A))/{(\max(A)-\min(A)+1)}$ 
> - Regla 4: Asumiendo uniformidad, $A$ con valor numérico:
> 	- $fs(c \le A < c',r)=(c'-c)/{(\max(A,r)-\min(A,r))}$ 
> - Regla 5: Asumiendo independencia:
> 	- $fs(P1\wedge P2 \wedge ... \wedge PN,r)=fs(P1,r)\cdot fs(P2,r)\cdot ...\cdot fs(PN,r)$  
> - Regla 6: Asumiendo propiedad de probabilidades: (de que carajo habla duran GAGA)
> 	- $fs(\neg P,r)=1-fs(P,r)$ 
> - Regla 7: Asumiendo independencia (duran ya estaba GAGA acá):
> 	- $fs(P \vee Q,r)= 1-((1-fs(P,r))*(1-fs(Q,r)))$

- Ejemplo: atributo sexo de persona: todos los valores de sexo son igualmente probables (la proporción de hombres es igual a la proporción de mujeres). 
	- $fs(sexo = {'F'}, persona) = 1/2$
- Ejemplo: Atributos sexo y edad en persona, con predicado: 
	- edad == 40 && sexo == ‘F’. 
	- La edad es independiente del sexo. 
$fs(edad == 40 \wedge sexo == ‘F’, persona) = fs(edad == 40, persona) * fs(sexo == ‘F’, persona)$
Pero no es obligatorio usar uniformidad o independencia para calcular el factor de selectividad.

###### Tamaño de resultado de operador físico de reunión
 Para la reunión tomaremos el mismo principio que tomamos para la selección, es decir que también usaremos **factor de selectividad**
Entonces tenemos que la cantidad de tuplas del resultado de la reunión viene dada por $|r| * |s| *fs(P,r,s)$ 

###### Factor se selectividad para reunión selectiva
Si $r$ es una tabla y $A$ una tributo, entonces $V(A,r)$ es el número de distintos valores que aparecen en $r$ para $A$.

Asumiendo uniformidad tenemos que: $$fs(r.A==s.B,r,s)=\frac{1}{\max(V(A,r),V(B,s))}$$
donde uniformidad significa que para cada atributo A/B en una tabla hay la misma cantidad de tuplas por el atributo B/A que cazan en la otra tabla

Para la reunión también tenemos un par de observaciones:
- Regla 1: Si $A$ es clave candidata de $r$: $fs(r.A == s.B,r,s) = 1/\max(|r|,V(B,s))$ 
- Regla 2: Si $B$ es clave foránea en $s$ referenciando a r: $fs(r.a==s.b,r,s)=1/|r|$ 
- Regla 3: Si toda tupla en $r$ produce tuplas en la reunión selectiva: $fs(r.A == s.B)=1/{V(B,s)}$ 
- Si se puede asumir independencia: $fs(r.A == s.B \wedge r.A’ = s.B’, r, s =s(r.A = s.B , r, s) * fs(r.A’ = s.B’, r, s)$ 



###### Cálculo de número de bloques
Para calcular el número de bloques si tengo $N$ registros de tamaño $R$, y $B$ es el tamaño del bloque debemos calcular: **$\text{NumBloques:}=\lceil \frac{(N \cdot R)}{B}\rceil$** 

###### Cálculo de estimaciones 

Veremos como estimar la cantidad de claves de búsqueda en un nodo de árbol B+.
Si tenemos que en un bloque de $C$ bytes entran $n$ claves de búsqueda, entonces tenemos la siguiente ecuación: $C=n * TCB + (n+1)*8$ donde $TCB$ es el tamaño de clave de búsqueda en bytes
- Recordar que en un nodo de árbol B+ de $n$ claves de búsqueda hay $n+1$ punteros de 8 Bytes (en sistemas de 64 bits)
- Despejando esta ecuación tenemos que $$n=\frac{(C-8)}{(TCB+8)}$$ 
***Ahora vamos a ver cómo procesar y estimar el costo de una consulta con materialización***
- **Fase 1: Decidir el plan de ejecución** 
	- Armar el árbol binario de ejecución
	- Calcular el factor de selectividad para selecciones y reuniones([[#Factor se selectividad para reunión selectiva]],[[#Factor de selectividad para la selección]])
	- Decidir los operadores físicos más eficientes (solo se usan índices si la tabla lo amerita)

![[EjemploFase1DecidirPlanDeEjecución.png]]

- **Fase 2: Estimar el costo de ejecutar el plan de evaluación**
	- Calcular el tamaño en bloques de las tablas de la BD(Primero calcular el tamaño en bytes de una tabla,[[#Estimación del tamaño de un registro de una tabla de bytes]] y luego dividir ese tamaño por el tamaño de bloque)
	- Calcular el tamaño de los resultados intermedios primero en cantidad de tuplas y luego en cantidad de bloques
		- Para casi todos los operadores: [[#Estimación del tamaño del resultado de un operador físico en cantidad de tuplas]]
		- Para Selección: [[#Tamaño de resultado intermedio de operador físico de selección]]
		- Para reunión: [[#Tamaño de resultado de operador físico de reunión]]
	- Calcular el costo de los operadores físicos
	- Sumar los costos totales: $\sum{costo(operaciones)} + \sum{costo(materializacion)}$(en el ejemplo los azules son los costos de operaciones y los amarillos los de la materialización) 
- Aplicar el método de dos fases

![[EjemploFase2EstimarCostoEjecutarPlanEvaluacion.png]]



# Optimización de consultas 

***Pasos en optimización de consultas basada en costos:***
1. Generar expresiones lógicamente equivalente usando **reglas de equivalencia**
2. Anotar expresiones resultantes con operadores físicos para obtener **planes de evaluación alternativos**
3. Elegir el plan de evaluación mas económico basado en el **costo estimado**

###### Transformación de expresiones de consulta

- Dos expresiones de álgebra de tablas son **equivalentes por igualdad** si las dos tablas del resultado son equivalentes en esquema e información 
- Dos expresiones son **equivalentes módulo ordenamiento de registros** si las dos expresiones generan el mismo multiconjunto de tuplas(las mismas tuplas en la misma cantidad para cada tupla)
- Una **regla de equivalencia** dice que las expresiones de dos formas son equivalentes usando uno de os tipos de equivalencia de arriba

###### Reglas de equivalencia 
1. La selección conjuntiva de operaciones puede ser deconstruida en una secuencia de selecciones individuales: $$\sigma_{\theta_1\blacksquare\theta_2}(E)=\sigma_{\theta_1}(\sigma_{\theta_2}(E))$$
2. Las operaciones de selección son conmutativas: $$\sigma_{\theta_1}(\sigma_{\theta_2}(E))=\sigma_{\theta_2}(\sigma_{\theta_1}(E))$$
3. Solo la última proyección en una secuencia de estas es necesitada:$$\prod{L_{1}}( \prod{L_2}(\dots(\prod{L_n(E)})))=\prod{L_{1}}(E)$$
Ahora usaremos $\theta_{r}^N$ para indicar una lista de $N$ columnas de la tabla $r$ e indicaremos con $p_r$ a una proposición que sólo utilice columnas de $r$

4. La reunión natural es asociativa: $$(E_1 \bowtie E_2) \bowtie E_3 = E_1 \bowtie (E_2 \bowtie E_3)$$
5. La siguiente regla es parecida a la definición de reunión: $$E_1 \bowtie_\theta E_2 = \sigma_\theta(E_1 \times E_2)$$
6. La siguiente regla muestra cómo podemos expresar una selección de una reunión selectiva por medio de una reunión selectiva: $$\sigma_P(E_1 \bowtie_\theta E_2) = E_1 \bowtie_{\theta \land P} E_2$$
7. La siguiente regla nos permite aplicar selección antes de reunión selectiva: $$\sigma_{P_1}(E_1 \bowtie_\theta E_2) = \sigma_{P_1}(E_1) \bowtie_\theta E_2$$
8. La siguiente regla se deduce de reglas previas: $$\sigma_{P_1 \land P_2}(E_1 \bowtie_\theta E_2) = \sigma_{P_1}(E_1) \bowtie_\theta \sigma_{P_2}(E_2)$$
9. La siguiente regla muestra como se comporta la proyección cuando se usa junto con la reunión selectiva: $$\Pi_L(E_1 \bowtie_\theta E_2) = \Pi_L(\Pi_{L_1}(E_1) \bowtie_\theta \Pi_{L_2}(E_2))$$
10. La concatenación "conmuta" alterando solo el orden de las tuplas:$$r ++ s =_O s ++ r$$
11. La concatenación es asociativa:$$(r ++ s) ++ t = r ++ (s ++ t)$$
12. La selección distribuye con concatenación, intersección y resta:$$\sigma_P(E_1 \ \mathbf{{++ / \cap / - }}\ E_2) = \sigma_P(E_1) \ \mathbf{{++ / \cap / - }}\ \sigma_P(E_2)$$
13. La siguiente propiedad es más débil que la anterior
14. La proyección distribuye con la concatenación:$$\Pi_L(E_1 ++ E_2) = \Pi_L(E_1) ++ \Pi_L(E_2)$$
15. Eliminación de duplicados distribuye con reunión natural:$$\nu(r \bowtie s) = \nu(r) \bowtie \nu(s)$$
16. Eliminación de duplicados conmuta con selección:$$\nu(\sigma_P (r)) = \sigma_P (\nu(r))$$
###### Empujando selecciones

> [!IMPORTANT] Realizar la selección tan temprano como sea posible reduce el tamaño de la tabla a ser combinada 

###### Optimización Heurística

El problema es que la optimización basada en costo es cara, ya que el número de diferentes planes de ejecución para la misma consulta puede ser muy grande y encontrar el plan optimo requiere mucho esfuerzo computacional

Una **Heurística** es una técnica que aplica reglas generales o atajos para transformar una consulta en una consulta más eficiente (también se la puede llamar la estrategia del pulgar)

Entonces en vez de usar la optimización basada en costos así nomas, los sistemas pueden usar heurísticas para reducir el número de elecciones que deben ser hechas cuando se trabaja con costos. La **optimización heurística** transforma el árbol de consulta usando un conjunto de reglas que típicamente pero no siempre mejoran el desempeño de ejecución
La mayoría de los optimizadores incluyen **heurísticas** para reducir el costo de las optimizaciones de consultas, con el riesgo potencial de no encontrar un plan óptimo 

***Ejemplo de optimización heurística:***
- **Realizar selección tempranamente:**(reduce el número de tuplas)
	- Empujar selección abajo en el árbol de ejecución tanto como sea posible
- **Realizar el proyección temprano:**(Reduce el número de atributos y por ende el tamaño de un resultado intermedio)
- **Hacer la selección más restrictiva:**(i.e. con tamaño de resultado menor) antes de hacer las otras selecciones
- **Hacer operaciones de reunión más restrictivas**
- **Ciertas selecciones pueden ser combinadas con producto cartesiano abajo para tornar las operaciones de una reunión**

![[EjemploOptimizacónHeurística.png]]


###### Selección de orden de reunión basado en costo

Si tengo una reunión natural/selectiva de varias tablas, la optimización basada en costo es demasiado costosa, la razón es la gran cantidad de casos a examinar.
Con n tablas hay $(2(n-1))!/(n-1)!\space \text{diferentes ordenaciones}$  
*Observación:* los distintos ordenes pueden cambiar también el orden de las columnas. Pero podemos proyectar según los atributos de la expresión original de la consulta para que eso no suceda 

Para la selección de orden de reunión natura basado en costo hay **algoritmos de programación dinámica**, los cuales en vez de generar todas las expresiones de reunión posibles, se consideran conjuntos de relaciones a reunir y optimizar, los cuales se usan en tablas(como índices para las mismas). Usando **programación dinámica** el orden de reunión de menor costo para cada subconjunto de {$r_1,...,r_n$} es computado solo una vez y almacenado para uso futuro


> [!NOTE]- Ejemplo
> Si hay 4 tablas tenemos en total:
> - $\frac{(2*3)!}{3!} =120 \space \text{casos}$
> - Sin embargo la cantidad de subconjuntos de 4 elementos es 16. Por ende programación dinámica trabaja con tablas de 16 subconjuntos

***Solución usando programación dinámica:***
Construimos una tabla con una entrada para cada subconjunto de una o más de las tablas de la reunión.
En dicha tabla ponemos:
- Un índice que es un conjunto de tablas de la base de datos
- En cada celda:
	- El menor costo de computar la reunión de esas tablas(en cantidad de tuplas)
	- El tamaño estimado de la reunión de esas tablas(cantidad de registros)
	- La expresión que da lugar al menor costo
La construcción de esta tabla se hace por **inducción** en el *tamaño del subconjunto*

***Caso Base:***
- La entrada para una sola tabla $r$ consiste del tamaño de $r$, un costo 0 y la expresión que es $r$
- La entrada para un par de tablas {$r_i,r_j$}
	- Tiene estimación de tamaño igual al producto de tamaños de $r_i \text{y} \space r_j$ multiplicado por el factor de selectividad
	- Tiene costo 0 porque no hay tablas intermedias involucradas(es como asumir que las tablas de la BD están en memoria)
	- Además, tomamos la menor de $r_i$ y $r_j$ como el argumento izquierdo e la expresión de la reunión natural

***Caso inductivo:***
- Consideramos todas las maneras de particionas el conjunto actual de tablas $S$ en dos subconjuntos $S_1$ y $S_2$
- Para cada una de estas maneras consideramos la suma de:
	- Los mejores costos de $S_1$ y $S_2$
	- Los tamaños para los resultados de $S_1$ y $S_2$
- Sea cual sea la partición que da el mejor costo, usamos esta suma como el costo de $S$
- La expresión de $S$ es la reunión natural de las mejores expresiones para $S_1$ y $S_2$ 

**Solución alternativa:** Podemos modificar el algoritmo anterior para tomar en cuenta algoritmos de reunión natural. Cuando se computa el costo de $S_1 \bowtie S_2$ sumamos el costo de $S_1$, el costo de $S_2$ y el menor costo de juntar los dos resultados usando el mejor algoritmo disponible

La complejidad en tiempo del procedimiento es $O(3^n)$ y su complejidad en espacio es de $O(2^n) - \text{cantidad de subconjuntos de n elementos}$ 


###### Árboles de reunión profunda a la izquierda

En árboles de reunión profunda a la izquierda el lado derecho de cada reunión natural es una tabla, no el resultado de una reunión intermedia

***Para encontrar el mejor árbol de reunión profunda a la izquierda para un conjunto de n tablas:***
- Paso inductivo:
	- Si $S$ tiene $k$ tablas, para cada $r$ en $S$, primero computamos la reunión de $S-\{r\}$ y luego hacemos la reunión natural con $r$ 
	- La expresión de reunión para $S$ tiene la mejor expresión de reunión para $S-\{r\}$ como argumento izquierdo de la reunión final y $r$ como el argumento derecho
	- El costo de la reunión de $S$ es el costo de $S-\{r\}$ más el tamaño del resultado para $S-\{r\}$. Tomamos el $r$ que da el menor costo
	- El tamaño de $S$ se calcula por la fórmula que usa factor de selectividad 

**Complejidad:** Si esos árboles de reunión profunda a la izquierda son considerados, el tiempo de complejidad para encontrar el mejor orden de reunión es $O(n2^n)$. La complejidad del espacio permanece en $O(2^n)$ 


###### Enfoques híbridos:

Algunos sistemas gestores de BD combinan heurísticas con optimización parcial basada en costo. Enfoques de optimización de consultas que aplican elecciones heurísticas de plan para algunas partes de la consulta con elección basada en costo basada en la generación de planes alternativos para otras partes de la consulta han sido adoptados en varios SGBD

# Retorno de la información

El **retorno de la información** es el proceso de retornar documentos a partir de una colección de documentos en respuesta a una consulta(dichos documentos suelen estar en lenguaje natural)
La **información no es estructurada:**
- No tiene modelo formal bien definido
- Se basa en la comprensión del lenguaje natural
- Se almacena en una variedad amplia de formatos estándares

***Diferencias entre BD relacional y retorno de la información***


| **Bases de datos relacionales**                                           | **Sistema de retorno de la información**                                       |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Datos estructurados                                                       | Datos no son estructurados                                                     |
| Dirigidos por esquemas relacionales                                       | No hay esquemas fijos                                                          |
| Operaciones sobre metadatos                                               | Operaciones sobre datos                                                        |
| Las consultas retornan datos                                              | Las búsquedas retornan una lista de punteros a documentos                      |
| Los resultados se basan en correspondencia exacta y son siempre correctos | Los resultados se basan en correspondencia aproximada y medidas de efectividad |
| Trabajan con transacciones                                                | No trabajan con transacciones                                                  |

###### Lenguajes de consulta


Los sistemas de  retorno de información típicamente permiten **expresiones de consulta** formadas usando palabras clave y conectivos proposicionales. Algunos ejemplos:
- Consultas usando frases: Una frase es una secuencia de palabras
- Consultas de palabras clave: Se escribe texto de palabras clave y se asume AND entre esas palabras
- Consulta Booleanas: Las expresiones involucran términos y conectivos booleanos
- Consultas basadas en expresiones regulares: Se usan expresiones regulares y búsqueda basada en correspondencia de patrones
- Consultas de proximidad: Se expresa cuan cerca deben estar entre sí ciertos términos. En algunos casos se pide respetar el orden de las palabras
- Consulta en lenguaje natural: La consulta es texto en lenguaje natural

###### Resultados de una consulta

Los **resultados de una búsqueda** pueden ser una lista de identificadores de documentos y también algunas piezas de texto. Los documentos suelen retornarse en orden decreciente de puntaje de relevancia.
Por ello es necesario definir *cuando un documento es más relevante que otro*, la idea es medir que tanto un documento satisface la necesidad de información del usuario. Esta medición puede ser binaria o graduada

También podemos pensar en la **relevancia de términos** par definir que tan importantes son ciertos términos dentro de un documento o consulta. Por ejemplo:
- Frecuencia de términos: frecuencia de ocurrencia de un término de una consulta en un documento
- Frecuencia inversa de documentos: ¿En cuantos documentos ocurre la palabra?

Para la mayoría de los sistemas de retorno de información las palabras que ocurren en el título, lista de autores, título se les da mas importancia. Mientras que las palabras cuya primera ocurrencia es tarde en el documento se les da poca importancia  

###### Enfoques estadísticos

Un SRI al procesar una consulta no accede directamente a los documentos, sino que se usa una representación de cada documento( se construye para cada documento una estructura que resume lo que contiene).
En un **enfoque estadístico** los documentos son analizados y descompuestos en piezas que pueden ser palabras, frases, n-gramas, etc. Donde cada pieza se la cuenta, pesa y mide para determinar su relevancia e importancia. Luego dada una consulta se comparan los términos de esta con las piezas para determinar un *grado potencial de correspondencia* y para producir una *lista ordenada de documentos resultantes* 

Ejemplos de enfoques estadísticos:
- **Modelo Booleano:**
	- Los documentos se representan como conjunto de términos
	- Se usan consultas booleanas
	- Los documentos retornados son una correspondencia exacta
	- No hay noción de ordenar los documentos por relevancia 
- **Modelo de espacio vectorial:**
	- Cada documento se representa con un **vector de pares** de dimensión $n$ 
	- Cada término corresponde con una *dimensión*
	- Para cada dimensión del vector además del término hay un número que puede representar la presencia del término en el documento o la frecuencia del término en el documento(esto ultimo usando TF-IDF)
	- Se puede computar la **similitud de dos vectores** mediante una *función*
	- Una consulta también se representa como un vector de términos
	- Se puede establecer la **medida de relevancia** de un documento con respecto a una consulta(se compara el *vector de una consulta* con los vectores de los documentos para *estimación de similitud/relevancia*)
	- Las respuestas a una consulta se ordenan por relevancia 
	- Los términos tienen peso en los vectores de pares. Este peso puede ser la *frecuencia*  de cada termino en el documento o se puede usar **TD-IDF**(frecuencia de término-frecuencia inversa de documento), cuya formula se descompone en: $$TF-IDF_{i,j}=TF_{i,j}*IDF_i$$ $$TF_{i,j}=\frac{f_{i,j}}{\sum_{i=1 \to |V|}f_{i,j}}$$ $$IDF_i=log(\frac{N}{n_i})$$
		- Donde $TF_{i,j}$ es la frecuencia del término $i$ en el documento $D_j$ normalizada
		- $f_{i,j}$ es la cantidad de ocurrencias del término $i$ en el documento $D_j$
		- $N$ es el número de documentos en la colección
		- $n_i$ es el número de documentos donde el término $i$ ocurre 
	- También podemos calcular la *relevancia de un documento* $D_j$ con respecto a una consulta $Q$ de la siguiente manera: $$rel(D_j,Q)=\sum_{i \in Q}TF_{ij}\times IDF_i$$
	- Se usa la siguiente **función de similitud de vectores** para calcular la similitud entre el vector de una consulta y el vector de un documento (función coseno del ángulo entre los vectores de la consulta y el documento): $$cosine(d_j,q)=\frac {\langle d_j \times q \rangle}{||d_j|| \times ||q||} = \frac{\sum_{i=1}^{|V|}w_{ij} \times w_{iq}}{\sqrt{\sum_{i=1}^{|V|}w^2_{ij}}\times \sqrt{\sum_{i=1}^{|V|}w^2_{iq}}}$$
		- Donde $d_j$ es el vector del documento $j,q$ es el vector de la consulta 
		- $W_{i,j}$ es el peso del término $i$ en el documento $j$, $w_{i,q}$ es el peso del término $i$ en el vector de la consulta $q$ 
		- $|V|$ es el número de dimensiones en el vector
	- ***Interpretación del resultado de la función de similitud de vectores:***
		- Si el resultado es cercano a 1, significa que los vectores son muy similares
		- Si el resultado es cercano a 0, los vectores no tienen casi nada en común
		- Si el resultado es -1, entonces los vectores son opuestos


###### Selección de términos relevantes de un documento 

Antes de construir la representación de un documento es importante *encontrar los términos relevantes*, para ello hace falta **prepocesar los documentos de la colección** para encontrar los términos relevantes. No todos los términos son relevantes, por ejemplo:
- Existen las **stopwords**, que son palabras que se espera que ocurran el 80% o más de los documentos de la colección
- A veces un término aparece de muchas maneras y no vale la pena tener todas sus variantes(como un mismo verbo conjugado de muchas maneras)
- O aparecen **sinónimos de un término**, para esto, una forma de tratar esta situación es con la **expansión de la consulta**, en la cual se agregan automáticamente sinónimos relacionados a la consulta del usuario(si por ejemplo la consulta dice mantenimiento de motos, y en el documento existe reparación de motos, el sistema podría extender la consulta a reparación OR mantenimiento)
	- **WordNet:** agrupa las palabras en conjuntos de sinónimos llamados **synsets**, estos se dividen en categorías: sustantivo, verbo, adjetivo y adverbio. Dentro de cada categoría estos se organizan usando relaciones clase/subclase (o ES)
	- No es tan simple, pues para seleccionar sinónimos correctos de una palabra, hace falta identificar de cual de los significados de esa palabra se trata, él cual muchas veces, va a depender del contexto
	- Para ello los sistemas más avanzados deben aplicar **técnicas de desambiguación de sentido de palabra**, los cuales analizan en contexto en que aparece la palabra para determinar cual sentido y por ende conjunto de sinónimos es el apropiado
	- Otra idea es usar representaciones vectoriales de las palabras, donde términos similares están próximos en el espacio vectorial
- **El uso de sinónimos en SRI tiene varias ventajas significativas**
	- *Mejora la precisión:* Los SRI pueden entender mejor la intención del usuario y ofrecer resultados más relevantes, incluso si las palabras exactas no coinciden 
	- *Aumento de cobertura:* Permite encontrar información que usa diferentes términos para referirse a lo mismo, asegurando que no se descarten documentos importantes
	- *Experiencia del usuario optimizada:* Los usuarios no tienen que adivinar el término exacto que se usó en los documentos, lo que facilita y agiliza la búsqueda de información 
- A veces interesa buscar entidades en lugar de términos(ejemplos: fecha y hora, relaciones, nombres de personas, nombres de organizaciones ,etc.)
	- Un **sistema de reconocimiento de entidades nombradas** identifica y clasifica automáticamente estos nombres, facilitando búsquedas y extracción de información.
		- Primero el texto se divide en tokens(palabras y signos de puntuación)
		- Luego se detectan posibles entidades 
		- Las entidades se clasifican en categorías predefinidas
		- El sistema considera el contexto para desambiguar significados y mejorar precisión 
		- Se extrae contenido estructurado a partir de texto
- **Técnicas empleadas por un sistema de reconocimiento de entidades nombradas:** 
	- *Métodos basados en reglas:* usan expresiones regulares, patrones lingüísticos, diccionarios o listas de entidades conocidas
	- *Métodos estadísticos:* que aprenden a partir de datos etiquetados para predecir entidades en textos
	- *Modelos de aprendizaje profundo:* que capturan contextos complejos a nivel de palabra y oración para identificar y clasificar entidades con alta precisión
- El retorno de entidades es muy útil para:
	- Mejorar la precisión de las búsquedas
	- Agrupar información relacionada


###### Índices invertidos

Una estructura de datos de **índice invertido** puede tener para término los identificadores de los documentos donde aparece el término y también puede tener las posiciones en el documento donde aparece el término. La lista invertida de un término puede requerir varios bloques de disco. Para eficiencia en el acceso se puede tener una lista invertida de un término en u conjunto consecutivos de bloques. Y mejor aún, podemos usar un índice de árbol B+ para mapear cada término a su lista invertida asociada

***Construcción de índices invertidos:***
1. Extraer vocabulario(términos) de los documentos de la colección
2. Armas estadísticas para cada documento dependiendo del modelo usado
3. Invertir el stream de documentos con sus términos en un stream de términos y sus documentos


###### Búsqueda de documentos relevantes a partir de consulta usando índice invertido

Asumimos que tenemos el vocabulario de la colección de documentos. Se trata de un proceso de 3 pasos:
1. **Búsqueda de vocabulario:** Cada término de la consulta se busca en el vocabulario. Los términos se pueden ordenar lexicográficamente para mejorar eficiencia
2. **Retorno de la información de documentos:** se retorna la información del documento para cada término
3. **Manipulación de la información retornada:** la información de cada documento es procesada para incorporar las distintas formas de lógica de consulta
***Tratamiento de consultas booleanas:***
- *Suposiciones:* La consulta involucra $n$ términos. $S_i$ es el conjunto de identificadores de documentos donde aparece el término i ($i \in \{1,...,n\}$) 
- *Operación AND:* Los documentos deseados son $S_1 \cap S_2\cap ... \cap S_n$ 
- *Operación OR:* Los documentos deseados son $S_1 \cup S_2\cup ... \cup S_n$ 
- *Operación NOT:* Sea $t_i$ término $i$. Explicamos NOT $t_i$. Podemos eliminar los documentos que contienen el termino $i$ haciendo  $S-S_i$ 

###### Medición de la relevancia de los resultados de una consulta
Los SRI soportan solo retorno aproximado, por ende pueden darte alguna de las siguientes situaciones:
- Falsos negativos: Algunos documentos relevantes pueden no ser retornados
- Falsos positivos: Algunos documentos irrelevantes pueden ser retornados
- Existen también Verdaderos positivos y verdaderos negativos

Hay algunas métricas de desempeño relevantes como:
- *Precisión*: Número de documentos relevantes retornados por la consulta divididos por el número total de documentos retornados por la consulta
- *Cobertura*: Número de documentos relevantes retornados por la consulta divididos por el número total de documentos relevantes en la base de datos 
La cobertura puede ser incrementada al presentas más resultados al usuario, pero existe el riesgo de que disminuya la precisión 

Al final se termina creando consultas y etiquetando manualmente documentos como relevantes e irrelevantes.

La **F-score** es usada como una medida que combina precisión y cobertura para comparar distintos conjuntos de resultados(es el promedio armónico de dos números) $$F=\frac{2pr}{p+r}$$
# Retorno de la información en la web

###### Rastreadores Web (Web Crawlers)

Dado que la colección de documentos en la web no se proporciona de antemano, los rastreadores web son programas que **localizan y recolectan información** siguiendo hiperenlaces presentes en documentos conocidos.

- **Proceso de Rastreo:** Los rastreadores comienzan con un **conjunto semilla** de documentos, que puede incluir mapas de sitios, páginas populares o sitios de alta autoridad (como Wikipedia, medios o universidades). Este rastreo puede tomar **meses**.
- **Análisis y Filtrado:** Un rastreador explora una página y extrae el **texto visible, metadatos, enlaces** y recursos (imágenes, videos). Es fundamental la **detección de contenido duplicado** y el **filtrado por calidad o spam** (por ejemplo, descartando páginas con poco contenido útil, exceso de publicidad o abuso de palabras clave). También se realiza una **clasificación preliminar** para inferir el tema o categoría de la página.
- **Escalabilidad:** Debido a la inmensidad de la web, el rastreo se realiza mediante **múltiples procesos en paralelo** en varias máquinas. Los enlaces pendientes se almacenan en una **frontera de rastreo**. Un **coordinador** gestiona la asignación de URLs y aplica **políticas de priorización** (basadas en la importancia del sitio y la frecuencia de actualización) para optimizar el uso de recursos y no sobrecargar los procesos.

###### Indexado

Los documentos recolectados son procesados por un sistema de indexado.

- **Índices Invertidos Colosales:** Los motores de búsqueda web utilizan **índices invertidos** que son colosales en tamaño y complejidad, indexando cientos de miles de millones de páginas y actualizándose continuamente.
- **Contenido del Índice:** Para cada palabra, la lista de ocurrencias en las páginas web incluye típicamente el **docID**, la **frecuencia del término**, las **posiciones** donde aparece, y un _**payload**_ con información adicional (como importancia semántica, puntajes de relevancia como TF-IDF, y datos para el _ranking_ como la autoridad del sitio).
- **Actualización Continua:** El proceso de indexado se ejecuta en varias máquinas, creando una **nueva copia del índice** en lugar de modificar el índice viejo, el cual sigue contestando consultas. Una vez completado, el nuevo índice reemplaza al anterior. Una **tabla de documentos** separada mapea el `docID` a la URL, consultada al final del proceso.

###### Búsquedas y Arquitectura Distribuida

Para gestionar la gran cantidad de consultas simultáneas, se utilizan **múltiples máquinas** (servidores).

- **Shards del Índice:** El índice se divide en fragmentos (shards) por términos o rangos de documentos, y cada shard se aloja en servidores distintos, a menudo con réplicas para tolerancia a fallos y balanceo de carga.
- **Procesamiento de Consultas:** Involucra varias etapas:
    1. **Análisis de la consulta:** Se realiza tokenización, normalización (corrección ortográfica, reducción a la raíz, eliminación de _stopwords_), **desambiguación semántica** (interpretando el sentido de cada término según el contexto), y expansión de la consulta.
    2. **Recuperación de documentos:** Se consulta el índice invertido y se aplican filtros (por ejemplo, penalizaciones por baja calidad).
    3. **Ranking de resultados:** Cada documento recibe un puntaje de relevancia para ordenarse.
- **Fusión Distribuida:** La consulta es enrutada a los shards relevantes. Cada shard calcula un _ranking local_, y los resultados se envían a un **coordinador (nodo maestro)** que fusiona las listas y recalcula un **ranking global**.
- **Organización de Nodos:** Los motores modernos son sistemas distribuidos de múltiples capas con nodos especializados (análisis de consulta, recuperación de documentos/shards, ranking global, presentación, indexado y rastreo).

###### Relevancia y PageRank

Las máquinas de búsqueda tempranas usaban principalmente TF-IDF, pero esto generaba problemas (muchos resultados, spam, baja clasificación de páginas populares).

- **Solución para la Web:** Se combina la relevancia tradicional (como TF-IDF) con la **popularidad del sitio**.
- **Medición de Popularidad:**
    - Una idea es usar el **número de enlaces** a un sitio como medida de prestigio. Un refinamiento da más peso a los enlaces provenientes de sitios con mayor prestigio.
    - Otra idea es llevar un registro de qué fracción de veces los usuarios seleccionan una página retornada como resultado de una búsqueda.
- **Algoritmo PageRank:** Este algoritmo, desarrollado por Google, mide la popularidad de una página basándose en la popularidad de las páginas que la enlazan. Se modela como una **caminata aleatoria** donde un navegante salta a una página aleatoria con probabilidad $\delta$ o sigue un enlace con probabilidad $1-\delta$.
- El PageRank de una página es la probabilidad de que esa persona visite la página en un momento dado. Las páginas con alto PageRank tienen más probabilidad de ser visitadas.
- **Combinación de Factores:** PageRank es una medida **estática** (no considera los términos de la consulta). Para obtener un ranking completo, PageRank y TF-IDF se combinan, a menudo utilizando una fórmula propietaria con pesos que se entrenan automáticamente con resultados etiquetados por humanos. Las palabras clave en el **texto del áncora** de los enlaces también se utilizan para inferir la relevancia de una página para un tema.

###### El Buscador de Google

El buscador de Google utiliza arañas web (Googlebot) e indexación masiva.

- **Algoritmos de Búsqueda:** Consideran cientos de factores, incluyendo palabras clave, sinónimos, y la ubicación del usuario, intentando comprender el contexto y la intención de la búsqueda.
- **Clasificación:** Utiliza **PageRank** para clasificar los resultados basándose en la autoridad y relevancia de las páginas. También aplica **personalización** basada en el historial y la ubicación del usuario, y penaliza sitios con spam o contenido duplicado.
- **Elementos del Resultado:** Un enlace devuelto por Google típicamente incluye el **título** (encabezado principal), la **URL** (dirección web), un **extracto** (_snippet_) y una ruta de navegación (_breadcrumb_).
- **Resultados Enriquecidos:** Google ofrece resultados más allá de los enlaces, como **fragmentos destacados** (resúmenes directos, listas o tablas), **paneles de conocimiento**, videos, imágenes, preguntas relacionadas y gráficos.