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

import random
from datetime import datetime
import config as cf
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
    
    data_structs['jobs'] = lt.newList()
    data_structs['skills'] = lt.newList()
    data_structs['employments_types'] = lt.newList()
    data_structs['multilocations'] = lt.newList()
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

def new_job(data_structs, title,street,city,country_code,address_text,marker_icon,workplace_type,company_name,company_url,company_size,
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

def new_skill(data_structs, field, level, title):
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

def add_Data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    
    return lt.addLast(data_structs, data)

def obtener_un_dato(lista,indice):
    """
    Retorna un dato a partir de su ID
    """
    return lt.getElement(lista,indice)

def get_data(data_structs):
    """
    Retorna un dato a partir de su ID
    """
    resultados = lt.newList("ARRAY_LIST")
    tamano= int(lt.size(data_structs))
    lt.addFirst(resultados,lt.firstElement(data_structs))
    for b in range(2,4):
        p = obtener_un_dato(data_structs, b)
        add_Data(resultados, p)
    for b in range (0,3):
        p = obtener_un_dato(data_structs, (tamano-b))
        add_Data(resultados, p)
    return resultados

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

def organizar_lista(list,cmp, alg=sa):
    if alg == "Selection":
        alg = se
    elif alg == "Insertion":
        alg = ins
    elif alg == "Shell":
        alg = sa
    else:
        alg = sa
    return alg.sort(list,cmp)

def cmp_fecha(dato1,dato2):
    
    if dato1["published_at"] > dato2["published_at"]:
        return True
    elif dato1["published_at"] < dato2["published_at"]:
        return False 
    
        


def req_2(data_structs,  ciudad, nombre_empresa):
    """
    Función que soluciona el requerimiento 2
    """
    ofertas=data_structs["jobs"]
    of_empresa_y_ciudad=lt.newList["ARRAYLIST"]
    for g in lt.iterator(ofertas):
        if g["company_name"]==nombre_empresa and g["city"]==ciudad:
            lt.addLast(of_empresa_y_ciudad, {"published_at":g["published_at"], "country_code":g["country_code"], "city":g["city"], "company_name":g["company_name"], "title":g["title"], "experience_level":g["experience_level"], "workplace_type":g["workplace_type"], "address_text":g["address_text"]})
    return of_empresa_y_ciudad

def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def cmp_fechas(fecha_inicial, oferta, fecha_final):
    if fecha_inicial[0:10] <= oferta['published_at'][0:10] <= fecha_final[0:10]:
        return oferta


def cmd_fecha_y_pais(oferta_1, oferta_2):
    if oferta_1['published_at'][0:10] < oferta_2['published_at'][0:10]:
        if oferta_1['country_code'] < oferta_2['country_code']:
            return oferta_1
        
    
    
def req_5(data_structs, nom_ciudad, f_inicial, f_final):
    """
    Función que soluciona el requerimiento 5
    """
    
    general=0
    dict_company_name={}
    listado_ofertas=lt.newList("ARRAY_LIST")
    
    for oferta in lt.iterator(data_structs["jobs"]):
        oferta_valida=cmp_fechas(f_inicial, oferta, f_final)
        if oferta_valida!=None:
            if oferta["city"]==nom_ciudad:
                general +=1
                dict_company_name[oferta["company_name"]]+=1
                lt.addLast(listado_ofertas, oferta)
                
    llave_menor=min(dict_company_name, key=lambda k:dict_company_name[k])
    llave_mayor=max(dict_company_name, key=lambda k:dict_company_name[k])
    valor_menor=dict_company_name["llave_menor"]
    valor_mayor=dict_company_name["llave_mayor"]
        
    
    
    
    
        
        
        
                
                
                
                
                
            
                
    
    
       
    
    

    
    

def req_6(data_structs, n_ciudades, country_code, experience_level, f_inicial, f_final):
    """
    Función que soluciona el requerimiento 6
    """
    empleo=data_structs["employments_types"]
    ofertas=organizar_lista(data_structs["jobs"], cmp_fecha)
    res_city_cumplen=lt.newList("ARRAYLIST")
    res_empresas_cumplen=lt.newList("ARRAYLIST")
    res_ofertas_cumplen=lt.newList("ARRAYLIST")
    res_mayor_n_city=0
    res_menor_n_city=0
    res_req_6=lt.newList("ARRAYLIST")
    for oferta in lt.iterator(ofertas):
        


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
        answer==lt.newList("LINKED_LIST")
        add_employment_type(answer)
        add_job(answer)
        add_multilocation(answer)
        add_skill(answer) 
    return answer
        
    
def sublist(lista,inicio,numero):
    lista = lt.subList(lista,inicio,numero)
    return lista    

def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
