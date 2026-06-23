"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    with open("files/input/data.csv", "r") as archivo:
        resultado = []
        for linea in archivo:
            if not linea.strip():
                continue
            columna = linea.split('\t')
            letra = columna[0]
            cantidad_columna_4 = len(columna[3].split(','))
            cantidad_columna_5 = len(columna[4].split(','))
            resultado.append((letra, cantidad_columna_4, cantidad_columna_5))
    return resultado    
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
