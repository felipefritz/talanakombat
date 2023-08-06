import sys

from utils import cargar_pelea_desde_json, crear_jugadores, jugar_pelea


def main(pelea_json_path: str):
    pelea_json_valido = cargar_pelea_desde_json(pelea_json_path)
    if not pelea_json_valido:
        print("Los datos de la pelea en el archivo json contiene datos inválidos")
        return
    
    player1, player2 = crear_jugadores(pelea_json_valido,
                                       nombre_jugador1='Tonyn Stallone',
                                       nombre_jugador2='Arnaldor Shuatseneguer',
                                       combos_jugador_1={'DSDP': (3, 'Taladoken'), 'SDK': (2, 'Remuyuken')},
                                       combos_jugador_2={'SAK': (3, 'Remuyuken'), 'ASAP': (2, 'Taladoken')})
                                       
                                        
    jugar_pelea(player1=player1,
                player2=player2)


if __name__ == '__main__':
    
    main(pelea_json_path='data_peleas/pelea2.json')
    sys.exit()






