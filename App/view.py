"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from tabulate import tabulate


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- ")

def newController(lt_type):
    """
    Se crea una instancia del controlador
    """
    control = controller.newController(lt_type)
    return control


def loadData(control, file_size='5pct'):
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    amazon, disney, hulu, netflix, movies = controller.loadData(control, file_size)
    
    amazon_size = amazon[0]
    amazon_data = amazon[1]

    disney_size = disney[0]
    disney_data = disney[1]

    hulu_size = hulu[0]
    hulu_data = hulu[1]

    netflix_size = netflix[0]
    netflix_data = netflix[1]

    movies_size = movies[0]
    movies_data = movies[1]

    return amazon_size, amazon_data, disney_size, disney_data, hulu_size, hulu_data, netflix_size, netflix_data, movies_size, movies_data


catalog = None

control = newController('ARRAY_LIST')

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        amz_size, amz_data, dny_size, dny_data, hlu_size, hlu_data, nfx_size, nfx_data,movies_size,movies_data = loadData(control)
        print(tabulate({'Servicio de streaming':['Amazon Prime','Disney Plus','Hulu','Netflix'], \
            'Contenido total':[amz_size, dny_size, hlu_size, nfx_size]}, headers='keys', tablefmt='fancy_grid'))

        # implementar funcion para mostrar 3 primeros y 3 ultimos

        #Amazon
        amazonFirst1 = lt.getElement(amz_data, 1)
        amazonFirst2 = lt.getElement(amz_data, 2)
        amazonFirst3 = lt.getElement(amz_data, 3)
        amazonLast1 = lt.getElement(amz_data, amz_size-2)
        amazonLast2 = lt.getElement(amz_data, amz_size-1)
        amazonLast3 = lt.getElement(amz_data, amz_size)

        #Disney Plus
        disneyFirst1 = lt.getElement(dny_data, 1)
        disneyFirst2 = lt.getElement(dny_data, 2)
        disneyFirst3 = lt.getElement(dny_data, 3)
        disneyLast1 = lt.getElement(dny_data, dny_size-2)
        disneyLast2 = lt.getElement(dny_data, dny_size-1)
        disneyLast3 = lt.getElement(dny_data, dny_size)

        #Hulu
        huluFirst1 = lt.getElement(hlu_data, 1)
        huluFirst2 = lt.getElement(hlu_data, 2)
        huluFirst3 = lt.getElement(hlu_data, 3)
        huluLast1 = lt.getElement(hlu_data, hlu_size-2)
        huluLast2 = lt.getElement(hlu_data, hlu_size-1)
        huluLast3 = lt.getElement(hlu_data, hlu_size)

        #Netflix
        netflixFirst1 = lt.getElement(nfx_data, 1)
        netflixFirst2 = lt.getElement(nfx_data, 2)
        netflixFirst3 = lt.getElement(nfx_data, 3)
        netflixLast1 = lt.getElement(nfx_data, nfx_size-2)
        netflixLast2 = lt.getElement(nfx_data, nfx_size-1)
        netflixLast3 = lt.getElement(nfx_data, nfx_size)

        print(f'\nLas primeras y ultimas 3 peliculas y series de Amazon Prime son: {amazonFirst1}\n{amazonFirst2}\n{amazonFirst3}\n{amazonLast1}\n{amazonLast2}\n{amazonLast3}')

        print(f'\nLas primeras y ultimas 3 peliculas y series de Disney plus son: {disneyFirst1}\n{disneyFirst2}\n{disneyFirst3}\n{disneyLast1}\n{disneyLast2}\n{disneyLast3}')

        print(f'\nLas primeras y ultimas 3 peliculas y series de Hulu son: {huluFirst1}\n{huluFirst2}\n{huluFirst3}\n{huluLast1}\n{huluLast2}\n{huluLast3}')

        print(f'\nLas primeras 3 peliculas de Netflix son: {netflixFirst1}\n{netflixFirst2}\n{netflixFirst3}\n{netflixLast1}\n{netflixLast2}\n{netflixLast3}\n')

    elif int(inputs[0]) == 2:
        pass

    else:
        sys.exit(0)
sys.exit(0)