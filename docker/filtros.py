#archivo para poner los filtros

import pandas as pd
import pyodbc as pdb
import psycopg2
import numpy as np
import time

pd.set_option('mode.chained_assignment', None)

#CONEXIONES BASE DE DATOS
host = "localhost" #SI ES PARA EL DOCKER-COMPOSE, CAMBIAR POR "postgres"
database = "root"
user = "root"
password = "root"
port = "5432"

connection_target = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port
    )
cur_target = connection_target.cursor()


#PASAR DE LA TABLA DE JUBILADOS A DATAFRAME

query_jubilados = """
select 
  jubilado_id, 
  nombre, 
  apellido, 
  edad, 
  pension_anual, 
  años_tributados, 
  numero_propiedades, 
  nacionalidad_española, 
  g.geografico_id, 
  g.ciudad, 
  g.comunidad_autonoma, 
  g.es_costa, 
  cantidad_hijos, 
  ec.estado_civil, 
  participacion_anterior, 
  maltrato, 
  d.tipo_discapacidad, 
  e.enfermedad_nivel, 
  hj.historial_judicial, 
  endeudamiento, 
  participacion_voluntariado, 
  fumador, 
  preferencia_internacional, 
  tt.tipo_turismo 
from 
  jubilados j 
  left join geografico g on j.geografico_id = g.geografico_id 
  left join estado_civil ec on j.estado_civil_id = ec.estado_civil_id 
  left join discapacidad d on j.tipo_discapacidad_id = d.tipo_discapacidad_id 
  left join enfermedades e on j.enfermedad_id = e.enfermedad_id 
  left join historial_judicial hj on j.historial_judicial_id = hj.historial_judicial_id 
  left join tipo_turismo tt on j.tipo_turismo_id = tt.tipo_turismo_id;
"""

cur_target.execute(query_jubilados)
rows = cur_target.fetchall()
list_of_rows = []
# Para guardar todas las filas
for row in rows:
    list_of_rows.append(row)
# Obtener los nombres de las columnas desde la descripción del cursor
column_names = [desc[0] for desc in cur_target.description]
# Crea el DataFrame con los datos y los nombres de las columnas
jubilados_df = pd.DataFrame(list_of_rows, columns=column_names)
print(jubilados_df)


#PASAR DE LA TABLA DE VIAJES A DATAFRAME

query_viajes = """
select 
  viajes_id, 
  g.geografico_id, 
  g.ciudad, 
  g.comunidad_autonoma, 
  g.es_costa, 
  v.numero_plazas, 
  v.numero_dias, 
  m.mes, 
  v.transporte_pagado, 
  tr.residencia, 
  tt.tipo_turismo 
from 
  viajes v 
  left join geografico g on v.geografico_id = g.geografico_id 
  left join mes m on v.mes_id = m.mes_id 
  left join tipo_residencia tr on v.tipo_residencia_id = tr.tipo_residencia_id 
  left join tipo_turismo tt on v.tipo_turismo_id = tt.tipo_turismo_id;
"""

cur_target.execute(query_viajes)
rows = cur_target.fetchall()
list_of_rows = []
# Para guardar todas las filas
for row in rows:
    list_of_rows.append(row)
# Obtener los nombres de las columnas desde la descripción del cursor
column_names = [desc[0] for desc in cur_target.description]
# Crea el DataFrame con los datos y los nombres de las columnas
viajes_df = pd.DataFrame(list_of_rows, columns=column_names)
print(viajes_df)



#FILTROS

# Bucle a través de todos los viajes
for viaje, fila_aleatoria in viajes_df.iterrows():
    print(f'analizando viaje {viaje + 1}')
    # Obtener el valor de geografico_id del viaje actual
    geografico_id_aleatorio = fila_aleatoria['geografico_id']
    info_viaje = fila_aleatoria.to_dict()  # Guarda la info del viaje en un diccionario

    # Filtrar df basándose en geografico_id, de forma que puedan acceder los que no viven ahí
    df_filtrado = jubilados_df[jubilados_df['geografico_id'] != geografico_id_aleatorio]

    #FILTROS DE VERDAD (INSERTAR LOS PUNTOS AQUI, USAD EL NOTEBOOK.IPYNB PARA PROBAR)

    # PUNTOS INICIALES
    df_filtrado['puntos'] = 0.0
    df_filtrado['puntos'] = df_filtrado['puntos'].astype(float)  # Para insertar decimales

    #PUNTOS POR EDAD
    df_filtrado['puntos'] += np.minimum(
        10, 10 * (np.exp(0.01 * (df_filtrado['edad'] - 58)) ** 1.15 - 1) / (np.exp(0.01 * (90 - 58)) ** 1.15 - 1) + 0.6)
    
    #PUNTOS POR ENDEUDAMIENTO
    df_filtrado.loc[df_filtrado['endeudamiento'] == True, 'puntos'] -= 7
    
    #PUNTOS POR AÑOS TRIBUTADOS
    df_filtrado['puntos'] += ((df_filtrado['años_tributados'] - 15) * 0.37)
    
    #PUNTOS POR FUMADOR
    df_filtrado.loc[df_filtrado['fumador'] == True, 'puntos'] -=0.5
    
    #PUNTOS POR NUMERO DE PROPIEDADES
    df_filtrado['puntos'] -= (df_filtrado['numero_propiedades']* 1.5)
    
    #PUNTOS POR PARTICIPACION VOLUNTARIADO
    df_filtrado.loc[df_filtrado['participacion_voluntariado'] == True, 'puntos'] += 2

    # CAPACIDAD VIAJE
    df_sorted = df_filtrado.sort_values(by='puntos', ascending=False)  # Para ordenar de más puntos a menos
    capacidad_viaje = info_viaje['numero_plazas']  # Crear una variable con la capacidad del viaje a partir del diccionario anterior

    # RESULTADO
    abuelos_seleccionados = df_sorted.head(capacidad_viaje)  # Limitamos por capacidad y mostramos
    #pd.set_option('display.max_columns', None)
    print(abuelos_seleccionados)