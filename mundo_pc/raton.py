from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_raton = 0
    def __init__(self, marca, tipoEntrada):
        Raton.contador_raton += 1
        self.__id_raton = Raton.contador_raton
        self._marca = marca
        self._tipoEntrada = tipoEntrada
    def __str__(self):
        return (
            f"Id: {self.__id_raton}, "
            f"Marca: {self._marca}, "
            f"Tipo de Entrada: {self._tipoEntrada}. "
        )
        

