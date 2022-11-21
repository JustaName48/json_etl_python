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

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def extract(url):
    # Extraer el JSON de la URL pasada
    # como parámetro
    response = requests.get(url)
    data = response.json()
    return data
# Recibimos los datos.

def transform(data):
    # Transformar los datos en dos vectores
    # para graficar
    x = [d['time'] for d in data]
    y = [d['signal'] for d in data]
    return x, y
# d es la variable que recorre todos los diccionarios, para la primer iteración
# d será el primer diccionario dentro de data.
# data es una lista de diccionarios, recorremos los diccionarios dentro de data con d y
# nos quedamos con el valor del "time".
# La función devuelve x e y, siendo cada uno una lista con los valores
# de "time" y "signal" respectivamente. 

def load(x ,y):
    # El código a continuación es especial
    # para animaciones de gráficos de línea.
    line.set_data(x, y) # Recibe los valores de x e y y los carga en un gráfico animado.
    fig.gca().relim()
    fig.gca().autoscale_view()
    return line,

# Si queremos hacer el gráfico estático:
"""
    def load(x ,y):
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.plot(x, y)
        plt.show()

"""

def update_animation(frame): # Esto es ETL.
    # Leer la data del sensor en la nube
    url = 'http://inove.pythonanywhere.com/monitor/sensor'
    data = extract(url)

    # Transformar la información para graficar
    x, y = transform(data)

    # Graficar la animación
    return load(x, y)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #
    print('# ---- Ejemplos con JSON ETL ---- #')

    # Crear el gráfico
    data = [] # Inicializamos con una varible vacía.

    fig = plt.figure()
    line, = plt.plot(data)

    # Graficar
    animation = FuncAnimation(fig, update_animation, interval=1000)
    plt.show()

    print("terminamos")

# VERSIÓN 2 DE ESTE EJERCICIO: Con Gráfico Estático #

JSON ETL [Python]
Ejemplos de clase
---------------------------
# Autor: Inove Coding School
# Version: 2.0

#Descripcion:
# Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "2.0"

import json
import requests

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def extract(url):
    # Extraer el JSON de la URL pasada
    # como parámetro
    response = requests.get(url)
    data = response.json()
    return data


def transform(data):
    # Transformar los datos en dos vectores
    # para graficar
    '''
    data =[{"time": 55.01,"signal": 794,"peak": 0,"hr": 70.03891050583658,"sample_rate": 100},....]
    d = {"time": 55.01,"signal": 794,"peak": 0,"hr": 70.03891050583658,"sample_rate": 100}
    d['time']
    55.01
    '''
    x = [d['time'] for d in data]  
    y = [d['signal'] for d in data]
    '''
    data =[{"time": 55.01,"signal": 794,"peak": 0,"hr": 70.03891050583658,"sample_rate": 100},....]
    d = {"time": 55.01,"signal": 794,"peak": 0,"hr": 70.03891050583658,"sample_rate": 100}
    d['signal']
    794
    '''
    return x, y


def load(x ,y):
    pass





if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #
    print('# ---- Ejemplos con JSON ETL ---- #')

    # Crear el gráfico
    data = []
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

import matplotlib.pyplot as plt

def extract(url):
    # Extraer el JSON de la URL pasada
    # como parámetro
    response = requests.get(url)
    data = response.json()
    return data


def transform(data):
    # Transformar los datos en dos vectores
    # para graficar
    '''
    data =[{"time": 55.01,"signal": 794,"peak": 0,"hr": 70.03891050583658,"sample_rate": 100},....]
    d = {"time": 55.01,"signal": 794,"peak": 0,"hr": 70.03891050583658,"sample_rate": 100}
    d['time']
    55.01
    '''
    x = [d['time'] for d in data]  
    y = [d['signal'] for d in data]
    '''
    data =[{"time": 55.01,"signal": 794,"peak": 0,"hr": 70.03891050583658,"sample_rate": 100},....]
    d = {"time": 55.01,"signal": 794,"peak": 0,"hr": 70.03891050583658,"sample_rate": 100}
    d['signal']
    794
    '''
    return x, y


def load(x ,y):
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(x, y)
    plt.show()



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print('# ---- Ejemplos con JSON ETL ---- #')
   
    # Leer la data del sensor en la nube
    url = 'http://inove.pythonanywhere.com/monitor/sensor'
    data = extract(url)

    # Transformar la información para graficar
    x, y = transform(data)

    # Graficar la anumación
    load(x, y)

    print("Terminamos")
