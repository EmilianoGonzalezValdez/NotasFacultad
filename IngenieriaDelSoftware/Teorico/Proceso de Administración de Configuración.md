Un proyecto de software produce muchos ítems: programas, documentos, datos, manuales, etcétera. Cualquiera de ellos puede cambiar fácilmente por lo cual es necesario saber el progreso del estado de cada uno. Esto le da motivo a este proceso

Para dejarlo claro, la administración de configuración del software (SCM) controla sistemáticamente los cambios producidos. Se enfoca en los cambios durante la evolución, los cambios de requerimientos se manejan aparte. Este proceso requiere tanto disciplina como herramientas.

SCM es usualmente independiente del proceso de desarrollo, a medida que los ítems se producen, estos se introducen en la SCM. Cabe aclarar que SCM solo controla los ítems del proceso de desarrollo. De esta forma *la administración de configuración debe asegurar que las distintas versiones se combinen apropiadamente sin perdidas*

Las funcionalidades necesarias son:
- Recolectar todos las fuentes, documentos y otra información del sistema actual
- Evitar cambios o eliminaciones desautorizadas 
- Deshacer cambios o revertir a una versión especifica 
- Hacer disponible la última versión del programa 

Sus mecanismos principales son:
- Control de Acceso
- Control de Versiones
- Identificación de la configuración
- Otros Mecanismos incluyen convenciones de nombres, estructuras de directorios, etc.


Una baseline es  un arreglo apropiado de ítems de configuración. Esta establece puntos de referencia a lo largo del desarrollo del sistemas capturando el estado lógico del sistema y forma la base de cambios posteriores 

Entonces, en el **Proceso de Administración de Configuración** primero definimos las actividades que requieren control de cambio, una vez definidas siguen las siguientes fases:
- Planeamiento: Identificar ítems, definir la estructura del repositorio, definir el control de acceso, puntos de referencia, reconciliación, procedimientos, definir procedimiento de publicación
- Ejecución: Realizar los procedimiento según lo establecido en el planeamiento 
- Auditoría: Para verificar que no se estén cometiendo errores