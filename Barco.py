class Barco:
    """Clase que representa un barco en el juego."""

    def __init__(self, unidades):
        # unidades: lista de posiciones que ocupa el barco
        self.unidades = unidades

    def tamano(self):
        """Devuelve el tamaño del barco (número de unidades)."""
        return len(self.unidades)
