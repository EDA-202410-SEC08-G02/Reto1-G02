﻿"""
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
    """
        Función que imprime un dato dado su ID
    """
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

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


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
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

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
