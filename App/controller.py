﻿"""
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

from gettext import Catalog
from operator import lt
from DISClib.ADT import list as lit
from turtle import title
from DISClib.Algorithms.Sorting import mergesort as ms
import config as cf
import model
import csv

csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

######## Inicialización del Catálogo de libros
def newController(lt_type):
    """
    Crea una instancia del modelo
    """
    control = {'model':None}
    control['model'] = model.newCatalog(lt_type)

    return control

########## Funciones para la carga de datos
def loadData(control, file_size='5pct'):
    """
    carga los datos de los archivos y cargar los datos de la 
    estructura de datos
    """
    catalog = control['model']
    generalFileAmazon = cf.data_dir + f'Streaming/amazon_prime_titles-utf8-{file_size}.csv'
    generalFileDisney = cf.data_dir + f'Streaming/disney_plus_titles-utf8-{file_size}.csv'
    generalFileHulu = cf.data_dir + f'Streaming/hulu_titles-utf8-{file_size}.csv'
    generalFileNetflix = cf.data_dir + f'Streaming/netflix_titles-utf8-{file_size}.csv'
    input_file_amazon = csv.DictReader(open(generalFileAmazon, encoding='utf-8'))
    input_file_disney = csv.DictReader(open(generalFileDisney, encoding='utf-8'))
    input_file_hulu = csv.DictReader(open(generalFileHulu, encoding='utf-8'))
    input_file_netflix = csv.DictReader(open(generalFileNetflix, encoding='utf-8'))

    for title in input_file_amazon:
        model.addTitles(catalog, title)
        model.addAmazon(catalog, title)
    for title in input_file_disney:
        model.addTitles(catalog, title)
        model.addDisney(catalog, title)
    for title in input_file_hulu:
        model.addTitles(catalog, title)
        model.addHulu(catalog, title)
    for title in input_file_netflix:
        model.addTitles(catalog, title)
        model.addNetflix(catalog, title)

    return catalog

#Funciones de ordenamiento
def AddGenre (catalog, genre):
    return lt.addLast(catalog, genre)
#datos ordenados por año y titulo
def SortCatalogTitle(catalog):
    return model.SortedCatalogGeneral(catalog["general"]["title"])

#Funciones de consulta sobre el catálogo


def sortTopGeneros(catalog):
    SortList = lit.newList('ARRAY_LIST')
    diccionario=model.listarTopGeneros(catalog)
    print(diccionario)
    for x in diccionario:
        info=diccionario.get(x)
        lit.addLast(SortList, info)
    ms.sort(SortList, cmpByTotal)
    return SortList
  

def cmpByTotal(total1, total2):
    return(total1["total"] > total2["total"])


#requerimento 1
 
def period_fechas(lis_o, fechasI, fechaF):
 
   return (model.period_fechas(lis_o, fechasI, fechaF))
  
   #model.period_fechas(lis_o, fechasI, fechaF)
   #print(model.period_fechas(lis_o, fechasI, fechaF))
 
 
 
 
#requerimento 3
 
 
def lis_ac(lis_o, actorP):
 
   return model.lis_ac(lis_o, actorP)