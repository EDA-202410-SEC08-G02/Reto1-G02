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
import time
import csv
import os


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    control = {'model': None}
    control['model'] = model.new_data_structs()
    return control


# Funciones para la carga de datos
def load_data(control, jobs_path, skills_path, employments_types_path, multilocations_path):
    """
    Carga los datos del reto
    """
    jobs_size = load_jobs(control, jobs_path)
    skills_size = load_skills(control, skills_path)
    employments_types_size = load_employments_types(control, employments_types_path)
    multilocations_size = load_multilocations(control, multilocations_path)
    return jobs_size, skills_size, employments_types_size, multilocations_size

def load_jobs(control, jobs_path):
    data_structs = control['model']
    path = os.path.join(cf.data_dir, jobs_path)
    jobs_file = open(path, 'r', encoding='utf-8')
    input_file = csv.DictReader(jobs_file, delimiter=';')
    for job in input_file:
        model.add_job(data_structs, job)
    return model.job_size(data_structs)

def load_skills(control, skills_path):
    data_structs = control['model']
    path = os.path.join(cf.data_dir, skills_path)
    skills_file = open(path, 'r', encoding='utf-8')
    input_file = csv.DictReader(skills_file, delimiter=';', fieldnames=['name', 'level', 'id'])
    for skill in input_file:
        model.add_skill(data_structs, skill)
    return model.skill_size(data_structs)

def load_employments_types(control, employments_types_path):
    data_structs = control['model']
    path = os.path.join(cf.data_dir, employments_types_path)
    employment_types_file = open(path, 'r', encoding='utf-8')
    input_file = csv.DictReader(employment_types_file, delimiter=';')
    for employment_type in input_file:
        model.add_employment_type(data_structs, employment_type)
    return model.employment_type_size(data_structs)

def load_multilocations(control, multilocations_size):
    data_structs = control['model']
    path = os.path.join(cf.data_dir, multilocations_size)
    multilocations_file = open(path, 'r', encoding='utf-8')
    input_file = csv.DictReader(multilocations_file, delimiter=';', fieldnames=['city', 'street', 'id'])
    for multilocation in input_file:
        model.add_multilocation(data_structs, multilocation)
    return model.multilocation_size(data_structs)

# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass

def req_1(control, n_ofertas, codigo_pais, nivel_experticia):
    """
    Retorna el resultado del requerimiento 1
    """
    start_time = get_time()
    data_structs = control["model"]
    tupla_listado_ofertas = model.req_1(data_structs, n_ofertas, codigo_pais, nivel_experticia)
    stop_time = get_time()
    delta = delta_time(start_time, stop_time)
    return delta, tupla_listado_ofertas


def req_2(control, n_ofertas, nombre_empresa, city):
    """
    Retorna el resultado del requerimiento 2
    """
    start_time = get_time()
    data_structs = control["model"]
    tupla_listado_ofertas = model.req_2(data_structs, n_ofertas, nombre_empresa, city)
    stop_time = get_time()
    delta = delta_time(start_time, stop_time)
    return delta, tupla_listado_ofertas


def req_3(control, nombre_empresa, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 3
    """
    start_time = get_time()
    data_structs = control['model']
    tupla_listado_ofertas = model.req_3(data_structs, nombre_empresa, fecha_inicial, fecha_final)
    stop_time = get_time()
    delta = delta_time(start_time, stop_time)
    return delta, tupla_listado_ofertas


def req_4(control, codigo_pais, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 4
    """
    start_time = get_time()
    data_structs = control["model"]
    tupla_listado_ofertas = model.req_4(data_structs, codigo_pais, fecha_inicial, fecha_final)
    stop_time = get_time()
    delta = delta_time(start_time, stop_time)
    return delta, tupla_listado_ofertas


def req_5(control, nombre_ciudad, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 5
    """
    start_time = get_time()
    data_structs = control["model"]
    tupla_listado_ofertas = model.req_5(data_structs, nombre_ciudad, fecha_inicial, fecha_final)
    stop_time = get_time()
    delta = delta_time(start_time, stop_time)
    return delta, tupla_listado_ofertas


def req_6(control, n, codigo_pais, nivel_experticia, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 6
    """
    start_time = get_time()
    data_structs = control["model"]
    tupla_listado_ciudades = model.req_6(data_structs, codigo_pais, nivel_experticia, fecha_inicial, fecha_final)
    stop_time = get_time()
    delta = delta_time(start_time, stop_time)
    return delta, tupla_listado_ciudades


def req_7(control, n_paises, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 7
    """
    start_time = get_time()
    data_structs = control["model"]
    tupla_listado_ofertas = model.req7(data_structs, n_paises, fecha_inicial, fecha_final)
    stop_time = get_time()
    delta = delta_time(start_time, stop_time)
    return delta, tupla_listado_ofertas


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
