"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from gettext import Catalog
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs
import time
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(lt_type):
    """
    Inicializa el catalogo de videos. Crea una lista para los videos, 
    y otra para las categorías. Retorna el catálogo inicializado.
    """

    catalog = {
                'amazon':None,
                'disney':None,
                'hulu':None,
                'netflix':None,
                'movies':None,
                'series':None,
                'general':None,
    }

    catalog['amazon'] = lt.newList(lt_type)
    catalog['disney'] = lt.newList(lt_type)
    catalog['hulu'] = lt.newList(lt_type)
    catalog['netflix'] = lt.newList(lt_type)
    catalog['movies'] = lt.newList(lt_type)
    catalog['series'] = lt.newList(lt_type)
    catalog['general'] = lt.newList(lt_type)

    return catalog

# Funciones para agregar informacion al catalogo

def addAmazon(catalog, amazon):
    lt.addLast(catalog['amazon'], amazon)
    lt.addLast(catalog['general'], amazon)
    return catalog

def addDisney(catalog, disney):
    lt.addLast(catalog['disney'], disney)
    lt.addLast(catalog['general'], disney)
    return catalog

def addHulu(catalog, hulu):
    lt.addLast(catalog['hulu'], hulu)
    lt.addLast(catalog['general'], hulu)
    return catalog

def addNetflix(catalog, netflix):
    lt.addLast(catalog['netflix'], netflix)
    lt.addLast(catalog['general'], netflix)
    return catalog

def addTitles(catalog, title):
    if title['type'] == 'Movie':
        lt.addLast(catalog['movies'], title)
    elif title['type'] == 'TV Show':
        lt.addLast(catalog['series'], title)
    return catalog


# Funciones para creacion de datos

# Funciones de consulta
def amazonSize(catalog):
    return lt.size(catalog['amazon'])

def disneySize(catalog):
    return lt.size(catalog['disney'])

def huluSize(catalog):
    return lt.size(catalog['hulu'])

def netflixSize(catalog):
    return lt.size(catalog['netflix'])

def seriesCatalogSize(catalog):
    return lt.size(catalog['series'])

def moviesCatalogSize(catalog):
    return lt.size(catalog['movies'])

def GeneralCatalogSize (catalog):
    return lt.size(catalog['general'])

# Funciones utilizadas para comparar elementos dentro de una lista
"""
def creacion_de_lista_de_genero_por_parametro (catalog['general'], genre): #4
    lista_de_genero_por_parametro = lt.newList("ARRAY_LIST")
    for i in lt.iterator(catalog['general']):
        if i["listed_in"] == genre:
            lt.addLast(lista_de_genero_por_parametro, i)
    return lista_de_genero_por_parametro
"""

"""
# Funciones de ordenamiento
lista_de_un_genero=creacion_de_lista_de_genero_por_parametro
def ordenar_lista_de_genero_por_parametro (lista_de_un_genero): #4
    for x in range(0,len(lista_de_un_genero)):
        """