import pandas as pd
from faker import Faker
from gender_guesser.detector import Detector
from unidecode import unidecode
import numpy as np

fake = Faker('es_ES')  # Configura Faker para generar datos en español
gender_detector = Detector()

#FUNCIÓN PARA CREAR EDAD POR PORCENTAJES

def generar_edad():
    prob = fake.random_int(1, 100)
    if prob <= 31.03: #7.57; 31.03 (0.2439)
        return fake.random_int(min=58, max=64)
    elif prob <= 52.5:  #5.48; 22.47
        return fake.random_int(min=65, max=69)
    elif prob <= 70.55:  #4.72; 19.35
        return fake.random_int(min=70, max=74)
    elif prob <= 85.5:  # 3.98; 16.32
        return fake.random_int(min=75, max=79)
    elif prob <= 95.52:  # 2.64; 10.82
        return fake.random_int(min=80, max=84)
    else:  # 4.48
        return fake.random_int(min=85, max=100)

# AQUÍ PARA CREAR COLUMNAS
def generar_datos():
    nombre_con_acentos = fake.first_name()
    nombre_sin_acentos = unidecode(nombre_con_acentos)
    genero = gender_detector.get_gender(nombre_sin_acentos)
    edad = generar_edad()
    endeudamiento = fake.random_int(1, 100) <= 18 # Endeudamiento es True el 18% de los casos
    return {
        'nombre': nombre_sin_acentos,
        'apellido': fake.last_name(),
        'genero': genero,
        'edad': edad,
        'endeudamiento': endeudamiento
    }
    
# 5000 filas de datos
datos = [generar_datos() for _ in range(5000)]
df = pd.DataFrame(datos)

# Guardar el DataFrame en un archivo CSV
df.to_csv('jubilados.csv', index=False)
print('DONE')