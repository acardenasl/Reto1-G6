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

    catalog = { 'general':None,
                'amazon':None,
                'disney':None,
                'hulu':None,
                'netflix':None,
                'movies':None,
                'series':None,
    }

    catalog['amazon'] = lt.newList(lt_type)
    catalog['disney'] = lt.newList(lt_type)
    catalog['hulu'] = lt.newList(lt_type)
    catalog['netflix'] = lt.newList(lt_type)
    catalog['movies'] = lt.newList(lt_type)  

    return catalog

# Funciones para agregar informacion al catalogo
def addAmazonMovie(catalog, amazonMovie):
    lt.addLast(catalog['amazon'], amazonMovie)

    return catalog


def addDisneyMovie(catalog, disneyMovie):
    lt.addLast(catalog['disney'], disneyMovie)

    return catalog


def addHuluMovie(catalog, huluMovie):
    lt.addLast(catalog['hulu'], huluMovie)

    return catalog


def addNetflixMovie(catalog, netflixMovie):
    lt.addLast(catalog['netflix'], netflixMovie)

    return catalog

def addMovies(catalog, Movies):
    if Movies['type'] == 'Movie':
        lt.addLast(catalog['movies'], Movies)

    return catalog


# Funciones para creacion de datos

# Funciones de consulta
def amazonMovieSize(catalog):
    return lt.size(catalog['amazon'])


def disneyMovieSize(catalog):
    return lt.size(catalog['disney'])


def huluMovieSize(catalog):
    return lt.size(catalog['hulu'])


def netflixMovieSize(catalog):
    return lt.size(catalog['netflix'])

def moviesCatalogSize(catalog):
    return lt.size(catalog['movies'])
# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento