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
from tabulate import tabulate as tab
from prettytable import PrettyTable


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar las películas estrenadas en un periodo de tiempo (G)")
    print("3- Encontrar contenido donde participa un actor (I)")
    print("4- Encontrar contenido por un género especifico (I)")
    print("5- Listar el TOP (N) de los géneros con más contenido (G)")
    print("6- Salir")

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
    amazon, disney, hulu, netflix, movies, series = controller.loadData(control, file_size)
    
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

    series_size = series[0]
    series_data = series[1]

    return amazon_size, amazon_data, disney_size, disney_data, hulu_size, hulu_data, netflix_size, netflix_data, movies_size, movies_data, series_size, series_data

catalog = None

control = newController('ARRAY_LIST')

"""
Menu principal
"""
def PrintRequ7(numTop):
    conta=int(numTop)
    numTopList=lt.newList()
    Sortdict=controller.sortTopGeneros(control["model"])
    for i in Sortdict["elements"]:
        lt.addLast(numTopList, i)
        print(i)
        conta = conta - 1
        if(conta==0):
            break
    print(numTopList)

def CatalogGenre (genre, Catalog):
    resultado = lt.newList("ARRAY_LIST")
    for i in Catalog["general"]:
        lista=i["Listed_in"]
        for x in lista:
            if genre in lista[x]:
                answer=controller.AddGenre(resultado, genre)

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.loadData(control)
    elif int(inputs[0]) == 2:
       print("Seleccione los periodos")
 
       lis_o = loadData(control)
      
       fechaI = int(input('Seleccione año de incio\n'))
       fechaF = int(input('Seleccione año de final\n'))
 
       lista_fechas = controller.period_fechas(lis_o, fechaI, fechaF)
 
       #print(len(lista_fechas))
       #print(lista_fechas)
 
       tablar1 = PrettyTable()
 
       tablar1.field_names = ["type", "release_year", "title", "duration", "sream_service", "director", "cast"]
 
       tablar1.add_row([lt.getElement(lista_fechas, 0)["type"],
       lt.getElement(lista_fechas, 0)["release_year"],
       lt.getElement(lista_fechas, 0)["title"],
       lt.getElement(lista_fechas, 0)["duration"],
       lt.getElement(lista_fechas, 0)["sream_service"],
       lt.getElement(lista_fechas, 0)["director"],
       lt.getElement(lista_fechas, 0)["cast"]])
 
       tablar1.add_row([lt.getElement(lista_fechas, 1)["type"],
       lt.getElement(lista_fechas, 1)["release_year"],
       lt.getElement(lista_fechas, 1)["title"],
       lt.getElement(lista_fechas, 1)["duration"],
       lt.getElement(lista_fechas, 1)["sream_service"],
       lt.getElement(lista_fechas, 1)["director"],
       lt.getElement(lista_fechas, 1)["cast"]])
 
       tablar1.add_row([lt.getElement(lista_fechas, 1)["type"],
       lt.getElement(lista_fechas, 2)["release_year"],
       lt.getElement(lista_fechas, 2)["title"],
       lt.getElement(lista_fechas, 2)["duration"],
       lt.getElement(lista_fechas, 2)["sream_service"],
       lt.getElement(lista_fechas, 2)["director"],
       lt.getElement(lista_fechas, 2)["cast"]])
 
       tablar1.add_row([lt.getElement(lista_fechas, 1)["type"],
       lt.getElement(lista_fechas, -1)["release_year"],
       lt.getElement(lista_fechas, -1)["title"],
       lt.getElement(lista_fechas, -1)["duration"],
       lt.getElement(lista_fechas, -1)["sream_service"],
       lt.getElement(lista_fechas, -1)["director"],
       lt.getElement(lista_fechas, -1)["cast"]])
 
       tablar1.add_row([lt.getElement(lista_fechas, 1)["type"],
       lt.getElement(lista_fechas, -2)["release_year"],
       lt.getElement(lista_fechas, -2)["title"],
       lt.getElement(lista_fechas, -2)["duration"],
       lt.getElement(lista_fechas, -2)["sream_service"],
       lt.getElement(lista_fechas, -2)["director"],
       lt.getElement(lista_fechas, -2)["cast"]])
 
       tablar1.add_row([lt.getElement(lista_fechas, 1)["type"],
       lt.getElement(lista_fechas, -3)["release_year"],
       lt.getElement(lista_fechas, -3)["title"],
       lt.getElement(lista_fechas, -3)["duration"],
       lt.getElement(lista_fechas, -3)["sream_service"],
       lt.getElement(lista_fechas, -3)["director"],
       lt.getElement(lista_fechas, -3)["cast"]])
    
       print(tablar1.get_string())

    elif int(inputs[0]) == 3:
       print("Seleccione actor para encontrar el contendio respectivo")
 
       lis_o = loadData(control)
 
       actorP = input("nombre del actor:")
 
       lis_ac = controller.lis_ac(lis_o, actorP)
 
       tabla2 = PrettyTable()
 
       tabla2.field_names = ["title", "release_year", "director", "sream_service",
        "duration", "cast", "country", "listed_in", "description"]
 
 
       tabla2.add_row([lt.getElement(lis_ac, 0)["title"],
       lt.getElement(lis_ac, 0)["release_year"],
       lt.getElement(lis_ac, 0)["director"],
       lt.getElement(lis_ac, 0)["sream_service"],
       lt.getElement(lis_ac, 0)["duration"],
       lt.getElement(lis_ac, 0)["cast"],
       lt.getElement(lis_ac, 0)["country"],
       lt.getElement(lis_ac, 0)["listed_in"],
       lt.getElement(lis_ac, 0)["description"]])
 
       tabla2.add_row([lt.getElement(lis_ac, 1)["title"],
       lt.getElement(lis_ac, 1)["release_year"],
       lt.getElement(lis_ac, 1)["director"],
       lt.getElement(lis_ac, 1)["sream_service"],
       lt.getElement(lis_ac, 1)["duration"],
       lt.getElement(lis_ac, 1)["cast"],
       lt.getElement(lis_ac, 1)["country"],
       lt.getElement(lis_ac, 1)["listed_in"],
       lt.getElement(lis_ac, 1)["description"]])
 
       tabla2.add_row([lt.getElement(lis_ac, 2)["title"],
       lt.getElement(lis_ac, 2)["release_year"],
       lt.getElement(lis_ac, 2)["director"],
       lt.getElement(lis_ac, 2)["sream_service"],
       lt.getElement(lis_ac, 2)["duration"],
       lt.getElement(lis_ac, 2)["cast"],
       lt.getElement(lis_ac, 2)["country"],
       lt.getElement(lis_ac, 2)["listed_in"],
       lt.getElement(lis_ac, 2)["description"]])
 
       tabla2.add_row([lt.getElement(lis_ac, -3)["title"],
       lt.getElement(lis_ac, -3)["release_year"],
       lt.getElement(lis_ac, -3)["director"],
       lt.getElement(lis_ac, -3)["sream_service"],
       lt.getElement(lis_ac, -3)["duration"],
       lt.getElement(lis_ac, -3)["cast"],
       lt.getElement(lis_ac, -3)["country"],
       lt.getElement(lis_ac, -3)["listed_in"],
       lt.getElement(lis_ac, -3)["description"]])
 
       tabla2.add_row([lt.getElement(lis_ac, -2)["title"],
       lt.getElement(lis_ac, -2)["release_year"],
       lt.getElement(lis_ac, -2)["director"],
       lt.getElement(lis_ac, -2)["sream_service"],
       lt.getElement(lis_ac, -2)["duration"],
       lt.getElement(lis_ac, -2)["cast"],
       lt.getElement(lis_ac, -2)["country"],
       lt.getElement(lis_ac, -2)["listed_in"],
       lt.getElement(lis_ac, -2)["description"]])
 
       tabla2.add_row([lt.getElement(lis_ac, -1)["title"],
       lt.getElement(lis_ac, -1)["release_year"],
       lt.getElement(lis_ac, -1)["director"],
       lt.getElement(lis_ac, -1)["sream_service"],
       lt.getElement(lis_ac, -1)["duration"],
       lt.getElement(lis_ac, -1)["cast"],
       lt.getElement(lis_ac, -1)["country"],
       lt.getElement(lis_ac, -1)["listed_in"],
       lt.getElement(lis_ac, -1)["description"]])
 
       print(tabla2.get_string())
    elif int(inputs[0]) == 4:
        genre=str(input("Escriba el genero a buscar: "))
        print(CatalogGenre(genre, catalog))
    elif int(inputs[0]) == 5:
        top=input("Ingrese el numero TOP de generos a identificar: ")
        PrintRequ7(top)
    else:
        sys.exit(0)
sys.exit(0)