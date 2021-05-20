class DispositivoEntrada:
    def __init__(self, tipoEntrada, marca):
        self._tipoEntrada = tipoEntrada
        self._marca = marca
    def __str__(self):
        return self._tipoEntrada + str(self._marca)
    