from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclado = 0
    def __init__(self, tipoEntrada, marca):
        Teclado.contador_teclado += 1
        self.__id_teclado = Teclado.contador_teclado
        self._tipoEntrada = tipoEntrada
        self._marca = marca
    def __str__(self):
        return (
            f"Id: {self.__id_teclado}, "
            f"Marca: {self._marca}, "
            f"Tipo de Entrada {self._tipoEntrada}"
        )
        
