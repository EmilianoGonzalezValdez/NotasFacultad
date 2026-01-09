El código necesita ser verificado antes de ser utilizado por otros. Para ello hay diferentes técnicas:

- Inspección de código
- Test de Unidad
- Verificación de programa

La inspección de código es un proceso de revisión como cualquier otro, se aplica luego de que el código fue compilado, testeado algunas veces y chequeado con herramientas de análisis estático. Se utilizan listas de control para enfocar la atención en puntos clave ya que es caro(es perder una persona para que se ponga a revisar)

El test de unidad es simplemente un test que se enfoca solo en el módulo escrito por un programador, el cual es también responsable de hacerlo (normalmente). Este test consta de varios casos y "drivers", los cuales ejecutan el módulo con sus test para automatizarlos

En el análisis estático se utilizan herramientas para analizar los programas fuentes y verificar la existencia de problemas, aunque muchas veces estos dan falsos positivos. Son muy útiles para encontrar pequeños bugs como memory leaks