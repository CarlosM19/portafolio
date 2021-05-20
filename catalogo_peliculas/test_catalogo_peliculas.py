from dominio.peliculas import Peliculas
from servicio.catalogo_peliculas import CatalogoPeliculas

opcion = None
while opcion != '4':
    print('Opciones:')
    print('1. Agregar Película:')
    print('2. Listar las Peliculas:')
    print('3. Eliminar Catalogo de Películas')
    print('4. Salir del Programa')
    opcion = input('Ingresa el número de tu Opción (1-4): ')
    if opcion == '1':
        nombre_pelicula = input('Ingresa el nombre de la película: ')
        pelicula = Peliculas(nombre_pelicula)
        CatalogoPeliculas.agregar_pelicula(pelicula)
    elif opcion == '2':
        CatalogoPeliculas.listar_peliculas()
    elif opcion == '3':
        CatalogoPeliculas.eliminar()
else:
    print('Salimos del Programa...')

