La codificación comienza ni bien está disponible la especificación del diseño de los módulos. Normalmente los módulos se asignan a programadores individuales. Acá también existe la noción de desarrollo Top-Down o Bottom-Up dependiendo de que nivel de módulo se desarrolla primero.

Hay 2 principales procesos de codificación:

1. Proceso Básico o programación incremental:
    - Escribir el código del modulo
    - Realizar test de unidad
    - Si hay algún error, arreglar bugs y repetir tests
2. **TDD**(Test Driven Development):
    - Primero se escriben los test y luego el código para que este pase los tests
    - Se realiza incrementalmente
    - La complejidad del código depende de que tan exhaustivos sean los tests
    - Normalmente el código necesitara una refactorización
    - Lo ideal seria que los test no sean mockeados
    - Selftesting code

Otra practica del Extreme Programming (además del TDD) es la programación de a pares, donde el código se escribe por dos programadores en vez de uno solo, mientras uno tipea, el otro va revisando lo tipeado. Estos roles se alternan periódicamente.

Otro paso esencial que los programadores deben realizar es el control de código fuente, donde normalmente se utilizan herramientas como SVN, CVS, VVS. Prácticamente esta herramienta es un repositorio donde se almacenan los archivos del código y de donde se construirá el sistema. Estas herramientas mantienen una historia completa de los cambios, permitiendo que todas las versiones viejas pueden recuperarse