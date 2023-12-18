import pandas as pd
from faker import Faker
import random

fake = Faker('es_ES')  # Configura Faker para generar datos en español

#AQUI PARA CREAR COLUMNAS
def generar_datos():
    return {
        'nombre': fake.first_name(),
        'apellido': fake.last_name(),
    }
    

# 5000 filas de datos
datos = [generar_datos() for _ in range(5000)]
df = pd.DataFrame(datos)

# Guardar el DataFrame en un archivo CSV
df.to_csv('jubilados.csv', index=False)