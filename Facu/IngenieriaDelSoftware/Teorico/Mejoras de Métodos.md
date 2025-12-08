**Extracción de métodos:** Se realiza si un método es demasiado largo, su objetivo es separar el método largo en otros métodos cortos cuya signatura indique lo que el método hace:

- Partes del código se extraen como nuevos métodos
- Variables referenciadas en estas partes se transforman en parámetros
- Variables declaradas en esta parte pero utilizadas en otras partes deben definirse en el método original
- También se realiza si existe un método que retorna un valor y además cambia el estado del objeto

**Agregar/eliminar parámetros:** Sirve para simplificar las interfaces donde sea posible:

- Agregar sólo si los parámetros existentes no proveen toda la información necesaria
- Eliminar si los parámetros se agregaron originalmente "por las dudas" y/o no se utilizan