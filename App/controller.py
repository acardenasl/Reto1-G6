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
 """

import config as cf
import model
import csv

csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def newController(lt_type):
    """
    Crea una instancia del modelo
    """
    control = {'model':None}
    control['model'] = model.newCatalog(lt_type)

    return control

# Funciones para la carga de datos
def loadData(control, file_size='5pct'):
    """
    carga los datos de los archivos y cargar los datos de la 
    estructura de datos
    """
    catalog = control['model']
    #general = loadGeneral(catalog, file_size)
    amazon = loadAmazon(catalog, file_size)
    disney = loadDisney(catalog, file_size)
    hulu = loadHulu(catalog, file_size)
    netflix = loadNetflix(catalog, file_size)
    movies = loadMovies(catalog, file_size)

    return amazon, disney, hulu, netflix,movies

def loadAmazon(catalog, file_size):
    amazonFile = cf.data_dir + f'Streaming/amazon_prime_titles-utf8-{file_size}.csv'
    input_file = csv.DictReader(open(amazonFile, encoding='utf-8'))
    for amazonMovie in input_file:
        model.addAmazonMovie(catalog, amazonMovie)

    return model.amazonMovieSize(catalog), catalog['amazon']


def loadDisney(catalog, file_size):
    disneyFile = cf.data_dir + f'Streaming/disney_plus_titles-utf8-{file_size}.csv'
    input_file = csv.DictReader(open(disneyFile, encoding='utf-8'))
    for disneyMovie in input_file:
        model.addDisneyMovie(catalog, disneyMovie)

    return model.disneyMovieSize(catalog), catalog['disney']

def loadHulu(catalog, file_size):
    huluFile = cf.data_dir + f'Streaming/hulu_titles-utf8-{file_size}.csv'
    input_file = csv.DictReader(open(huluFile, encoding='utf-8'))
    for huluMovie in input_file:
        model.addHuluMovie(catalog, huluMovie)

    return model.huluMovieSize(catalog), catalog['hulu']

def loadNetflix(catalog, file_size):
    netflixFile = cf.data_dir + f'Streaming/netflix_titles-utf8-{file_size}.csv'
    input_file = csv.DictReader(open(netflixFile, encoding='utf-8'))
    for netflixMovie in input_file:
        model.addNetflixMovie(catalog, netflixMovie)

    return model.netflixMovieSize(catalog), catalog['netflix']

def loadMovies(catalog, file_size):

    generalFileAmazon = cf.data_dir + f'Streaming/amazon_prime_titles-utf8-{file_size}.csv'
    generalFileDisney = cf.data_dir + f'Streaming/disney_plus_titles-utf8-{file_size}.csv'
    generalFileHulu = cf.data_dir + f'Streaming/hulu_titles-utf8-{file_size}.csv'
    generalFileNetflix = cf.data_dir + f'Streaming/netflix_titles-utf8-{file_size}.csv'
    input_file_amazon = csv.DictReader(open(generalFileAmazon, encoding='utf-8'))
    input_file_disney = csv.DictReader(open(generalFileDisney, encoding='utf-8'))
    input_file_hulu = csv.DictReader(open(generalFileHulu, encoding='utf-8'))
    input_file_netflix = csv.DictReader(open(generalFileNetflix, encoding='utf-8'))

    for generalMovie in input_file_amazon:
        model.addMovies(catalog, generalMovie)
    for generalMovie in input_file_disney:
        model.addMovies(catalog, generalMovie)
    for generalMovie in input_file_hulu:
        model.addMovies(catalog, generalMovie)
    for generalMovie in input_file_netflix:
        model.addMovies(catalog, generalMovie)

    return model.moviesCatalogSize(catalog), catalog['movies']
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo