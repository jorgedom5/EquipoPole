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

# FUNCIÓN PARA CREAR SI SON FUMADORES POR PORCENTAJES
def generar_fumador():
  prob = fake.random_int(1, 100)
  if prob <= 8.27: # % de fumadores mayores de 65 años en españa
    return 1 #FUMADOR
  elif prob <= 9.34: # % de fumadores ocasionales de 65 años en españa
    return 2 #FUMADOR OCASIONAL
  else:
    return 0 #NO FUMADOR

# FUNCIÓN PARA CREAR LA PREFERENCIA DEL VIAJE POR PORCENTAJES
def generar_preferencia_viaje():
  prob = fake.random_int(1, 100)
  if prob <= 15: # revisar porcentaje dependiendo del viaje
    return 1 # Capital de provincia
  elif prob <= 35: # revisar porcentaje dependiendo del viaje
    return 2 # Turismo de naturaleza
  elif prob <= 60: # revisar porcentaje dependiendo del viaje
    return 3 # Turismo cultural
  else:
    return 4 # Turismo de descanso

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
  else:  
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
    return 1
  elif prob <= 11:
    return 2
  elif prob <=  29:
    return 3
  else:
    return 0

# FUNCIÓN PARA CREAR EL LUGAR DE RESIDENCIA POR PORCENTAJES
def generar_lugar_residencia():
  prob = fake.random_int(1, 100)
  if prob <= 77.9:
    return 1 #ESPAÑA
  elif prob <= 83.13:
    return 2 #EUROPA
  elif prob <= 83.20:
    return 3 #ÁFRICA
  elif prob <= 99.66:
    return 4 #AMÉRICA
  elif prob <= 99.77:
    return 5 #ASIA
  else:
    return 6 #OCEANÍA


# AQUÍ PARA CREAR COLUMNAS
def generar_datos_jubilados():
    nombre_con_acentos = fake.first_name()
    nombre_sin_acentos = unidecode(nombre_con_acentos)
    genero = gender_detector.get_gender(nombre_sin_acentos)
    edad = generar_edad()
    endeudamiento = fake.random_int(1, 100) <= 18 # Endeudamiento es True el 18% de los casos
    tipo_pensionista = fake.random_int(1, 6)
    historial_judicial = generar_historial_delitos()
    cantidad_hijos = generar_hijos()
    lugar_residencia  = generar_lugar_residencia()
    participacion_voluntariado =  fake.random_int(1, 100) <=30
    estado_civil= generar_estado_civil()
    participacion_anterior=fake.random_int(1,100)<=15
    fumador = generar_fumador()
    preferencia_viaje = generar_preferencia_viaje()
    pension_anual = generar_pension_anual()
    años_tributados = generar_años_tributados()
    maltrato = fake.random_int(1, 100) <= 1
    discapacidad = generar_discapacidad()
    return {
        'Nombre': nombre_sin_acentos,
        'Apellido': fake.last_name(),
        'Género': genero,
        'Edad': edad,
        'Endeudamiento': endeudamiento,
        'Tipo de pensionista': tipo_pensionista,
        'Delito de mayor gravedad ' : historial_judicial,
        'Cantidad de hijos' : cantidad_hijos,
        'Lugar de residencia': lugar_residencia,
        'Participación en un voluntariado' : participacion_voluntariado,
        'Estado civil': estado_civil,
        'Participación anterior': participacion_anterior,
        'Fumador': fumador,
        'Preferencia viaje': preferencia_viaje,
        'Pension anual': pension_anual,
        'Años tributados': años_tributados,
        'Maltrato': maltrato,
        'Discapacidad': discapacidad
    }

# 5000 filas de datos con 'jubilado_id'
datos = [generar_datos_jubilados() for _ in range(5000)]
df = pd.DataFrame(datos)

# Guardar el DataFrame en un archivo CSV
df.to_csv('jubilados_provisional.csv', index=False)
print('DONE')
