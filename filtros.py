#archivo para poner los filtros

import pandas as pd
import psycopg2
import numpy as np
import time
import json

pd.set_option('mode.chained_assignment', None)

#CONEXIONES BASE DE DATOS
host = "postgres" #SI ES PARA EL DOCKER-COMPOSE, CAMBIAR POR "postgres"
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
  preferencia_viaje_1,
  preferencia_viaje_2,
  preferencia_viaje_3
from 
  jubilados j 
  left join geografico g on j.geografico_id = g.geografico_id 
  left join estado_civil ec on j.estado_civil_id = ec.estado_civil_id 
  left join discapacidad d on j.tipo_discapacidad_id = d.tipo_discapacidad_id 
  left join enfermedades e on j.enfermedad_id = e.enfermedad_id 
  left join historial_judicial hj on j.historial_judicial_id = hj.historial_judicial_id 
;
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
jubilados_df['participacion_activa'] = False #VARIABLE PARA SABER SI HA PARTICIPADO ESTE AÑO
jubilados_df['mes_ultimo_viaje'] = None 


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
resultados_viajes = {}

# Bucle a través de todos los viajes
for viaje, fila_aleatoria in viajes_df.iterrows():
    print(f'analizando viaje {viaje + 1}')
    # Obtener el valor de geografico_id del viaje actual
    geografico_id_aleatorio = fila_aleatoria['geografico_id']
    mes_viaje_aleatorio = fila_aleatoria['mes']
    info_viaje = fila_aleatoria.to_dict()  # Guarda la info del viaje en un diccionario

    # Filtrar df basándose en geografico_id, de forma que puedan acceder los que no viven ahí, y eliminamos de paso los que han viajado en el mismo mes
    df_filtrado = jubilados_df[(jubilados_df['geografico_id'] != geografico_id_aleatorio) & 
                               (jubilados_df['mes_ultimo_viaje'] != mes_viaje_aleatorio)]


    #FILTROS DE VERDAD (INSERTAR LOS PUNTOS AQUI, USAD EL NOTEBOOK.IPYNB PARA PROBAR)


    # PUNTOS INICIALES
    df_filtrado['puntos'] = 0.0
    df_filtrado['puntos'] = df_filtrado['puntos'].astype(float)  # Para insertar decimales
    
    # PUNTOS POR MISMA COMUNIDAD AUTONOMA
    df_filtrado.loc[df_filtrado['comunidad_autonoma'] == info_viaje['comunidad_autonoma'], 'puntos'] -= 5

    #PUNTOS POR EDAD
    df_filtrado['puntos'] += np.minimum(
        10, 10 * (np.exp(0.01 * (df_filtrado['edad'] - 58)) ** 1.15 - 1) / (np.exp(0.01 * (80 - 58)) ** 1.15 - 1) + 0.6)
    
    #PUNTOS POR PENSION ANUAL
    df_filtrado.loc[(df_filtrado['pension_anual'] > 10963) & (df_filtrado['pension_anual'] < 12000), 'puntos'] += 10
    df_filtrado.loc[(df_filtrado['pension_anual'] > 12000) & (df_filtrado['pension_anual'] < 16000), 'puntos'] += 9
    df_filtrado.loc[(df_filtrado['pension_anual'] > 16000) & (df_filtrado['pension_anual'] < 21500), 'puntos'] += 7
    df_filtrado.loc[(df_filtrado['pension_anual'] > 21500) & (df_filtrado['pension_anual'] < 24000), 'puntos'] += 5
    df_filtrado.loc[(df_filtrado['pension_anual'] > 24000) & (df_filtrado['pension_anual'] < 27000), 'puntos'] += 3.5
    df_filtrado.loc[(df_filtrado['pension_anual'] > 27000) & (df_filtrado['pension_anual'] < 30000), 'puntos'] += 2
    df_filtrado.loc[(df_filtrado['pension_anual'] > 30000) & (df_filtrado['pension_anual'] < 32000), 'puntos'] += 1
    
    #PUNTOS POR HIJOS
    df_filtrado['puntos'] += ((df_filtrado['cantidad_hijos'] - 2) * 0.4)
    
    #PUNTOS POR ESTADO CIVIL
    df_filtrado.loc[df_filtrado['estado_civil'] == 'Viudo', 'puntos'] +=5.5
    df_filtrado.loc[df_filtrado['estado_civil'] == 'Soltero', 'puntos'] +=2.25
    df_filtrado.loc[df_filtrado['estado_civil'] == 'Casado', 'puntos'] +=2
    
    #PUNTOS POR ESTADO DE SALUD
    df_filtrado.loc[df_filtrado['enfermedad_nivel'] == 'Ninguna', 'puntos'] +=1
    df_filtrado.loc[df_filtrado['enfermedad_nivel'] == 'Leve', 'puntos'] +=1.5
    df_filtrado.loc[df_filtrado['enfermedad_nivel'] == 'Media', 'puntos'] +=3.25
    df_filtrado.loc[df_filtrado['enfermedad_nivel'] == 'Grave', 'puntos'] -=10
    
    #PUNTOS POR ENDEUDAMIENTO
    df_filtrado.loc[df_filtrado['endeudamiento'] == True, 'puntos'] -= 7
    
    #PUNTOS POR AÑOS TRIBUTADOS
    df_filtrado['puntos'] += ((df_filtrado['años_tributados'] - 15) * 0.37)
    
    #PUNTOS POR FUMADOR
    df_filtrado.loc[df_filtrado['fumador'] == True, 'puntos'] -=2
    
    #PUNTOS POR NUMERO DE PROPIEDADES
    df_filtrado['puntos'] -= (df_filtrado['numero_propiedades']* 1.25)
    
    #PUNTOS POR PARTICIPACION VOLUNTARIADO
    df_filtrado.loc[df_filtrado['participacion_voluntariado'] == True, 'puntos'] += 2.5
    
    #PUNTOS POR HISTORIAL JUDICIAL
    df_filtrado.loc[df_filtrado['historial_judicial'] == 'Muy Grave', 'puntos'] -= 1000
    df_filtrado.loc[df_filtrado['historial_judicial'] == 'Grave', 'puntos'] -= 10
    df_filtrado.loc[df_filtrado['historial_judicial'] == 'Leve', 'puntos'] -= 2
    df_filtrado.loc[df_filtrado['historial_judicial'] == 'Falta', 'puntos'] -= 0.5
    
    #PUNTOS POR DISCAPACIDAD
    df_filtrado.loc[df_filtrado['tipo_discapacidad'] == 'Grado 1', 'puntos'] += 0.2
    df_filtrado.loc[df_filtrado['tipo_discapacidad'] == 'Grado 2', 'puntos'] += 0.5
    df_filtrado.loc[df_filtrado['tipo_discapacidad'] == 'Grado 3', 'puntos'] += 0.8
    df_filtrado.loc[df_filtrado['tipo_discapacidad'] == 'Grado 4', 'puntos'] -= 1000
    df_filtrado.loc[df_filtrado['tipo_discapacidad'] == 'Grado 5', 'puntos'] -= 1000
    
    #PUNTOS POR PARTICIPACION ANTERIOR
    df_filtrado.loc[df_filtrado['participacion_anterior'] == True, 'puntos'] -= 5
    df_filtrado.loc[df_filtrado['participacion_activa'] == True, 'puntos'] -= 11 #SI YA HA PARTICIPADO EN ESTE AÑO
    
    #PUNTOS POR VICTIMA DE MALTRATO
    df_filtrado.loc[df_filtrado['maltrato'] == True, 'puntos'] += 3
    
    #PUNTOS POR PREFERENCIA DE VIAJE
    df_filtrado.loc[df_filtrado['preferencia_viaje_1'] == info_viaje['viajes_id'], 'puntos'] += 5
    df_filtrado.loc[df_filtrado['preferencia_viaje_2'] == info_viaje['viajes_id'], 'puntos'] += 2.5
    df_filtrado.loc[df_filtrado['preferencia_viaje_3'] == info_viaje['viajes_id'], 'puntos'] += 1.5    
    
    #PUNTOS POR PREFERENCIA DE VIAJE INTERNACIONAL
    df_filtrado.loc[(df_filtrado['preferencia_internacional'] == True) & ((info_viaje['geografico_id'] == 60) | 
                                                                          (info_viaje['geografico_id'] == 61) | 
                                                                          (info_viaje['geografico_id'] == 62) | 
                                                                          (info_viaje['geografico_id'] == 63)), 'puntos'] += 4
    #PUNTOS SI NO VIVEN EN ZONA DE COSTA PARA VIAJES DE COSTA
    df_filtrado.loc[(df_filtrado['es_costa'] == False)&(info_viaje['es_costa']== True),'puntos'] += 5

    # FILTRAR POR  DE CAPACIDAD VIAJE
    df_sorted = df_filtrado.sort_values(by='puntos', ascending=False)  # Para ordenar de más puntos a menos
    capacidad_viaje = info_viaje['numero_plazas']  # Crear una variable con la capacidad del viaje a partir del diccionario anterior

    # RESULTADO
    abuelos_seleccionados = df_sorted.head(capacidad_viaje)  # Limitamos por capacidad y mostramos
    # pd.set_option('display.max_columns', None)
    jubilados_df.loc[jubilados_df['jubilado_id'].isin(abuelos_seleccionados['jubilado_id']), 'participacion_activa'] = True
    jubilados_df.loc[jubilados_df['jubilado_id'].isin(abuelos_seleccionados['jubilado_id']), 'mes_ultimo_viaje'] = mes_viaje_aleatorio #poner el mes en el que han viajado
    print(abuelos_seleccionados)
    
    info_viaje_dict = info_viaje.copy()
    resultados_viajes[f'viaje_{viaje + 1}'] = {
      "info_viaje": info_viaje_dict,
      "participantes": abuelos_seleccionados.to_dict(orient='records')
    }

# GUARDAR EN UN JSON LOS GANADORES, CAMBIO
json_path = '/app/resultados_viajes.json'  # en docker, para guardar el archivo
#json_path = 'resultados_viajes.json'  # en local, para guardar el archivo
with open(json_path, 'w') as json_file:
    json.dump(resultados_viajes, json_file)
