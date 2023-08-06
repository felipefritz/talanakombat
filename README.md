# Requerimiento:

## Descripción Talana Kombat JRPG 

Talana Kombat es un juego donde 2 personajes se enfrentan hasta la muerte. Cada personaje tiene 2 golpes especiales que se ejecutan con una combinación de movimientos + 1 botón de golpe. 

## Botones:

| Botón | Acción   |
|-------|----------|
| W     | Arriba   |
| S     | Abajo    |
| A     | Izquierda|
| D     | Derecha  |
| P     | Puño     |
| K     | Patada   |

## Instrucciones para cargar nuevas peleas:

## Jugadores y Combos:

1. **Tonyn Stallone**

| Combinación | Daño | Movimiento |
|-------------|------|------------|
| DSD + P     | 3    | Taladoken  |
| SD + K      | 2    | Remuyuken  |
| P o K       | 1    | Puño o Patada |

2. **Arnaldor Shuatseneguer**

| Combinación | Daño | Movimiento |
|-------------|------|------------|
| SA + K      | 3    | Remuyuken  |
| ASA + P     | 2    | Taladoken  |
| P o K       | 1    | Puño o Patada |

## Carga de peleas

1. Ir a data_peleas.
2. Crea un archivo json con la siguiente estructura:
3. Los nombres 'player1' y 'player2' no deben ser modificados.
4. Puedes editar los movimientos y golpes a tu gusto siguiendo estas reglas:
   1. Los movimientos son una lista de string y cada string puede ser de largo máximo 5 (puede ser vacío). 
   2. Los golpes son una lista de string  y cada string puede ser un solo botón máximo o un carácter (puede ser vacío). 

## Ejecutar:

1. En la terminal escribe: `python main.py`

## Resultados en pantalla de terminal:

1. Arnaldor Shuatseneguer realiza un Taladoken, dejando a Tonyn Stallone con 4 de vida.
2. Tonyn Stallone se mueve.
3. Arnaldor Shuatseneguer se mueve.
4. Tonyn Stallone realiza un Taladoken, dejando a Arnaldor Shuatseneguer con 3 de vida.
5. Arnaldor Shuatseneguer se mueve.
6. Tonyn Stallone se mueve.
7. Arnaldor Shuatseneguer realiza un Remuyuken, dejando a Tonyn Stallone con 1 de vida.
8. Tonyn Stallone se mueve.
9. Arnaldor Shuatseneguer realiza un Remuyuken, dejando a Tonyn Stallone con -2 de vida.
10. Arnaldor Shuatseneguer gana la pelea!
