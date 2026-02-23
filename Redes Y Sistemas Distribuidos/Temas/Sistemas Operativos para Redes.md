Para manejar los tipos de redes a estudiar hacen falta *sistemas operativos de redes (SOR)*. En cada tipo de red hay un problema a ser resuelto si queremos que no tenga un mal desempeño, siendo la SOR quien se encarga de resolver estos problemas. Para que las máquinas en un tipo de red se puedan comunicar hacen falta *protocolos de comunicación*. Los SOR contienen estos protocolos.

Los SOR están organizadas como una pila de capas o niveles, donde la cantidad de capas, los nombres de estas, sus contenidos y su función difieren de un tipo de red a otro. El motivo de esta organización es lograr que cada capa le ofrezca ciertos servicios a las capas superiores ocultando su implementación. De esta forma una capa superior puede acceder a las operaciones y servicios primitivos ofrecidos por una capa inferior mediante le *Interfaz entre dichas capas* la cual es el conjunto de lo que puede ofrecer la capa inferior a la superior.
Además como el SOR se ocupa de la comunicación de información siempre debemos pensar como se comunica una capa $n$ de un dispositivos con la capa $n$ de otro dispositivo sin darle importancia a los problemas de capas inferiores a la $n$.

El *Protocolo de capa $n$* es el conjunto de reglas y convenciones usadas en la conversación entre la capa $n$ de una maquina y la capa $n$ de otra maquina.
Las comunicaciones entre capas consecutivas ocurren:
- **Durante el envío de mensaje:** cada capa pasa los datos y la información de control a la capa inmediatamente inferior, hasta que se alcanza la capa mas baja
- **Durante la recepción de mensaje:** cada capa pasa cierta información conteniendo los datos a la capa inmediatamente superior hasta que alcanza la capa mas alta   

Debajo de la capa 1 está el *medio físico*. Al conjunto de capas y protocolos se la llama *arquitectura de red* o pila de protocolos