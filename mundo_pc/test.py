from orden import Orden
from computadora import Computadora
from monitor import Monitor
from teclado import Teclado
from raton import Raton

raton1 = Raton("Microsoft", "Bluetooth")
raton2 = Raton("HP", "USB")
raton3 = Raton("Lenovo", "USB")

teclado1 = Teclado("USB", "Microsoft")
teclado2 = Teclado("Bluetooth", "HP")
teclado3 = Teclado("USB", "Lenovo")

monitor1 = Monitor("HP", "21 Pulg.")
monitor2 = Monitor("Lenovo", "19 Pulg.")
monitor3 = Monitor("BenQ", "24 Pulg.")

computadora1 = Computadora("HP", monitor1, teclado2, raton2)
computadora2 = Computadora("Lenovo", monitor2, teclado3, raton3)
computadora3 = Computadora("Armada", monitor3, teclado1, raton1)

computadoras1 = [computadora1, computadora3]
computadoras2 = [computadora3, computadora2]

orden1 = Orden(computadoras1)
orden2 = Orden(computadoras2)
orden1.agregarComputadora(computadora2)

print(orden1)
print(orden2) 