###ESTO ES LO QUE HEMOS HECHO PARA VIAJES
###SOLO ESTÁ CREADO VIAJES
###PARA IMPORTAR DIFERENTES CSV

import random
from faker import Faker
import psycopg2

# Inicializar Faker
fake = Faker()

#CREACIÓN TABLAS

# TABLA VIAJES

#crear datos dentro de la tabla
def generar_datos(viajes_id):
    geografico_id = random.randint(1, 64)
    tipo_turismo_id = random.randint(1, 4)
    numero_dias = random.randint(4, 10)
    transporte_pagado = fake.random_int(1, 100) <= 90
    mes_id = random.randint(1, 12)
    tipo_hotel_id = random.randint(1, 5)
    return {
        'viajes_id': viajes_id,
        'geografico_id': geografico_id,
        'tipo_turismo_id': tipo_turismo_id,
        'numero_dias': numero_dias,
        'transporte_pagado': transporte_pagado,
        'mes_id': mes_id,
        'tipo_hotel_id': tipo_hotel_id
    }


#POSTGRES

# Conectar a la base de datos PostgreSQL
conn = psycopg2.connect(
    host="postgres",
    database="root",
    user="root",
    password="root",
    port="5432"
)

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS viajes (
        viajes_id SERIAL PRIMARY KEY,
        geografico_id INTEGER,
        tipo_turismo_id INTEGER,
        numero_dias INTEGER,
        transporte_pagado BOOLEAN,
        mes_id INTEGER,
        tipo_hotel_id INTEGER
    )
""")

# Commit para aplicar cambios en la base de datos
conn.commit()

# Generar datos y guardar en la base de datos
for viajes_id in range(1, 5001):
    datos = generar_datos(viajes_id)
    cursor.execute("""
        INSERT INTO viajes (
            viajes_id, geografico_id, tipo_turismo_id, numero_dias,
            transporte_pagado, mes_id, tipo_hotel_id
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        datos['viajes_id'], datos['geografico_id'], datos['tipo_turismo_id'],
        datos['numero_dias'], datos['transporte_pagado'], datos['mes_id'],
        datos['tipo_hotel_id']
    ))

# Commit para aplicar cambios en la base de datos
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

print('DONE')