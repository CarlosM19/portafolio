from raton import Raton
from teclado import Teclado
from monitor import Monitor

class Computadora:
    contador_computadora = 0
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadora += 1
        self.__id_computadora = Computadora.contador_computadora
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
    def __str__(self):
        return (
            f"""
            {self._nombre}: {self.__id_computadora}
                Monitor: {self._monitor}
                Teclado: {self._teclado}
                Raton: {self._raton}
            """
        )


