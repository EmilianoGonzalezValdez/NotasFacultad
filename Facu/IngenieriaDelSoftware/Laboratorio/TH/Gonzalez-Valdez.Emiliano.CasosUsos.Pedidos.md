### Caso de Uso 1 : Iniciar Partida
Actor Primario: Usuario 
Precondición: La partida ha sido creada 
**Escenario exitoso principal:** 
1. El Usuario creador de la partida solicita al sistema iniciar la partida
2. El sistema valida que la cantidad de jugadores esté entre 2 y 6, luego cambia el estado de la partida a "En curso", le asigna roles secretos a los Jugadores y les reparte su primera mano, elige al primer usuario en jugar en base a quien este mas cerca de la fecha de nacimiento de Agatha Christie, y les notifica a los usuarios que la partida ha comenzado junto con sus roles, mano principal y secretos
**Escenario Excepcionales:** 
2.a) El número de jugadores esta fuera del intervalo [2,6]
- El sistema notifica al creador de la partida que hay un número de jugadores invalido

2.b) Un jugador que no es el creador de la partida quiere iniciar la partida
- El sistema notifica que solo el creador de la partida puede iniciarla 

### Caso de Uso 2 : Turno Completo
Actor Primario: Usuario 
Precondición: La partida ha sido iniciada
**Escenario exitoso principal:** 
1. El Usuario Juega una carta de efecto
2. El sistema valida dicha carta y le notifica al usuario que debe elegir un target para dicho efecto
3. El Usuario elige un target
4. El sistema valida el target y aplica dicho efecto, luego notifica al usuario que su acción se ha completado y que debe descartar y alzar cartas
5. El usuario descarta tantas cartas como quiere y alza las que necesite hasta llegar a 6 cartas
6. El sistema valida que tenga 6 cartas y notifica a los usuarios que ha finalizado el turno
**Escenario Alternativos:**
1.a) El usuario Juega un set de Detective
- El sitema valida que el set tenga las cartas mínimas necesarias y le notifica al usuario que se ha bajado el set
1.b) El usuario agrega una carta de detective a un set
- El sistema verifica que el set exista, que tanto el set como la carta sean del mismo detective y le notifica al usuario que se logro bajar la carta al set
1.c) El usuario descarta una carta y alza otra
- El sistema valida la jugada y le notifica al usuario que su turno ha terminado
1.d) El usuario no realizo ninguna acción en su turno
- El sistema descarta y alza 1 carta aleatoria de la mano del jugador y da por finalizado el turno, luego notifica que el turno ha finalizado
6.a) Al alzar cartas el usuario descubre la ultima carta de la baraja
- El sistema valida que sea la ultima carta de la baraja, notifica a los usuarios que ha ganado el asesino y da por finalizada la partida, cambiando el estado de esta a "Finalizada"
**Escenario Excepcionales:**
4.a) El usuario elige un target incorrecto
- El sistema notifica que el target elegido es incorrecto

### Caso de Uso 3 : Efecto de Carta Not So Fast
Actor principal: Usuario afectado por alguna carta
Precondición: El Usuario fue elegido como objetivo de algún efecto de carta
**Escenario exitoso principal:**
1. El usuario decide usar la carta Not So Fast contra la carta jugada por el otro jugador
2. El sistema valida que se pueda usar actualmente la carta Not So Fast, aplica su efecto y notifica a los usuarios de su uso 
**Escenrio Excepcionales:**
2.a) La carta Not So Fast no puede jugarse actualmente
- El sistema notifica al usuario que no puede jugar dicha carta
