# Requerimiento:

### Descripcion Talana Kombat JRPG 
Talana Kombat es un juego donde 2 personajes se enfrentan hasta la muerte. Cada personaje tiene 2 golpes especiales que se ejecutan con una combinación de movimientos + 1 botón de golpe. 


### Botones:
1. (W) Arriba
2. (S) Abajo
3. (A) Izquierda
4. (D) Derecha
5. (P) Puño
6. (K) Patada 
   

### Instrucciones para cargar nuevas peleas:

### Jugadores y Combos:
1. Tonyn Stallone
      Combinación     daño      movimiento
   1. DSD + P	        3	    Taladoken
   2. SD + K	        2	    Remuyuken
   3. P o K             1       Puño o Patada

2. Arnaldor Shuatseneguer
    Combinación	    daño	movimiento
    1. SA + K	    3	    Remuyuken
    2. ASA + P	    2	    Taladoken
    3. P o K	    1	   Puño o Patada


### Carga de peleas
1. Ir a data_peleas.
2. Crea un archivo json con la siguiente estructura:
   1. {
    "player1": {"movimientos": ["D","DSD","S","DSD","SD"], "golpes": ["K","P","","K","P"]},
    "player2": {"movimientos": ["SA","SA","SA","ASA","SA"], "golpes": ["K","","K","P","P"]}
}
3. nombres player1 y player 2 no deben ser modificados
4. Puedes editar los movimientos y golpes a tu gusto siguiendo estas reglas:
   1. Los movimientos son una lista de string y cada string puede ser de largo máximo 5 (puede ser vacío) 
   2. Los golpes son una lista de string  y cada string puede ser un solo botón maximo o un caracter (puede ser vacío) 


### Ejecutar:
1. En la terminal escribe: python main.py

#### Resultados en pantalla de terminal:
Arnaldor Shuatseneguer realiza un Taladoken, dejando a Tonyn Stallone con 4 de vida
Tonyn Stallone se mueve
Arnaldor Shuatseneguer se mueve
Tonyn Stallone realiza un Taladoken, dejando a Arnaldor Shuatseneguer con 3 de vida
Arnaldor Shuatseneguer se mueve
Tonyn Stallone se mueve
Arnaldor Shuatseneguer realiza un Remuyuken, dejando a Tonyn Stallone con 1 de vida
Tonyn Stallone se mueve
Arnaldor Shuatseneguer realiza un Remuyuken, dejando a Tonyn Stallone con -2 de vida
Arnaldor Shuatseneguer gana la pelea!