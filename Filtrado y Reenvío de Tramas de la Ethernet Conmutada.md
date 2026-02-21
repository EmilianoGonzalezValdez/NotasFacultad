**Reenvío de una trama recibida por el conmutador:**
1. Registrar enlace de ingreso, dirección MAC del host emisor de la trama
2. **Identificación de la interfaz del destino:**
	- Se busca en la tabla del conmutador la dirección MAC del destino
3. Si se encuentra la entrada para el destino:
	- Si el destino está en el segmento por el cual vino la trama
 		- descartar la trama
	- Si no enviar trama en la interfaz indicada por la entrada
- Si no se encuentra una entrada para el destino, **inundar** (enviar en todas las interfaces excepto aquella por la que llegó la trama)

Aqui asumimos que cada tarjeta constituye un dominio de colisiones.

**Ventajas de usar conmutadores:**
- Con un conmutador se pueden enviar tantos datos por segundo como la capacidad de la matriz de conmutación de alta velocidad
- Además, como el conmutador tiene varios búferes (al menos uno por tarjeta, sino más), entonces van a tenerse muchas menos colisiones que si en lugar de un conmutador se tuviera un concentrador