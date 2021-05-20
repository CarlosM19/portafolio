class Orden:
    contador_orden = 0
    
    def __init__(self, computadoras):
        Orden.contador_orden += 1
        self.__id_orden = Orden.contador_orden
        self._computadoras = computadoras
        
    def agregarComputadora(self, computadora):
        self._computadoras.append(computadora)
    
    def __str__(self):
        computadora_str = " "
        for computadora in self._computadoras:
            computadora_str += computadora.__str__()
        
        return (
            f"Orden: {self.__id_orden}, "
            f"Computadoras: {computadora_str}"
        )
        

    