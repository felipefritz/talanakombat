

def valida_datos_de_pelea_en_archivo_json(pelea_json):
    movimientos_validos = ['D', 'S', 'A']
    golpes_validos = ['P', 'K']
    
    if not validar_player_names_en_json(pelea_json):
        return False
    
    for jugador in ['player1', 'player2']:
        for movimiento in pelea_json[jugador]['movimientos']:
            for m in movimiento:
                if m not in movimientos_validos:
                    return False

        for golpe in pelea_json[jugador]['golpes']:
            if golpe and golpe not in golpes_validos:
                return False

    return True


def validar_player_names_en_json(pelea_json):
    nombre_jugadores_validos = ['player1', 'player2']

    for jugador in pelea_json.keys():
        if jugador not in nombre_jugadores_validos:
            print(f"El jugador '{jugador}' no es válido. Los jugadores válidos son 'player1' y 'player2'.")
            return False
    return True