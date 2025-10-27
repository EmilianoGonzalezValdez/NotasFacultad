Como la arquitectura tiene impacto sobre los *atributos no funcionales* (Atributos de la [[Calidad]]), debe ser evaluada con respecto a estas propiedades en la arquitectura propuesta. Para ello usaremos el método **ATAM (Archithecture Tradeoff Analysis Method)**
El **ATAM** evalúa las consecuencias de las decisiones arquitectónicas en relación a los atributos de calidad. Sus pasos son:
1. Recolectar escenarios: Elegir escenarios de interés para el análisis, sean principales o excepcionales 
2. Recolectar requerimientos y/o restricciones: Definir lo que se espera del sistema en tales escenarios especificando los niveles deseados para cada atributo de interés
3. Describir las vistas arquitectónicas: Las vistas del sistema son recolectadas 
4. Análisis especifico a cada atributo: Se analizan distintas vistas para diferentes escenarios separadamente para cada atributo de interés para comparar los niveles deseados con los obtenidos en cada uno de estos
5. Identificar puntos sensitivos y de compromiso: Identificamos los puntos de sensibilidad (elementos que afectan a un atributo de interés) y los puntos de compromiso (elementos que afectan a mas de un punto de interés)