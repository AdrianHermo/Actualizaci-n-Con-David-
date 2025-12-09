class Tablero:
    def __init__(self):
        self.grid = [['.' for _ in range(5)] for _ in range(5)]

    def colocar(self, f, c):
        self.grid[f][c] = 'B'

    def atacar(self, f, c):
        return "Impacto" if self.grid[f][c] == 'B' else "Agua"