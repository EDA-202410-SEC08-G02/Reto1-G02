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
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


control = None

def new_controller():
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller()
    return control

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Listar las últimas N ofertas de trabajo según su país y nivel de experticia")
    print("3- Listar las últimas N ofertas de trabajo por empresa y ciudad")
    print("4- Consultar las ofertas que publicó una empresa durante un periodo especifico de tiempo")
    print("5- Consultar las ofertas que se publicaron en un país durante un periodo de tiempo")
    print("6- Consultar las ofertas que se publicaron en una ciudad durante un periodo de tiempo")
    print("7- Clasificar las N ciudades con mayor número de ofertas de trabajo por experticia entre un rango de fechas")
    print("8- Clasificar los N países con mayor número de ofertas de trabajo por divisa")
    print("9- Identificación de los países con mayor y menor ofertas de trabajo en un rango de fechas")
    print("0- Salir")

def load_data(control, size):
    """
    Carga los datos
    """
    jobs_size, skills_size, employments_types_size, multilocations_size = controller.load_data(control,
                        jobs_path=size + '-jobs.csv',
                        skills_path=size + '-skills.csv',
                        employments_types_path=size + '-employments_types.csv',
                        multilocations_path=size + '-multilocations.csv')
    return jobs_size, skills_size, employments_types_size, multilocations_size

def print_jobs(control, pos, id):
    jobs = control['model']['jobs']
    jobs_sublist = lt.subList(jobs, pos, id)
    headers = {'Fecha de publicación': [],
               'Título de la oferta': [],
               'Nombre de la empresa que publica': [],
               'Nivel de experticia de la oferta': [],
               'País de la oferta': [],
               'Ciudad de la oferta': []}
    
    for job in lt.iterator(jobs_sublist):
        headers['Fecha de publicación'].append(job['published_at'])
        headers['Título de la oferta'].append(job['title'])
        headers['Nombre de la empresa que publica'].append(job['company_name'])
        headers['Nivel de experticia de la oferta'].append(job['experience_level'])
        headers['País de la oferta'].append(job['country_code'])
        headers['Ciudad de la oferta'].append(job['city'])

    print(tabulate(headers, headers='keys'))


def print_req_1(control, n_ofertas, codigo_pais, nivel_experticia):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    delta, tupla_listado_ofertas = controller.req_1(control, n_ofertas, codigo_pais, nivel_experticia)

    print(f'El total de ofertas de trabajo ofrecidas según la condición {nivel_experticia} es {tupla_listado_ofertas[0]}.\n')
    print(f"Listado de ofertas publicadas ordenados cronológicamente:\n")
    headers = {'Fecha de publicación de la oferta': [],
               'Título de la oferta': [],
               'Nombre de la empresa de la oferta': [],
               'Nivel de experticia de la oferta': [],
               'País de la empresa de la oferta': [],
               'Ciudad de la empresa de la oferta': [],
               'Tamaño de la empresa de la oferta': [], 
               'Tipo de ubicación de trabajo': [],
               'Disponible a contratar ucranianos': []}
    
    for oferta in lt.iterator(tupla_listado_ofertas[1]):
        headers['Fecha de publicación de la oferta'].append(oferta['published_at'])
        headers['Título de la oferta'].append(oferta['title'])
        headers['Nombre de la empresa de la oferta'].append(oferta['company_name'])
        headers['Nivel de experticia de la oferta'].append(oferta['experience_level'])
        headers['Ciudad de la oferta'].append(oferta['city'])
        headers['País de la empresa de la oferta'].append(oferta['country_code'])
        headers['Ciudad de la empresa de la oferta'].append(oferta['city'])
        headers['Tamaño de la empresa de la oferta'].append(oferta['company_size'])
        headers['Tipo de ubicación de trabajo'].append(oferta['workplace_type'])
        headers['Disponible a contratar ucranianos'].append(oferta['open_to_hire_ukrainians'])
    
    print(tabulate(headers, headers='keys'))
    print(delta)

def print_req_2(control, n_ofertas, nombre_empresa, city):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    tupla_listado_ofertas = controller.req_2(control, n_ofertas, nombre_empresa, city)

    print(f'El total de ofertas ofrecidas por la empresa y ciudad es {tupla_listado_ofertas[0]}.\n')
    headers = {'Fecha de publicación': [],
               'Título de la oferta': [],
               'Nombre de la empresa que publica': [],
               'Nivel de experticia de la oferta': [],
               'Ciudad de la oferta': [],
               'País de la oferta': [],
               'Formato de aplicacion de la oferta': [],
               'Tipo de lugar de trabajo de la oferta': []}
    for oferta in lt.iterator(tupla_listado_ofertas[1]):
        headers['Fecha de publicación'].append(oferta['published_at'])
        headers['Título de la oferta'].append(oferta['title'])
        headers['Nombre de la empresa que publica'].append(oferta['company_name'])
        headers['Nivel de experticia de la oferta'].append(oferta['experience_level'])
        headers['Ciudad de la oferta'].append(oferta['city'])
        headers['País de la oferta'].append(oferta['country_code'])
        headers['Formato de aplicacion de la oferta'].append(oferta['display_offer'])
        headers['Tipo de lugar de trabajo de la oferta'].append(oferta['workplace_type'])

    print(tabulate(headers, headers='keys'))


def print_req_3(control, nombre_empresa, fecha_inicial, fecha_final):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    tupla_listado_ofertas = controller.req_3(control, nombre_empresa, fecha_inicial, fecha_final)

    print(f'El número total de ofertas es {tupla_listado_ofertas[0]}.\n')
    print(f'El número total de ofertas con experticia junior es {tupla_listado_ofertas[3]}.\n')
    print(f'El número total de ofertas con experticia mid es {tupla_listado_ofertas[2]}.\n')
    print(f'El número total de ofertas con experticia senior es {tupla_listado_ofertas[1]}.\n')

    headers = {'Fecha de publicación': [],
               'Título de la oferta': [],
               'Nombre de la empresa que publica': [],
               'Nivel de experticia de la oferta': [],
               'Ciudad de la oferta': [],
               'País de la oferta': [],
               'Tamaño de la empresa de la oferta': [],
               'Tipo de lugar de trabajo de la oferta': [],
               'Disponible a contratar ucranianos (Verdadero o Falso)': []}
    
    for oferta in lt.iterator(tupla_listado_ofertas[4]):
        headers['Fecha de publicación'].append(oferta['published_at'])
        headers['Título de la oferta'].append(oferta['title'])
        headers['Nombre de la empresa que publica'].append(oferta['company_name'])
        headers['Nivel de experticia de la oferta'].append(oferta['experience_level'])
        headers['Ciudad de la oferta'].append(oferta['city'])
        headers['País de la oferta'].append(oferta['country_code'])
        headers['Tamaño de la empresa de la oferta'].append(oferta['company_size'])
        headers['Tipo de lugar de trabajo de la oferta'].append(oferta['workplace_type'])
        headers['Disponible a contratar ucranianos (Verdadero o Falso)'].append(oferta['open_to_hire_ukrainians'])

    print(tabulate(headers, headers='keys'))

def print_req_4(control, codigo_pais, fecha_inicial, fecha_final):
    """
    Función que imprime la solución del Requerimiento 4 en consola
    """
    tupla_listado_ofertas = controller.req_4(control, codigo_pais, fecha_inicial, fecha_final)

    print(f"El total de ofertas en el país en el período de consulta es {tupla_listado_ofertas[0]}\n.")
    print(f"El total de empresas que publicaron al menos una oferta es {tupla_listado_ofertas[1]}\n.")
    print(f"El número total de ciudades del país en las que se publicaron ofertas es {tupla_listado_ofertas[2]}\n.")
    print(f"La ciudad del país con mayor número de ofertas es {tupla_listado_ofertas[3]} con {tupla_listado_ofertas[4]} ofertas\n.")
    print(f"La ciudad del país con menor número de ofertas es {tupla_listado_ofertas[5]} con {tupla_listado_ofertas[6]} ofertas\n.")
    print(f"Listado de ofertas publicadas ordenados cronológicamente:\n")
    
    headers = {"Fecha de publicación de la oferta: ": [],
               "Título de la oferta: ": [],
               "Nivel de experticia requerido: ": [],
               "Nombre de la empresa de la oferta: ": [],
               "Ciudad de la empresa de la oferta: ": [],
               "Tipo de lugar de trabajo de la oferta: ": [],
               "Tipo de trabajo (remoto o no): ": [],
               "Disponible a contratar ucranianos: ": []}
    
    for oferta in lt.iterator(tupla_listado_ofertas[7]):
        headers["Fecha de publicación de la oferta: "].append(oferta['published_at'])
        headers["Título de la oferta: "].append(oferta['title'])
        headers["Nivel de experticia requerido: "].append(oferta['experience_level'])
        headers["Nombre de la empresa de la oferta: "].append(oferta['company_name'])
        headers["Ciudad de la empresa de la oferta: "].append(oferta['city'])
        headers["Tipo de lugar de trabajo de la oferta: "].append(oferta['workplace_type'])
        headers["Tipo de trabajo (remoto o no): "].append(oferta['remote_interview'])
        headers["Disponible a contratar ucranianos: "].append(oferta['open_to_hire_ukrainians'])
    
    print(tabulate(headers, headers='keys'))

def print_req_5(control, nombre_ciudad, fecha_inicial, fecha_final):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    tupla_listado_ofertas = controller.req_5(control, nombre_ciudad, fecha_inicial, fecha_final)
    print(f'El número total de ofertas de una ciudad en un periodo es {tupla_listado_ofertas[0]}.\n')
    print(f'El número total de empresas que publicaron por lo menos una oferta en la ciudad de consulta es {tupla_listado_ofertas[1]}.\n')
    print(f'La empresa con mayor número de ofertas y su conteo es {tupla_listado_ofertas[2][3]}.\n')
    print(f'La empresa con mayor número de ofertas y su conteo es {tupla_listado_ofertas[4][5]}.\n')
    headers = {'Fecha de publicación': [],
               'Título de la oferta': [],
               'Nombre de la empresa que publica': [],
               'Tamaño de la empresa de la oferta': [],
               'Tipo de lugar de trabajo de la oferta': []}
    
    for oferta in lt.iterator(tupla_listado_ofertas[4]):
        headers['Fecha de publicación'].append(oferta['published_at'])
        headers['Título de la oferta'].append(oferta['title'])
        headers['Nombre de la empresa que publica'].append(oferta['company_name'])
        headers['Tamaño de la empresa de la oferta'].append(oferta['company_size'])
        headers['Tipo de lugar de trabajo de la oferta'].append(oferta['workplace_type'])
    print(tabulate(headers, headers='keys'))


def print_req_6(control, n, codigo_pais, nivel_experticia, fecha_inicial, fecha_final):
    """
    Función que imprime la solución del Requerimiento 6 en consola
    """
    tupla_listado_ciudades = controller.req_6(control, n, codigo_pais, nivel_experticia, fecha_inicial, fecha_final)
    print(f'El total de ciudades que cumplen con las condiciones de la consulta es: {tupla_listado_ciudades["total_ciudades"]}.\n')
    print(f'El total de empresas que cumplen con las condiciones de la consulta es: {tupla_listado_ciudades["total_empresas"]}.\n')
    print(f'El total de ofertas publicadas que cumplen con las condiciones de la consulta es: {tupla_listado_ciudades["total_ofertas"]}.\n')
    
    for ciudad_info in tupla_listado_ciudades["ciudades_ordenadas"]:
        ciudad, info = ciudad_info
        print(f'Ciudad: {ciudad}')
        print(f'Total de ofertas: {info["total_ofertas"]}')
        print(f'Promedio de salario ofertado: {info["promedio_salario"]}')
        print(f'Número de empresas que publicaron al menos una oferta: {len(info["empresas"])}')
        print(f'Empresa con mayor número de ofertas: {info["empresa_mas_ofertas"]} ({info["total_ofertas_empresa_mas"]} ofertas)')
        print(f'Mejor oferta por salario: {info["mejor_oferta"]}')
        print(f'Peor oferta por salario: {info["peor_oferta"]}\n')


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass




# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            size = input('Tamaño del archivo CSV: ')
            jobs_size, skills_size, employment_types_size, multilocations_size = load_data(control, size)

            print(f'El total de registros de ofertas de trabajo es {jobs_size}')
            print_jobs(control, 1, 3)
            print_jobs(control, jobs_size-2, 3)

        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            nombre_empresa = input('Nombre de la empresa: ')
            fecha_inicial = input('Fecha inicial: ')
            fecha_final = input('Fecha final: ')
            print_req_3(control, nombre_empresa, fecha_inicial, fecha_final)

        elif int(inputs) == 5:
            codigo_pais = input('Código del país: ')
            fecha_inicial = input('Fecha inicial: ')
            fecha_final = input('Fecha final: ')
            print_req_4(control, codigo_pais, fecha_inicial, fecha_final)

        elif int(inputs) == 6:
            n = input('Numero de ciudades para la consulta:')
            codigo_pais = input('Codigo del pais:')
            nivel_experticia = input('Nivel de experticia de las ofertas de interés:')
            fecha_inicial = input('Fecha inicial:')
            fecha_final = input('Fecha final:')
            print_req_5(control,n, codigo_pais, nivel_experticia, fecha_inicial, fecha_final)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
