import random
from faker import Faker
import psycopg2
import pandas as pd
from gender_guesser.detector import Detector
from unidecode import unidecode
import numpy as np

random.seed(42) #OBTENER LO MISMO SIEMRPE

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
 
# FUNCIÓN PARA CREAR HISTORIAL DELITOS POR PORCENTAJES   

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

# FUNCIÓN PARA CREAR NUMERO DE HIJOS POR PORCENTAJES

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

# FUNCIÓN PARA CREAR EL ESTADO CIVIL POR PORCENTAJES

def generar_estado_civil():
  prob = fake.random_int(1, 100)
  if prob <=  13.59: #revisar porcentaje dependiendo del viaje
    return 1 #SOLTERO
  elif prob <=  75.49: # revisar porcentaje dependiendo del viaje
    return 2 #CASADO
  else:  # revisar porcentaje dependiendo del viaje
    return 3 #VIUDO

# FUNCIÓN PARA CREAR LA PENSIÓN ANUAL POR PORCENTAJES
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
  
# FUNCIÓN PARA CREAR LOS AÑOS TRIBUTADOS POR PORCENTAJES
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

# FUNCIÓN PARA CREAR SI HAY DISCAPACIDAD POR PORCENTAJES
def generar_discapacidad():
  prob = fake.random_int(1, 100)
  if prob <= 4:
    return 2
  elif prob <= 11:
    return 3
  elif prob <=  29:
    return 4
  else:
    return 1

# FUNCIÓN PARA CREAR LUGARES DONDE RESIDEN POR PORCENTAJES
def generar_geografico():
    prob = fake.random_int(1, 100)
    if prob <= 17.82:
        # Regiones de Andalucía
        return fake.random_int(1, 8)
    elif prob <= 22.57:
        # Regiones de Aragón
        return fake.random_int(9, 11)
    elif prob <= 26.76:
        # Regiones de Asturias
        return fake.random_int(12, 13)
    elif prob <= 31.57:
        # Regiones de Islas Baleares
        return fake.random_int(14, 17)
    elif prob <= 35.76:
        # Regiones de Canarias
        return fake.random_int(18, 21)
    elif prob <= 38.95:
        # Regiones de Cantabria
        return 22
    elif prob <= 42.14:
        # Regiones de Castilla-La Mancha
        return fake.random_int(23, 26)
    elif prob <= 46.03:
        # Regiones de Castilla y León
        return fake.random_int(28, 35)
    elif prob <= 60.62:
        # Regiones de Cataluña
        return fake.random_int(37, 39)
    elif prob <= 65.81:
        # Regiones de Comunidad Valenciana
        return fake.random_int(41, 42)
    elif prob <= 68.20:
        # Regiones de Extremadura
        return 44
    elif prob <= 70.85:
        # Regiones de Galicia
        return fake.random_int(46, 48)
    elif prob <= 72.14:
        # Regiones de La Rioja
        return 50
    elif prob <= 84.95:
        # Regiones de Comunidad de Madrid
        return 51
    elif prob <= 86.34:
        # Regiones de Región de Murcia
        return fake.random_int(52, 52)
    elif prob <= 89.53:
        # Regiones de Comunidad Foral de Navarra
        return 54
    elif prob <= 92:
        # Regiones de País Vasco
        return fake.random_int(55, 57)
    elif prob <= 97:
        # Regiones de Ceuta
        return 58
    elif prob <= 98:
        # Regiones de Melilla
        return 59
    else:
        # Regiones de Europa, América, África, Oceania
        return fake.random_int(60, 63)  
    
# FUNCIÓN PARA CREAR ENFERMEDADES
def generar_enfermedades():
    probabilidad = random.randint(1, 100)
    if probabilidad <= 27:
        return 1 #Ninguna
    elif probabilidad <= 71:
        return 2 #Leve
    elif probabilidad <= 88:
        return 3 #Media
    else:
        return 4 #Grave

#FUNCIÓN PARA CREAR NUMERO DE PROPIEDADES POR PORCENTAJES  
def generar_numero_propiedades(): #realizado actual
    prob = fake.random_int(1, 100)
    if prob <= 45 :
        return 1
    elif prob <= 85 :
        return 2
    elif prob <= 88 :
        return 3
    elif prob <= 91:
        return 4
    elif prob <= 94:
        return 5
    elif prob <= 97:
        return 6
    else:
        return 0
  
#TABLA EN SI

def generar_datos_jubilados(jubilado_id):
    nombre_con_acentos = fake.first_name()
    nombre_sin_acentos = unidecode(nombre_con_acentos)
    genero = gender_detector.get_gender(nombre_sin_acentos)
    edad = generar_edad()
    endeudamiento = fake.random_int(1, 100) <= 18 # Endeudamiento es True el 18% de los casos
    historial_judicial = generar_historial()
    cantidad_hijos = generar_hijos()
    geografico_id = generar_geografico()
    participacion_voluntariado =  fake.random_int(1, 100) <=30
    estado_civil= generar_estado_civil()
    participacion_anterior=fake.random_int(1,100)<=15
    preferencia_internacional=fake.random_int(1,100)<=20 #True si prefieren viaje internacional el 20% de los casos
    fumador = fake.random_int(1, 100) <=17 #FUMADOR 17% DE LAS VECES
    preferencia_viaje = random.randint(1, 150)
    preferencia_viaje2 = random.randint(1, 150)
    preferencia_viaje3= random.randint(1, 150)
    while preferencia_viaje2 == preferencia_viaje:
      preferencia_viaje2 = random.randint(1, 150)
    while preferencia_viaje3 == preferencia_viaje:
      preferencia_viaje3 = random.randint(1, 150)
    while preferencia_viaje3==preferencia_viaje2:
       preferencia_viaje3= random.randint(1, 150)
    pension_anual = generar_pension_anual()
    años_tributados = generar_años_tributados()
    maltrato = fake.random_int(1, 100) <= 1
    discapacidad = generar_discapacidad()
    enfermedad = generar_enfermedades()
    numero_propiedades = generar_numero_propiedades()
    nacionalidad_española = fake.random_int(1, 100) <=98 #ESPAÑOL 98% DE LAS VECES
    return {
        'jubilado_id': jubilado_id,
        'nombre': nombre_sin_acentos,
        'apellido': fake.last_name(),
        'genero': genero,
        'edad': edad,
        'endeudamiento': endeudamiento,
        'historial_judicial_id' : historial_judicial,
        'cantidad_hijos' : cantidad_hijos,
        'geografico_id': geografico_id,
        'participacion_voluntariado' : participacion_voluntariado,
        'estado_civil_id': estado_civil,
        'participacion_anterior': participacion_anterior,
        'preferencia_internacional': preferencia_internacional,
        'fumador': fumador,
        'preferencia_viaje_1': preferencia_viaje,
        'preferencia_viaje_2': preferencia_viaje2,
        'preferencia_viaje_3': preferencia_viaje3,
        'pension_anual': pension_anual,
        'años_tributados': años_tributados,
        'maltrato': maltrato,
        'tipo_discapacidad_id': discapacidad,
        'enfermedad_id': enfermedad,
        'numero_propiedades': numero_propiedades,
        'nacionalidad_española': nacionalidad_española

    }



# TABLA VIAJES

#crear datos dentro de la tabla
def generar_datos_viajes(viajes_id):
    geografico_id = random.randint(1, 63)
    tipo_turismo_id = random.randint(1, 4)
    numero_dias = random.randint(4, 10)
    transporte_pagado = fake.random_int(1, 100) <= 90
    mes_id = random.randint(1, 12)
    tipo_hotel_id = random.randint(1, 5)
    numero_plazas =random.randint(10,25)
    return {
        'viajes_id': viajes_id,
        'geografico_id': geografico_id,
        'tipo_turismo_id': tipo_turismo_id,
        'numero_dias': numero_dias,
        'transporte_pagado': transporte_pagado,
        'mes_id': mes_id,
        'tipo_residencia_id': tipo_hotel_id,
        'numero_plazas':numero_plazas
    }


#POSTGRES

# Conectar a la base de datos PostgreSQL
conn = psycopg2.connect(
    host="postgres", #SI ES PARA EL DOCKER-COMPOSE, CAMBIAR POR "postgres", en local igual a "localhost"
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
        historial_judicial_id INTEGER,
        cantidad_hijos INTEGER,
        geografico_id INTEGER,
        participacion_voluntariado BOOLEAN,
        estado_civil_id INTEGER,
        participacion_anterior BOOLEAN,
        preferencia_internacional BOOLEAN,
        fumador BOOLEAN,
        preferencia_viaje_1 INTEGER,
        preferencia_viaje_2 INTEGER,
        preferencia_viaje_3 INTEGER,
        pension_anual FLOAT,
        años_tributados INTEGER,
        maltrato BOOLEAN,
        tipo_discapacidad_id INTEGER,
        enfermedad_id INTEGER,
        numero_propiedades INTEGER,
        nacionalidad_española BOOLEAN
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
        tipo_residencia_id INTEGER,
        numero_plazas INTEGER  );
""")

# Commit para aplicar cambios en la base de datos
conn.commit()

# RELLENAR TABLAS

#JUBILADOS

#JUBILADOS

for jubilado_id in range(1, 100001):
    datos_jubilados = generar_datos_jubilados(jubilado_id)
    cursor.execute("""
        INSERT INTO public.jubilados (
            jubilado_id, nombre, apellido, genero, edad, endeudamiento,
            historial_judicial_id, cantidad_hijos, geografico_id,
            participacion_voluntariado, estado_civil_id, participacion_anterior,
            preferencia_internacional, fumador, preferencia_viaje_1, preferencia_viaje_2,preferencia_viaje_3, pension_anual, años_tributados,
            maltrato, tipo_discapacidad_id, enfermedad_id, numero_propiedades, nacionalidad_española
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
    """, (
        datos_jubilados['jubilado_id'], datos_jubilados['nombre'],
        datos_jubilados['apellido'], datos_jubilados['genero'],
        datos_jubilados['edad'], datos_jubilados['endeudamiento'],
        datos_jubilados['historial_judicial_id'], datos_jubilados['cantidad_hijos'],
        datos_jubilados['geografico_id'], datos_jubilados['participacion_voluntariado'],
        datos_jubilados['estado_civil_id'], datos_jubilados['participacion_anterior'],
        datos_jubilados['preferencia_internacional'], datos_jubilados['fumador'], datos_jubilados['preferencia_viaje_1'], datos_jubilados['preferencia_viaje_2'],datos_jubilados['preferencia_viaje_3'], datos_jubilados['pension_anual'],
        datos_jubilados['años_tributados'], datos_jubilados['maltrato'],
        datos_jubilados['tipo_discapacidad_id'], datos_jubilados['enfermedad_id'], datos_jubilados['numero_propiedades'], datos_jubilados['nacionalidad_española']
    ))

# VIAJES
for viajes_id in range(1, 151):
    datos = generar_datos_viajes(viajes_id)
    cursor.execute("""
        INSERT INTO public.viajes (
            viajes_id, geografico_id, tipo_turismo_id, numero_dias,
            transporte_pagado, mes_id, tipo_residencia_id,numero_plazas
        ) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)
    """, (
        datos['viajes_id'], datos['geografico_id'], datos['tipo_turismo_id'],
        datos['numero_dias'], datos['transporte_pagado'], datos['mes_id'],
        datos['tipo_residencia_id'],datos['numero_plazas']
    ))

# Commit para aplicar cambios en la base de datos
conn.commit()

#FOREIGN KEYS CONFIGURACIÓN

cursor.execute("""
    ALTER TABLE public.jubilados ADD CONSTRAINT jubilados_geografico 
FOREIGN KEY (geografico_id) REFERENCES public.geografico(geografico_id);

ALTER TABLE public.viajes ADD CONSTRAINT viajes_geografico 
FOREIGN KEY (geografico_id) REFERENCES public.geografico(geografico_id);

ALTER TABLE public.jubilados ADD CONSTRAINT jubilados_discapacidad 
FOREIGN KEY (tipo_discapacidad_id) REFERENCES public.discapacidad(tipo_discapacidad_id);

ALTER TABLE public.jubilados ADD CONSTRAINT jubilados_estadocivil 
FOREIGN KEY (estado_civil_id) REFERENCES public.estado_civil(estado_civil_id);

ALTER TABLE public.jubilados ADD CONSTRAINT jubilados_judicial 
FOREIGN KEY (historial_judicial_id) REFERENCES public.historial_judicial(historial_judicial_id);

ALTER TABLE public.viajes ADD CONSTRAINT viajes_tipoturismo 
FOREIGN KEY (tipo_turismo_id) REFERENCES public.tipo_turismo(tipo_turismo_id);

ALTER TABLE public.viajes ADD CONSTRAINT viajes_tiporesidencia 
FOREIGN KEY (tipo_residencia_id) REFERENCES public.tipo_residencia(tipo_residencia_id);

ALTER TABLE public.viajes ADD CONSTRAINT viajes_mes 
FOREIGN KEY (mes_id) REFERENCES public.mes(mes_id);

ALTER TABLE public.jubilados ADD CONSTRAINT jubilados_enfermedad 
FOREIGN KEY (enfermedad_id) REFERENCES public.enfermedades(enfermedad_id);
""")

conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

print('DONE')