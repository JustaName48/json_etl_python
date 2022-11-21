#!/usr/bin/env python
'''
JSON ETL [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 2.0

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "2.0"

import json
import requests


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #
    print('# ---- Ejemplos con JSON Request ---- #')

    # El .get() extrae toda la info de la URL. Lo guardo en la variable RESPONSE.
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    # Se puede obtener al JSON de dos formas distintas:
    # Usando RESPONSE y .json() des-serializo y detecto donde están los JSON
    # y los transforma en lista diccionario.
    data = json.loads(response.text) # Forma 1)
    data = response.json() # Forma 2) Lo obtengo en formato lista de diccionarios. Esta forma es mejor! + Portátil!
    print('Imprimir los datos traídos de la nube')
    # Con .dumps lo transformamos a los lista dicc en string y lo ordenamos.
    print(json.dumps(data, indent=4)) # Lo vuelvo a pasar a JSON y lo ordeno.

    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    # El request.get des-serealiza y obtenes una lista de diccionarios.
    data = response.json()

# Acá podemos hacer un filtrado de la información:
# Con un bucle for iteramos para mostrar en pantalla.
    for user in data:
        if user['userId'] > 2:
            # No mostrar más de 2 usuarios
            # para no ocupar toda la pantalla con mensajes
            break
        print('El usuario {} completó {}? {}'.format(user['userId'],
                                                      user['title'],
                                                      user['completed']
                                                      ))

    print("terminamos")
