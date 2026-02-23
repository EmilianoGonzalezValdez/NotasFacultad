Si dos tramas se transmiten en forma simultánea en un canal de difusión: se traslapan en el tiempo y la señal resultante se altera. Este evento se llama **colisión**

¿Cómo evitar/disminuir las colisiones?

Para ello vamos a definir una subcapa de la capa de enlace de datos que se encargue del control de colisiones. Esta subcapa de la CED se llama *subcapa de control de acceso al medio (SCAM)*. La subcapa MAC (intuyo que se refiere a SCAM) es una subcapa inferior de la CED

¿Por qué estudiar la SCAM?
- Para comprender cómo se organizan, diseñan y funcionan las LAN cableadas e inalámbricas
- Para entender cómo los distintos tipos de LAN hacen control de colisiones. Para esto se usan *protocolos de control de colisiones*

En una *red de difusión* el asunto clave es cómo determinar quén puede usar el canal cuando hay competencia por él.
*Protocolos de acceso múltiple* PAM: se usan para determinar quién sigue en un canal de difusión

