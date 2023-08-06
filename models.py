class Jugador:
    def __init__(self, movimientos, golpes, nombre, combos):
        self.movimientos = movimientos
        self.golpes = golpes
        self.vida = 6
        self.nombre = nombre
        self.combos = combos

    def ataque(self, i):
        danio = 0
        movimiento = ''
        if i < len(self.movimientos) and i < len(self.golpes):
            combo = self.movimientos[i] + self.golpes[i]
            if combo in self.combos:
                danio, movimiento = self.combos[combo]
            elif self.movimientos[i]:
                movimiento = f'{self.nombre} se mueve'
            elif self.golpes[i] == 'P':
                movimiento = 'Puño'
                danio = 1
            elif self.golpes[i] == 'K':
                movimiento = 'Patada'
                danio = 1
        return danio, movimiento
