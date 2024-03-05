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


import config as cf
import pandas as pd
import glob
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {'jobs': None,
                    'skills': None,
                    'employments_types': None,
                    'multilocations': None}
    
    data_structs['jobs'] = lt.newList('ARRAY_LIST')
    data_structs['skills'] = lt.newList('ARRAY_LIST')
    data_structs['employments_types'] = lt.newList('ARRAY_LIST')
    data_structs['multilocations'] = lt.newList('ARRAY_LIST')
    return data_structs


# Funciones para agregar informacion al modelo
def add_job(data_structs, job):
    """
    Función para agregar nuevos elementos job a la lista jobs
    """
    lt.addLast(data_structs['jobs'], job)
    return data_structs


def add_skill(data_structs, skill):
    """
    Función para agregar nuevos elementos skill a la lista skills
    """
    lt.addLast(data_structs['skills'], skill)
    return data_structs


def add_employment_type(data_structs, employment_type):
    """
    Función para agregar nuevos elementos employment_type a la lista employments_types
    """
    lt.addLast(data_structs['employments_types'], employment_type)
    return data_structs


def add_multilocation(data_structs, multilocation):
    """
    Función para agregar nuevos elementos multilocation a la lista multilocations
    """
    lt.addLast(data_structs['multilocations'], multilocation)
    return data_structs


# Funciones para creacion de datos
def new_job(title,street,city,country_code,address_text,marker_icon,workplace_type,company_name,company_url,company_size,
            experience_level,published_at,remote_interview,open_to_hire_ukrainians,id,display_offer):
    """
    Crea un nuevo elemento job
    """
    job = {'title': '',
           'street': '',
           'city': '',
           'country_code': '',
           'address_text': '',
           'marker_icon': '',
           'workplace_type': '',
           'company_name': '',
           'company_url': '',
           'company_size': '',
           'experience_level': '',
           'published_at': '',
           'remote_interview': '',
           'open_to_hire_ukrainians': '',
           'id': '',
           'display_offer': ''}
    
    job['title'] = title
    job['street'] = street
    job['city'] = city
    job['country_code'] = country_code
    job['address_text'] = address_text
    job['marker_icon'] = marker_icon
    job['workplace_type'] = workplace_type
    job['company_name'] = company_name
    job['company_url'] = company_url
    job['company_size'] = company_size
    job['experience_level'] = experience_level
    job['published_at'] = published_at
    job['remote_interview'] = remote_interview
    job['open_to_hire_ukrainians'] = open_to_hire_ukrainians
    job['id'] = id
    job['display_offer'] = display_offer
    return job

def new_skill(field, level, title):
    """
    Crea un nuevo elemento skill
    """
    skill = {'field': '',
             'level': '',
             'title': ''}
    
    skill['field'] = field
    skill['level'] = level
    skill['title'] = title
    return skill

def new_employment_type(type, title, currency, min_salary, max_salary):
    """
    Crea un nuevo elemento employment_type
    """
    employment_type = {'type': '',
                       'title': '',
                       'currency': '',
                       'min_salary': '',
                       'max_salary': ''}
    
    employment_type['type'] = type
    employment_type['title'] = title
    employment_type['currency'] = currency
    employment_type['min_salary'] = min_salary
    employment_type['max_salary'] = max_salary  
    return employment_type

def new_multilocation(location, city, title):
    """
    Crea un nuevo elemento multilocation
    """
    multilocation = {'location': '',
                     'city': '',
                     'title': ''}
    
    multilocation['location'] = location
    multilocation['city'] = city
    multilocation['title'] = title
    return multilocation

# Funciones de consulta


def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass

def job_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    size = lt.size(data_structs['jobs'])
    return size

def skill_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    size = lt.size(data_structs['skills'])
    return size

def employment_type_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    size = lt.size(data_structs['employments_types'])
    return size

def multilocation_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    size = lt.size(data_structs['multilocations'])
    return size

def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs, nombre_empresa, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 3
    """
    contador_general = 0
    contador_senior = 0
    contador_mid = 0
    contador_junior = 0
    listado_ofertas = lt.newList('ARRAY_LIST')

    for oferta in lt.iterator(data_structs['jobs']):
        if nombre_empresa == oferta['company_name']:
            oferta_valida = cmp_fechas(fecha_inicial, oferta, fecha_final)
            if oferta_valida != None:
                
                contador_general += 1

                if 'senior' == oferta_valida['experience_level']:
                    contador_senior += 1

                elif 'mid' == oferta_valida['experience_level']:
                    contador_mid += 1

                else:
                    contador_junior += 1
                lt.addLast(listado_ofertas, oferta_valida)

    sa.sort(listado_ofertas, cmd_fecha_y_pais)
    return contador_general, contador_senior, contador_mid, contador_junior, listado_ofertas

def req_4(data_structs, codigo_pais, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    archivos_csv = glob.glob("*.csv")
    data = pd.concat((pd.read_csv(f) for f in archivos_csv), ignore_index=True)
    data_filtrada = data[(data['country_code'] == codigo_pais) & (data['published_at'] >= fecha_inicial) & (data['published_at'] <= fecha_final)]

    total_ofertas = len(data_filtrada)
    total_empresas = data_filtrada['company_name'].nunique()
    total_ciudades = data_filtrada['city'].nunique()
    ciudad_mas_ofertas = data_filtrada['city'].value_counts().idxmax()
    conteo_ciudad_mas_ofertas = data_filtrada['city'].value_counts().max()
    ciudad_menos_ofertas = data_filtrada['city'].value_counts().idxmin()
    conteo_ciudad_menos_ofertas = data_filtrada['city'].value_counts().min()
    data_ordenada = data_filtrada.sort_values(by=['published_at', 'company_name'])
    return total_ofertas, total_empresas, total_ciudades, ciudad_mas_ofertas, conteo_ciudad_mas_ofertas, ciudad_menos_ofertas, conteo_ciudad_menos_ofertas


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass

# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass

def cmp_fechas(fecha_inicial, oferta, fecha_final):
    if fecha_inicial[0:10] <= oferta['published_at'][0:10] <= fecha_final[0:10]:
        return oferta

def cmp_fechas_sa(fecha_1, fecha_2):
    if fecha_1[0:10] < fecha_2[0:10]:
        return fecha_1

def cmd_fecha_y_pais(oferta_1, oferta_2):
    if oferta_1['published_at'][0:10] < oferta_2['published_at'][0:10]:
        if oferta_1['country_code'] < oferta_2['country_code']:
            return oferta_1

def cmp_ofertas_by_empresa_y_fecha (oferta1, oferta2):
    """
    Devuelve verdadero (True) si la empresa de la oferta1 es menor que en la
    oferta2, en caso de que sean iguales se analiza la fecha de publicación de la oferta
    laboral, de lo contrario devuelva falso (False).
    Args:
    oferta1: información de la primera oferta laboral que incluye
    "company_name" y "published_at"
    oferta1: información de la segunda oferta laboral que incluye
    "company_name" y "published_at"
    | """
    #Comparar el nombre de la empresa
    if oferta1["company_name"] < oferta2["company_name"]:
        return True
    elif oferta1["company_name"] > oferta2["company_name"]:
        return False
    else:
        #Comparar fecha de publicacion
        fecha_oferta1 = oferta1["published_at"]
        fecha_oferta2 = oferta2["published_at"]

        #Extraer los items de la fecha
        fecha_oferta1_items = fecha_oferta1.split(" ")
        fecha_oferta2_items = fecha_oferta2.split(" ")

        #Comparar año, mes, dia, hora y minuto 
        for i in range(len(fecha_oferta1_items)):
            if fecha_oferta1_items[i] < fecha_oferta2_items[i]:
                return True 
            elif fecha_oferta1_items[i] > fecha_oferta2_items[i]:
                return False
        #Si las fechas son iguales
        return False

def seleccion_array_o_linked(answer):
    if answer=="1":
        answer=lt.newList("ARRAY_LIST")
        add_employment_type(answer)
        add_job(answer)
        add_multilocation(answer)
        add_skill(answer)        
    elif answer=="2":
        answer==lt.newList("SINGLE_LINKED")
        add_employment_type(answer)
        add_job(answer)
        add_multilocation(answer)
        add_skill(answer) 
    return answer
        
def sublist(lst, pos, num):
    new_sublist = lt.subList(lst, pos, num)
    return new_sublist

def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
