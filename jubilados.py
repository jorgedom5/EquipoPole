import pandas as pd
from faker import Faker
from gender_guesser.detector import Detector
from unidecode import unidecode
import numpy as np

fake = Faker('es_ES')  # Configura Faker para generar datos en español
gender_detector = Detector()

# FUNCIÓN PARA CREAR EDAD POR PORCENTAJES
def generar_edad():
    prob = fake.random_int(1, 100)
    if prob <= 31.03:  # 7.57; 31.03 (0.2439)
        return fake.random_int(min=58, max=64)
    elif prob <= 52.5:  # 5.48; 22.47
        return fake.random_int(min=65, max=69)
    elif prob <= 70.55:  # 4.72; 19.35
        return fake.random_int(min=70, max=74)
    elif prob <= 85.5:  # 3.98; 16.32
        return fake.random_int(min=75, max=79)
    elif prob <= 95.52:  # 2.64; 10.82
        return fake.random_int(min=80, max=84)
    else:  # 4.48
        return fake.random_int(min=85, max=100)
    
# FUNCIÓN PARA CREAR HISTORIAL DELITOS POR PORCENTAJES
def generar_historial_delitos():
    probabilidad = fake.random_int(1, 100)
    if probabilidad <= 0.8:
        return 1
    elif probabilidad <= 3.8:
        return 2
    elif probabilidad <= 4.58:
        return 3
    elif probabilidad <= 4.89:
        return 4
    else:
        return 0

#FUNCIÓN PARA CREAR HIJOS POR PORCENTAJES
def generar_hijos():
    prob = fake.random_int(1, 100)
    if prob <= 18.65 :
        return 0
    elif prob <= 44.21 :
        return 1
    elif prob <= 87.58 :
        return 2
    elif prob <= 90.58:
        return 3
    elif prob <= 93.58:
        return 4
    elif prob <= 96.58:
        return 5
    else:
        return fake.random_int(min=6, max=8)

# AQUÍ PARA CREAR COLUMNAS
def generar_datos(jubilado_id):
    nombre_con_acentos = fake.first_name()
    nombre_sin_acentos = unidecode(nombre_con_acentos)
    genero = gender_detector.get_gender(nombre_sin_acentos)
    edad = generar_edad()
    hijos = generar_hijos()
    endeudamiento = fake.random_int(1, 100) <= 18  # Endeudamiento es True el 18% de los casos
    delitos = generar_historial_delitos()
    participacion_voluntariado =  fake.random_int(1, 100) <=4.4 # 4% de personas son voluntarias
    return {
        'jubilado_id': jubilado_id,
        'nombre': nombre_sin_acentos,
        'apellido': fake.last_name(),
        'genero': genero,
        'edad': edad,
        'hijos': hijos,
        'endeudamiento': endeudamiento,
        'historial_delitos': delitos,
        'voluntario': participacion_voluntariado
    }

# 5000 filas de datos con 'jubilado_id'
datos = [generar_datos(jubilado_id) for jubilado_id in range(1, 5001)]
df = pd.DataFrame(datos)

# Guardar el DataFrame en un archivo CSV
df.to_csv('jubilados_provisional.csv', index=False)
print('DONE')
