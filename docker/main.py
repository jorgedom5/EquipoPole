import random
from faker import Faker
import psycopg2
import pandas as pd
from gender_guesser.detector import Detector
from unidecode import unidecode
import numpy as np

# CONFIGURACIÓN
fake = Faker('es_ES')  # Configura Faker para generar datos en español
gender_detector = Detector()

#CREACIÓN TABLAS

# TABLA JUBILADOS

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
    
def generar_historial():
  probabilidad = fake.random_int(1, 100)
  if probabilidad <= 0.8:
    return 2
  elif probabilidad <= 3.8:
    return 3
  elif probabilidad <= 4.58:
    return 4
  elif probabilidad <= 4.89:
    return 5
  else:
    return 1

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

def generar_estado_civil():
  prob = fake.random_int(1, 100)
  if prob <=  13.59: #revisar porcentaje dependiendo del viaje
    return 1 #SOLTERO
  elif prob <=  75.49: # revisar porcentaje dependiendo del viaje
    return 2 #CASADO
  else:  # revisar porcentaje dependiendo del viaje
    return 3 #VIUDO

def generar_pension_anual():
  prob = fake.random_int(1, 100)
  if prob <= 30:
    return fake.random_int(min=10963, max=16000)
  elif prob <=  75:
    return fake.random_int(min=16000, max=21500)
  elif prob <=  90:
    return fake.random_int(min=21500, max=27000)
  elif prob <=  97.5:
    return fake.random_int(min=27000, max=32000)
  else:  #
    return fake.random_int(min=32000, max=42823)

def generar_años_tributados():
  prob = fake.random_int(1, 100)
  if prob <= 5:
    return fake.random_int(min=15, max=20)
  elif prob <= 10:
    return fake.random_int(min=21, max=25)
  elif prob <= 17:
    return fake.random_int(min=26, max=30)
  elif prob <= 24:
    return fake.random_int(min=31, max=34)
  elif prob <= 43:
    return fake.random_int(min=35, max=39)
  else:
    return fake.random_int(min=40, max=44)

def generar_discapacidad():
  prob = fake.random_int(1, 100)
  if prob <= 4:
    return 1
  elif prob <= 11:
    return 2
  elif prob <=  29:
    return 3
  else:
    return 0

#TABLA EN SI

def generar_datos_jubilados(jubilado_id):
    nombre_con_acentos = fake.first_name()
    nombre_sin_acentos = unidecode(nombre_con_acentos)
    genero = gender_detector.get_gender(nombre_sin_acentos)
    edad = generar_edad()
    endeudamiento = fake.random_int(1, 100) <= 18 # Endeudamiento es True el 18% de los casos
    tipo_pensionista = fake.random_int(1, 6)
    historial_judicial = generar_historial()
    cantidad_hijos = generar_hijos()
    #lugar_residencia  = generar_lugar_residencia()
    participacion_voluntariado =  fake.random_int(1, 100) <=30
    estado_civil= generar_estado_civil()
    participacion_anterior=fake.random_int(1,100)<=15
    preferencia_internacional=fake.random_int(1,100)<=20 #True si prefieren viaje internacional el 20% de los casos
    #fumador = generar_fumador()
    #preferencia_viaje = generar_preferencia_viaje()
    pension_anual = generar_pension_anual()
    años_tributados = generar_años_tributados()
    maltrato = fake.random_int(1, 100) <= 1
    discapacidad = generar_discapacidad()
    return {
        'jubilado_id': jubilado_id,
        'nombre': nombre_sin_acentos,
        'apellido': fake.last_name(),
        'genero': genero,
        'edad': edad,
        'endeudamiento': endeudamiento,
        'tipo_pensionista': tipo_pensionista,
        'historial_judicial' : historial_judicial,
        'cantidad_hijos' : cantidad_hijos,
        #'Lugar de residencia': lugar_residencia,
        'participacion_voluntariado' : participacion_voluntariado,
        'estado_civil': estado_civil,
        'participacion_anterior': participacion_anterior,
        'preferencia_internacional': preferencia_internacional,
        #'Fumador': fumador,
        #'Preferencia viaje': preferencia_viaje,
        'pension_anual': pension_anual,
        'años_tributados': años_tributados,
        'maltrato': maltrato,
        'discapacidad': discapacidad

    }



# TABLA VIAJES

#crear datos dentro de la tabla
def generar_datos_viajes(viajes_id):
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
    host="postgres", #SI ES PARA EL DOCKER-COMPOSE, CAMBIAR POR "postgres"
    database="root",
    user="root",
    password="root",
    port="5432"
)

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# GENERAR TABLAS VACÍAS

# JUBILADOS
cursor.execute("""
    DROP TABLE IF EXISTS public.jubilados;
    
    CREATE TABLE IF NOT EXISTS public.jubilados (
        jubilado_id SERIAL PRIMARY KEY,
        nombre VARCHAR(255),
        apellido VARCHAR(255),
        genero VARCHAR(255),
        edad INTEGER,
        endeudamiento BOOLEAN,
        tipo_pensionista INTEGER,
        historial_judicial VARCHAR(255),
        cantidad_hijos INTEGER,
        participacion_voluntariado BOOLEAN,
        estado_civil VARCHAR(255),
        participacion_anterior BOOLEAN,
        preferencia_internacional BOOLEAN,
        pension_anual FLOAT,
        años_tributados INTEGER,
        maltrato BOOLEAN,
        discapacidad VARCHAR(255)
    );
""")

conn.commit()

# VIAJES
cursor.execute("""
    DROP TABLE IF EXISTS public.viajes;
    CREATE TABLE IF NOT EXISTS public.viajes (
        viajes_id SERIAL PRIMARY KEY,
        geografico_id INTEGER,
        tipo_turismo_id INTEGER,
        numero_dias INTEGER,
        transporte_pagado BOOLEAN,
        mes_id INTEGER,
        tipo_hotel_id INTEGER
    );
""")

# GEOGRAFICO
cursor.execute("""
    DROP TABLE IF EXISTS public.geografico;
    CREATE TABLE IF NOT EXISTS public.geografico (
        geografico_id SERIAL PRIMARY KEY,
        ciudad varchar(50),
        comunidad_autonoma varchar(50),
        es_costa BOOLEAN
    );
""")

# Commit para aplicar cambios en la base de datos
conn.commit()

# RELLENAR TABLAS

#JUBILADOS

for jubilado_id in range(1, 100001):
    datos_jubilados = generar_datos_jubilados(jubilado_id)
    cursor.execute("""
        INSERT INTO public.jubilados (
            jubilado_id, nombre, apellido, genero, edad, endeudamiento,
            tipo_pensionista, historial_judicial, cantidad_hijos,
            participacion_voluntariado, estado_civil, participacion_anterior,
            preferencia_internacional, pension_anual, años_tributados,
            maltrato, discapacidad
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        datos_jubilados['jubilado_id'], datos_jubilados['nombre'],
        datos_jubilados['apellido'], datos_jubilados['genero'],
        datos_jubilados['edad'], datos_jubilados['endeudamiento'],
        datos_jubilados['tipo_pensionista'], datos_jubilados['historial_judicial'],
        datos_jubilados['cantidad_hijos'], datos_jubilados['participacion_voluntariado'],
        datos_jubilados['estado_civil'], datos_jubilados['participacion_anterior'],
        datos_jubilados['preferencia_internacional'], datos_jubilados['pension_anual'],
        datos_jubilados['años_tributados'], datos_jubilados['maltrato'],
        datos_jubilados['discapacidad']
    ))

# VIAJES
for viajes_id in range(1, 151):
    datos = generar_datos_viajes(viajes_id)
    cursor.execute("""
        INSERT INTO public.viajes (
            viajes_id, geografico_id, tipo_turismo_id, numero_dias,
            transporte_pagado, mes_id, tipo_hotel_id
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        datos['viajes_id'], datos['geografico_id'], datos['tipo_turismo_id'],
        datos['numero_dias'], datos['transporte_pagado'], datos['mes_id'],
        datos['tipo_hotel_id']
    ))
    
#GEOGRAFICO
cursor.execute("""
    INSERT INTO public.geografico (geografico_id, ciudad, comunidad_autonoma, es_costa)
    VALUES
    (1, 'Almeria', 'Andalucia', true),
    (2, 'Cadiz', 'Andalucia', true),
    (3, 'Cordoba', 'Andalucia', false),
    (4, 'Granada', 'Andalucia', false),
    (5, 'Huelva', 'Andalucia', true),
    (6, 'Jaen', 'Andalucia', false),
    (7, 'Malaga', 'Andalucia', true),
    (8, 'Sevilla', 'Andalucia', false),
    (9, 'Huesca', 'Aragon', false),
    (10, 'Teruel', 'Aragon', false),
    (11, 'Zaragoza', 'Aragon', false),
    (12, 'Oviedo', 'Principado de Asturias', false),
    (13, 'Gijon', 'Principado de Asturias', true),
    (14, 'Mallorca', 'Islas Baleares', true),
    (15, 'Menorca', 'Islas Baleares', true),
    (16, 'Ibiza', 'Islas Baleares', true),
    (17, 'Formentera', 'Islas Baleares', true),
    (18, 'Las Palmas', 'Canarias', true),
    (19, 'Santa Cruz de Tenerife', 'Canarias', true),
    (20, 'El Hierro', 'Canarias', true),
    (21, 'La Gomera', 'Canarias', true),
    (22, 'Santander', 'Cantabria', true),
    (23, 'Albacete', 'Castilla-La Mancha', false),
    (24, 'Ciudad Real', 'Castilla-La Mancha', false),
    (25, 'Cuenca', 'Castilla-La Mancha', false),
    (26, 'Guadalajara', 'Castilla-La Mancha', false),
    (27, 'Toledo', 'Castilla-La Mancha', false),
    (28, 'Avila', 'Castilla y Leon', false),
    (29, 'Burgos', 'Castilla y Leon', false),
    (30, 'Leon', 'Castilla y Leon', false),
    (31, 'Palencia', 'Castilla y Leon', false),
    (32, 'Salamanca', 'Castilla y Leon', false),
    (33, 'Segovia', 'Castilla y Leon', false),
    (34, 'Soria', 'Castilla y Leon', false),
    (35, 'Valladolid', 'Castilla y Leon', false),
    (36, 'Zamora', 'Castilla y Leon', false),
    (37, 'Barcelona', 'Cataluna', true),
    (38, 'Gerona', 'Cataluna', false),
    (39, 'Lerida', 'Cataluna', false),
    (40, 'Tarragona', 'Cataluna', true),
    (41, 'Alicante', 'Comunidad Valenciana', true),
    (42, 'Castellon', 'Comunidad Valenciana', true),
    (43, 'Valencia', 'Comunidad Valenciana', true),
    (44, 'Badajoz', 'Extremadura', false),
    (45, 'Caceres', 'Extremadura', false),
    (46, 'La Coruna', 'Galicia', true),
    (47, 'Lugo', 'Galicia', true),
    (48, 'Orense', 'Galicia', true),
    (49, 'Pontevedra', 'Galicia', true),
    (50, 'Logrono', 'La Rioja', false),
    (51, 'Madrid', 'Comunidad de Madrid', false),
    (52, 'Murcia', 'Region de Murcia', true),
    (53, 'Cartagena', 'Region de Murcia', true),
    (54, 'Pamplona', 'Comunidad Foral de Navarra', true),
    (55, 'Alava', 'Pais Vasco', false),
    (56, 'Guipuzcoa', 'Pais Vasco', true),
    (57, 'Vizcaya', 'Pais Vasco', true),
    (58, 'Ceuta', 'Ceuta', true),
    (59, 'Melilla', 'Melilla', true),
    (60, 'Europa', 'Europa', true),
    (61, 'America', 'America', true),
    (62, 'Africa', 'Africa', true),
    (63, 'Oceania', 'Oceania', true);
""")

# Commit para aplicar cambios en la base de datos
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

print('DONE')
