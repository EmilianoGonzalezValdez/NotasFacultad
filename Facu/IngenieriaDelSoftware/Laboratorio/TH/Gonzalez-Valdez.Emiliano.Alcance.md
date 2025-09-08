---
Versíon: "1.0"
Fecha: 2025-08-20T08:37:00
---

### Introducción 
El documento define formalmente el alcance, los objetivos,  y los criterios de aceptación para el desarrollo del sistema "ADOTC". El propósito de dicho sistema es automatizar por completo las jornadas ludicas dedicadas al juego "Agatha Death On The Cards", proporcionando una forma mas intuitiva y remota de jugar conectados a la Internet. En adjunto se presentan las [reglas del juego](https://famaf.aulavirtual.unc.edu.ar/mod/resource/view.php?id=26327)

### Funcionalidades Incluidas:
- Acceso remoto via browser a un listado de partidas no empezadas definido
- Partidas preestablecidas con tamaño desde 2 hasta 6 jugadores
- Cada jugador se identifica con un Nombre y una Foto seleccionados al unirse a una partida, ademas de decir su fecha de nacimiento al unirse a la partida
- Listado de partidas no empezadas con nombre de esta, cantidad de jugadores y una contraseña opcional para hacer privada la misma
- La primera persona en unirse a una partida sera el creador de la misma y tendrá acceso a poder empezar la partida cuando esta posea los jugadores requeridos
- Solo se pueden abandonar partidas no empezadas 
- Se presenta un chat de texto en vivo en cada partida
- Los turnos presentan 1 minuto como tiempo máximo, en cuyo caso de acabar sera como si el jugador no quisiera hacer nada en su turno(referenciando las reglas de l juego) 
- La partida se guardara en una base de datos, permitiendo la recolección en caso de una pronta salida
- Las reglas del juego adjuntadas en la introducción serán respetadas

### Funcionalidades no incluidas:
- Un sistema de Usuarios, amistades, grupos, mensajería fuera de partida
- Una aplicación de escritorio o móvil
- Opción de salir de una partida ya empezada
- Sistema de chat de Voz o Cámara durante la partida
- Historial de partidas
- Creación de salas independientes a las incluidas en la lista
- Alguna forma de bot que rellene lugares en las partidas, ya sea de un jugador que no esta jugando activamente o de algún lugar de la sala que no se ocupo
- Reglas nuevas sobre las propuestas por el juego oficial