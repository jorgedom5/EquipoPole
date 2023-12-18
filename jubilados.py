import pandas as pd
from faker import Faker
from gender_guesser.detector import Detector
from unidecode import unidecode

fake = Faker('es_ES')  # Configura Faker para generar datos en español
gender_detector = Detector()

# AQUÍ PARA CREAR COLUMNAS
def generar_datos():
    nombre_con_acentos = fake.first_name()
    nombre_sin_acentos = unidecode(nombre_con_acentos)
    genero = gender_detector.get_gender(nombre_sin_acentos)
    return {
        'nombre': nombre_sin_acentos,
        'apellido': fake.last_name(),
        'genero': genero
    }
    
# 5000 filas de datos
datos = [generar_datos() for _ in range(5000)]
df = pd.DataFrame(datos)

# Guardar el DataFrame en un archivo CSV
df.to_csv('jubilados.csv', index=False)
