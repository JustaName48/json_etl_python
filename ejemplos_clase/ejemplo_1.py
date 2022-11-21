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
import os

os.chdir(os.path.dirname(__file__))


def json_create():
    # Ejemplos de como se construyen los JSON
    max_json = {
              "nombre": "Max",
              "apellido": "Power",
              "hijos": [
                    {
                     "firstName": "Alice",
                     "age": 6
                    },
                    {
                     "firstName": "Bob",
                     "age": 8
                    }
                    ]
              }

    emma_json = {
                 "nombre": "Emma",
                 "apellido": "Thompson",
                 "hijos": []
                 }

    json_test = {"max": max_json, "emma": emma_json}
# Con los dos diccionarios creamos una estructura más compleja, es decir un nuevo diccionario
# que tiene 2 elementos. En un diccionario unimos a dos elementos.

    print('Imprimir json como un objeto')
    print(emma_json)

    print('Convertir JSON a json_string e imprimir en pantalla')
    json_string = json.dumps(emma_json, indent=4)
    print(json_string)

    print('Imprimir json como un objeto')
    print(json_test)

    print('Convertir JSON a json_string e imprimir en pantalla')
    json_string = json.dumps(json_test, indent=4)
    print(json_string)


def json_serialize():
    # Generar un json y almacenarlo en archivo (dump)

    estudiante1 = {
                  "nombre": "Max",
                  "apellido": "Power",
                  "materias": [
                      {
                       "asignatura": "matematica",
                       "estado": "en curso"
                      },
                      {
                       "asignatura": "lengua",
                       "estado": "finalizado"
                      }
                      ]
                   }

    with open('mi_json.json', 'w') as jsonfile: # Creo un archivo tipo JSON.
        data = [estudiante1] # La data que se le pasa con .dump tiene que tener formato de lista!!!
        # Puede ser lista de diccionarois. No se le puede mandar un archivo tipo 
        # diccionario como estudiante1 a un .json, la data debe ser en forma de lista.
        json.dump(data, jsonfile, indent=4)


def json_deserialize():
    # Leer json y actualizarlo
    estudiante2 = {
                  "nombre": "Jean",
                  "apellido": "Gray",
                  "materias": [
                      {
                       "asignatura": "matematica",
                       "estado": "finalizado"
                      },
                      {
                       "asignatura": "lengua",
                       "estado": "finalizado"
                      }
                      ]
                   }

# 3 procesos: Abre archivo, identifica JSON y lo extra, añadir el segundo estudiante.
# En el primero leo la información del archivo JSON, le paso el nombre
# y el alias. Tengo que deserializar la información con el método LOAD.
# Nos quedamos solamente con lo que tenga formato tipo json, se identifica y se guarda.
# Al deserializar la información está en formato diccionario, lo que permite
# añadir o agregarle información con otro diccionario
# Se le agrega a la variable current_data la info del estudiante2 con append.
    with open('mi_json.json', 'r') as jsonfile:
        current_data = json.load(jsonfile) # Se extrae una lista de diccionarios
        current_data.append(estudiante2) # Por eso se puede usar append.

# Ahora se sobreescribe el archivo, se borra y empieza de vuelta.
# Le damos formato JSON a la información guardada
    with open('mi_json.json', 'w') as jsonfile:
        json.dump(current_data, jsonfile, indent=4)

    with open('mi_json.json', 'r') as jsonfile:
        json_data = json.load(jsonfile)

    print('Mostrar el contenido del archivo mi_json')
    print(json.dumps(json_data, indent=4))


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #
    print('# ---- Ejemplos con JSON ---- #')
    json_create()
    json_serialize()
    json_deserialize()

    print("terminamos")
