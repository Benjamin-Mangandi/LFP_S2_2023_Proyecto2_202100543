class error:
    def __init__(self,tipo, error, fila, columna):
        self.tipo = tipo
        self.error = error
        self.fila = fila
        self.columna = columna