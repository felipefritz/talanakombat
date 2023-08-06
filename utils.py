import json
from models import Jugador
from validators import valida_datos_de_pelea_en_archivo_json


def cargar_pelea_desde_json(pelea_path_json: str):
    """_summary_
    Lee un archivo json y valida que tenga los datos correctos
    
    Los movimientos son una lista de string y pueden ser de largo máximo 5 (puede ser vacío) 
    Los golpes son una lista de string que pueden ser un solo botón maximo (puede ser vacío) 

    Debe tener la siguiente estructura:
    
    {
        "player1": {"movimientos": ["D","DSD","S","DSD","SD"], "golpes": ["K","P","","K","P"]},
        "player2": {"movimientos": ["SA","SA","SA","ASA","SA"], "golpes": ["K","","K","P","P"]}
    }
    Args:
        pelea_path_json (str): Es un string con la ruta al archivo json de la pelea que se quiere cargar

    Returns:
        Diccionario con los datos de los players 1 y 2 
    """
    with open(pelea_path_json) as file:
        
        pelea_json = json.load(file)
        if not valida_datos_de_pelea_en_archivo_json(pelea_json):
            return False
        else:
            return pelea_json


def crear_jugadores(pelea_json_valida: dict,
                    nombre_jugador1: str,
                    nombre_jugador2: str,
                    combos_jugador_1: dict,
                    combos_jugador_2: dict):
                    
    """Carga los movimientos y golpes de los jugadores del archivo json validado
        
    Args:
        pelea_json_valida (dict): es el json obtenido del archivo de pelea
        combos: son las combinaciones de teclas que generan un poder en el player y tienen el formato:
                {'DSDP': (3, 'Taladoken'), 'SDK': (2, 'Remuyuken')}
                
    Returns:
        2 Instancias de Jugador() para player1 y player2
    """
    player1_movimientos = pelea_json_valida['player1']['movimientos']
    player1_golpes = pelea_json_valida['player1']['golpes']
    
    player2_movimientos = pelea_json_valida['player2']['movimientos']
    player2_golpes = pelea_json_valida['player2']['golpes']
    
    player1 = Jugador(nombre=nombre_jugador1,
                        movimientos=player1_movimientos,
                        golpes=player1_golpes, 
                        combos=combos_jugador_1)
    
    player2 = Jugador(nombre=nombre_jugador2,
                        movimientos=player2_movimientos,
                        golpes=player2_golpes, 
                        combos=combos_jugador_2)
    
    return player1, player2        


def obtener_turno_primer_atacante(player1, player2):
    """ 
    debe partir atacando el jugador que envió una combinación menor de botones (movimiento + golpes), 
    Revisa quien comienza  el ataque basado en su cantidad
    de movimientos y cantidad de golpes declarados en el archivo json

    Args:
        player1 (_type_): models.Jugador()
        player2 (_type_): models.Jugador()

    Returns:
    lista de jugadores ordenados por turno: turno1 al atacar es turno[0]
    """
    if len(player1.movimientos) < len(player2.movimientos) or \
       (len(player1.movimientos) == len(player2.movimientos) and len(player1.golpes) < len(player2.golpes)):
        turno = [player1, player2]
    else:
        turno = [player2, player1]
    return turno


def jugar_pelea(player1, player2):
    """ Comienza la pelea entre player1 y 2, obteniendo el turno del primer atacante, luego cada jugador lanza el ataque o movimiento definido en el
    archivo json de pelea y ademas relata la pelea imprimiendo el estado de cada jugador y movimiento o ataque realizado
    
    Args:
        player1 (_type_): models.Jugador()
        player2 (_type_): models.Jugador()
    
    Returns: Retorna el jugador ganador, pero en el contexto no se requiere, pero se podria requerir para un campeonato de players (escalar el programa)
    """
    turno = obtener_turno_primer_atacante(player1, player2)

    # Pelea comienza
    for i in range(max(len(player1.movimientos), len(player2.movimientos))):
        for jugador in turno:
            danio, movimiento = jugador.ataque(i)
            if danio > 0:
                turno[(turno.index(jugador) + 1) % 2].vida -= danio
                print(f'{jugador.nombre} realiza un {movimiento}, dejando a {turno[(turno.index(jugador) + 1) % 2].nombre} con {turno[(turno.index(jugador) + 1) % 2].vida} de vida')
            elif movimiento:
                print(movimiento)
            
            if turno[(turno.index(jugador) + 1) % 2].vida <= 0:
                print(f'{jugador.nombre} gana la pelea!')
                return jugador
            
