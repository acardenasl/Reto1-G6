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

# Funciones de ordenamiento

    #organizar por merge elementos por rango de años


def listarTopGeneros(catalog):
    generostop={}

    #Buscador top generos para amazon
    for i in range(1, lt.size(catalog["amazon"])):
        pelicula=lt.getElement(catalog["amazon"], i)
        generos=pelicula["listed_in"].split(",")
        for x in generos:
            if not x in generostop:
                generostop[x] = {"nombre":x,"total":0, "movies": 0, "TV_shows":0}
            generostop[x]["total"]+=1
            if pelicula["type"]=="Movie":
                generostop[x]["movies"]+=1
            if pelicula["type"]=="TV Show":
                generostop[x]["TV_shows"]+=1

    #Buscador top generos para disney
    for i in range(1, lt.size(catalog["disney"])):
        pelicula=lt.getElement(catalog["disney"], i)
        generos=pelicula["listed_in"].split(",")
        for x in generos:
            if not x in generostop:
                generostop[x] = {"nombre":x,"total":0, "movies": 0, "TV_shows":0}
            generostop[x]["total"]+=1
            if pelicula["type"]=="Movie":
                generostop[x]["movies"]+=1
            if pelicula["type"]=="TV Show":
                generostop[x]["TV_shows"]+=1

    #Buscador top generos para hulu   
    for i in range(1, lt.size(catalog["hulu"])):
        pelicula=lt.getElement(catalog["hulu"], i)
        generos=pelicula["listed_in"].split(",")
        for x in generos:
            if not x in generostop:
                generostop[x] = {"nombre":x,"total":0, "movies": 0, "TV_shows":0}
            generostop[x]["total"]+=1
            if pelicula["type"]=="Movie":
                generostop[x]["movies"]+=1
            if pelicula["type"]=="TV Show":
                generostop[x]["TV_shows"]+=1

    #Buscador top generos para Netflix
    for i in range(1, lt.size(catalog["netflix"])):
        pelicula=lt.getElement(catalog["netflix"], i)
        generos=pelicula["listed_in"].split(",")
        for x in generos:
            if not x in generostop:
                generostop[x] = {"nombre":x,"total":0, "movies": 0, "TV_shows":0}
            generostop[x]["total"]+=1
            if pelicula["type"]=="Movie":
                generostop[x]["movies"]+=1
            if pelicula["type"]=="TV Show":
                generostop[x]["TV_shows"]+=1

    return generostop