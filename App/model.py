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


# Funciones de consulta

def get_data(lst, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    element = lt.getElement(lst, id)
    return element

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

def req_1(data_structs, n_ofertas, codigo_pais, nivel_experticia):
    """
    Función que soluciona el requerimiento 2
    """
    ofertas_nivel_experticia = 0
    listado_ofertas = lt.newList('ARRAY_LIST')

    for oferta in lt.iterator(data_structs['jobs']):
        if codigo_pais == oferta['country_code']:
            if nivel_experticia == oferta['experience_level']:
                ofertas_nivel_experticia += 1
                lt.addLast(listado_ofertas, oferta)
    listado_ofertas = sublist(listado_ofertas, 1, n_ofertas)

    return ofertas_nivel_experticia, listado_ofertas

def req_2(data_structs, n_ofertas, nombre_empresa, city):
    """
    Función que soluciona el requerimiento 2
    """
    contador_ofertas = 0
    listado_ofertas = lt.newList('ARRAY_LIST')

    for oferta in lt.iterator(data_structs['jobs']):
        if nombre_empresa == oferta['company_name']:
            if city == oferta['city']:
                contador_ofertas += 1
                lt.addLast(listado_ofertas, oferta)
                
    listado_ofertas = sublist(listado_ofertas, 1, n_ofertas)

    return contador_ofertas, listado_ofertas


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
            esta_entre_fechas_inicial_y_final = cmp_entre_fechas_inicial_y_final(fecha_inicial, oferta, fecha_final)
            if esta_entre_fechas_inicial_y_final:
                contador_general += 1
                if 'senior' == oferta['experience_level']:
                    contador_senior += 1
                elif 'mid' == oferta['experience_level']:
                    contador_mid += 1
                else:
                    contador_junior += 1
                lt.addLast(listado_ofertas, oferta)


    return contador_general, contador_junior, contador_mid, contador_senior, listado_ofertas


def req_4(data_structs, codigo_pais, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    ofertas_periodo_pais = 0
    dict_city = {}
    empresas_pais = lt.newList('ARRAY_LIST')
    listado_ofertas = lt.newList('ARRAY_LIST')

    for oferta in lt.iterator(data_structs['jobs']):
        if codigo_pais == oferta['country_code']:
            if not lt.isPresent(empresas_pais, oferta['company_name']):
                lt.addLast(empresas_pais, oferta['company_name'])
            if oferta['city'] not in dict_city:
                dict_city[oferta['city']] = 1
            else:
                dict_city[oferta['city']] += 1
            esta_entre_fechas_inicial_y_final = cmp_entre_fechas_inicial_y_final(fecha_inicial, oferta, fecha_final)
            if esta_entre_fechas_inicial_y_final:
                ofertas_periodo_pais += 1
                lt.addLast(listado_ofertas, oferta)

    ciudades_ofertas = len(dict_city)
    conteo_empresas_pais = lt.size(empresas_pais)
    llave_menor = min(dict_city, key=lambda k: dict_city[k])
    llave_mayor = max(dict_city, key=lambda k: dict_city[k])
    valor_menor = dict_city[llave_menor]
    valor_mayor = dict_city[llave_mayor]

    return ofertas_periodo_pais, conteo_empresas_pais, ciudades_ofertas, llave_mayor, valor_mayor, llave_menor, valor_menor, listado_ofertas

    
def req_5(data_structs, nombre_ciudad, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 5
    """
    ofertas_ciudad_y_periodo = 0
    dict_company_name = {}
    dict_city = {}
    listado_ofertas=lt.newList("ARRAY_LIST")
    
    for oferta in lt.iterator(data_structs["jobs"]):
        if cmp_entre_fechas_inicial_y_final(fecha_inicial, oferta, fecha_final):
            if nombre_ciudad == oferta["city"]:
                if oferta['city'] not in dict_city:
                    dict_city[oferta['city']] = 1
                else:
                    dict_city[oferta['city']] += 1

                if oferta['company_name'] not in dict_company_name:
                    dict_company_name[oferta['company_name']] = 1
                else:
                    dict_company_name[oferta['company_name']] += 1
                    ofertas_ciudad_y_periodo += 1
                    lt.addLast(listado_ofertas, oferta)
    
    conteo_empresas_ciudad = len(dict_city)
    llave_menor = min(dict_company_name, key=lambda k: dict_company_name[k])
    llave_mayor = max(dict_company_name, key=lambda k: dict_company_name[k])
    valor_menor = dict_company_name["llave_menor"]
    valor_mayor = dict_company_name["llave_mayor"]
    
    return ofertas_ciudad_y_periodo, conteo_empresas_ciudad, llave_mayor, valor_mayor, llave_menor, valor_menor, listado_ofertas


def req_6(data_structs, n, codigo_pais, nivel_experticia, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    ciudades_unicas = []
    for oferta in lt.iterator(data_structs["jobs"]):
        if (not codigo_pais) or (oferta['country_code'] == codigo_pais):
            if oferta['experience_level'] == nivel_experticia:
                fecha_oferta = oferta['published_at']
                if fecha_inicial <= fecha_oferta <= fecha_final:
                    ciudad = oferta['city']
                    if ciudad not in ciudades_unicas:
                        ciudades_unicas.append(ciudad)
    #Total de ciudades unicas
    ciudades_cumplen = len(ciudades_unicas)
    total_ciudades = min(ciudades_cumplen, n)
   # Filtrar las ofertas
    ofertas_filtradas = []
    for oferta in data_structs["jobs"]:
        if (not codigo_pais or oferta['country_code'] == codigo_pais) and oferta['experience_level'] == nivel_experticia:
            ofertas_filtradas.append(oferta)
    #El total de empresas que cumplen con las condiciones de la consulta
    empresas_unicas = []
    for oferta in ofertas_filtradas:
        empresa = oferta["company_name"]
        if empresa not in empresas_unicas:
            empresas_unicas.append(empresa)
    total_empresas = len(empresas_unicas)
    #El total de ofertas publicadas que cumplen con las condiciones de la consulta
    total_ofertas = len(ofertas_filtradas)
    # Promedio
    suma_salarios = 0
    conteo_salarios = 0
    for oferta in ofertas_filtradas:
        if 'salary_from' in oferta and 'salary_to' in oferta:
            suma_salarios += (oferta['salary_from'] + oferta['salary_to']) / 2
            conteo_salarios += 1
    promedio_salario_ofertado = None
    if conteo_salarios > 0:
        promedio_salario_ofertado = suma_salarios / conteo_salarios
    # Ciudad con mayor cantidad de ofertas
    ciudad_mas_ofertas = ofertas_filtradas['city'].value_counts().idxmax()
    total_ofertas_ciudad_mas = ofertas_filtradas['city'].value_counts().max()
    # Ciudad con menor cantidad de ofertas
    ciudad_menos_ofertas = ofertas_filtradas['city'].value_counts().idxmin()
    total_ofertas_ciudad_menos = ofertas_filtradas['city'].value_counts().min()
    #ordenar las cuidades
    conteo_ofertas_por_ciudad = {}
    for oferta in ofertas_filtradas:
        ciudad = oferta['city']
        if ciudad in conteo_ofertas_por_ciudad:
            conteo_ofertas_por_ciudad[ciudad] += 1
        else:
            conteo_ofertas_por_ciudad[ciudad] = 1
    lista_ciudades_conteo = list(conteo_ofertas_por_ciudad.items())
    ciudades_ordenadas = sorted(lista_ciudades_conteo, key=lambda x: x[1], reverse=True)

    return total_ciudades, total_empresas, total_ofertas, promedio_salario_ofertado, ciudad_mas_ofertas, total_ofertas_ciudad_mas, ciudad_menos_ofertas, total_ofertas_ciudad_menos, ciudades_ordenadas

def req_7(data_structs, n_paises, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 7
    """
    total_ofertas = 0
    dict_country_code = {}
    dict_city = {}
    dict_company_name = {}
    dict_skills = {}
    dict_multilocations_ids = {}
    niveles_de_experticia = ['junior', 'mid', 'senior']
    

    for oferta in lt.iterator(data_structs["jobs"]):
        if cmp_entre_fechas_inicial_y_final(fecha_inicial, oferta, fecha_final):
            if n_paises < len(dict_country_code):
                if oferta['country_code'] not in dict_country_code:
                    dict_country_code[oferta['country_code']] = 1
                    total_ofertas += 1

                else:
                    dict_country_code[oferta['country_code']] += 1
                    total_ofertas += 1

                    if oferta["city"] not in dict_city:
                        dict_city[oferta["city"]] = 1
                    else:
                        dict_city[oferta["city"]] += 1

                        for nivel in niveles_de_experticia:
                            if nivel == oferta['experience_level']:
                                for habilidad in lt.iterator(data_structs['skills']):
                                    if oferta['id'] == habilidad['id']:
                                        if habilidad["name"] not in dict_skills:
                                            dict_skills[habilidad["name"]] = 1
                                        else:
                                            dict_skills[habilidad["name"]] += 1

                                        if oferta['company_name'] not in dict_company_name:
                                                    dict_company_name[oferta['company_name']] = 1
                                        else:
                                            dict_company_name[oferta['company_name']] += 1

                                        for multilocation in lt.iterator(data_structs['multilocations']):
                                            if oferta['id'] == multilocation['id']:
                                                if multilocation["id"] not in dict_multilocations_ids:
                                                    dict_multilocations_ids[multilocation["id"]] = 1
                                                else:
                                                    dict_multilocations_ids[multilocation["id"]] += 1
                                   
    conteo_ciudades_ofertas_pais = len(dict_city)
    llave_mayor_country_code = max(dict_country_code, key=lambda k:dict_country_code[k])
    llave_mayor_city = max(dict_city, key=lambda k:dict_city[k])
    llave_mayor_skills = max(dict_city, key=lambda k:dict_city[k])
    llave_menor_skills = min(dict_city, key=lambda k:dict_city[k])

    valor_mayor_country = dict_country_code[llave_mayor_country_code]
    valor_mayor_city = dict_city[llave_mayor_city]
    valor_mayor_skills = dict_skills[llave_mayor_skills]
    valor_menor_skills = dict_skills[llave_menor_skills]

    promedio_nivel_skills = sum(dict_skills.values())//len(dict_skills)

    return total_ofertas, conteo_ciudades_ofertas_pais, llave_mayor_country_code, valor_mayor_country,\
           llave_mayor_city, valor_mayor_city, llave_mayor_skills, valor_mayor_skills,llave_menor_skills, valor_menor_skills, promedio_nivel_skills


# Funciones utilizadas para comparar elementos dentro de una lista
def cmp_entre_fechas_inicial_y_final(fecha_inicial, oferta, fecha_final):
    return (fecha_inicial[0:10] <= oferta['published_at'][0:10] <= fecha_final[0:10])

def cmp_fechas(oferta1, oferta2):
    return (oferta1['published_at'][0:10] < oferta2['published_at'][0:10])

def cmp_ofertas_by_fecha_y_codigo_pais(oferta1, oferta2):
    """
    Devuelve verdadero (True) si la fecha de publicación de la oferta1 es menor que en la
    oferta2, en caso de que sean iguales se analiza la empresa de la oferta
    laboral, de lo contrario devuelva falso (False).
    Args:
    oferta1: información de la primera oferta laboral que incluye
    "company_name" y "published_at"
    oferta1: información de la segunda oferta laboral que incluye
    "company_name" y "published_at"
    | """
    #Comparar las fechas de publicación
    if oferta1["published_at"] < oferta2["published_at"]:
        return True
    elif oferta1["published_at"] > oferta2["published_at"]:
        return False
        #Comparar los códigos de país
    else:
        return (oferta1["country_code"] < oferta2["country_code"])

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
    
    #Comparar fecha de publicacion
    else:
        return (oferta1["published_at"] < oferta2["published_at"])
    
def cmp_ofertas_by_fecha_y_empresa (oferta1, oferta2):
    """
    Devuelve verdadero (True) si la fecha de publicación de la oferta1 es menor que en la
    oferta2, en caso de que sean iguales se analiza la empresa de la oferta
    laboral, de lo contrario devuelva falso (False).
    Args:
    oferta1: información de la primera oferta laboral que incluye
    "company_name" y "published_at"
    oferta1: información de la segunda oferta laboral que incluye
    "company_name" y "published_at"
    | """
    #Comparar las fechas de publicación
    if oferta1["published_at"] < oferta2["published_at"]:
        return True
    elif oferta1["published_at"] > oferta2["published_at"]:
        return False
    
    #Comparar los nombres de las empresas
    else:
        return (oferta1["company_name"] < oferta2["company_name"])

def sublist(lst, pos, num):
    new_sublist = lt.subList(lst, pos, num)
    return new_sublist

def sort(lst, sort_crit):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    sa.sort(lst, sort_crit)