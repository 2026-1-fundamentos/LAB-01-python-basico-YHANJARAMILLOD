"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_05():
    with open("files/input/data.csv", "r") as archivo:
        lector = csv.reader(archivo, delimiter='\t')
        contador = {}
        for columna in lector:
            if not columna.strip():
                continue
            letra = columna[0]
            valor = int(columna[1])
            if letra in contador:
                contador[letra].append(valor)
            else:
                contador[letra] = [valor]
        resultado = []
        for letra, valores in sorted(contador.items()):
            maximo = max(valores)
            minimo = min(valores)
            resultado.append((letra, maximo, minimo))
    return resultado
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
