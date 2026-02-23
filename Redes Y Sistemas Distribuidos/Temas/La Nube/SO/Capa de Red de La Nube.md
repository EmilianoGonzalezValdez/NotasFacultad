La capa de red está formada por protocolos que facilitan la conectividad y el enrutamiento dentro de la infraestructura de red de cada proveedor.
También se preocupa de la seguridad de estas redes. Los protocolos usados son:
- *Protocolos de internet:* Son importantes para que los datos puedan moverse entre redes conectadas a través de internet. Se usan BGP e IP
- *Protocolos para redes privadas virtuales (VPN):* Las VPN permiten establecer conexiones seguras entre las redes del cliente y la nube a través de internet. Los protocolos mas comunes incluyen:
	- *OpenVPN:* Cifra los datos y asegura que viajen protegidos a través de una conexión pública
	- *WireGuard:* También cifra conexiones VPN, ofreciendo mayor velocidad y simplicidad
- *Protocolos para conexiones privadas entre cliente y proveedor de la nube:* Cuando las empresas necesitan conexiones más rápidas y seguras, pueden optar por métodos privados que no usan internet. Por ejemplo:
	- *MPLS:* crea rutas privadas dedicadas para enviar datos directamente entre las instalaciones del cliente y el proveedor de nube
	- *Tuneles VPN:* permiten crear una conexión segura sobre internet público hacia el proveedor de nube, utilizando protocolos como IPsec o L2TP
	- *Conexiones dedicadas:* establecen líneas privadas entre el centro de datos del cliente y la nube, siendo estas conexiones mas rápidas, confiables y seguras que las basadas en internet público