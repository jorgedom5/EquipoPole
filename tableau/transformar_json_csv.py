import pandas as pd
import json

with open('resultados_viajes.json', encoding='utf-8') as json_file:
    data = json.load(json_file)

viajes_data = []
participantes_data = []

for viaje_key, viaje_value in data.items():
    viaje_info = viaje_value['info_viaje']
    participantes = viaje_value['participantes']

    viaje_data = {'viaje_id': viaje_info['viajes_id'],
                  'geografico_id': viaje_info['geografico_id'],
                  'ciudad': viaje_info['ciudad'],
                  'comunidad_autonoma': viaje_info['comunidad_autonoma'],
                  'es_costa': viaje_info['es_costa'],
                  'numero_plazas': viaje_info['numero_plazas'],
                  'numero_dias': viaje_info['numero_dias'],
                  'mes': viaje_info['mes'],
                  'transporte_pagado': viaje_info['transporte_pagado'],
                  'residencia': viaje_info['residencia'],
                  'tipo_turismo': viaje_info['tipo_turismo']}
    viajes_data.append(viaje_data)

    for participante in participantes:
        participante_data = {'viaje_id': viaje_info['viajes_id'],
                             'jubilado_id': participante['jubilado_id'],
                             'nombre': participante['nombre'],
                             'apellido': participante['apellido'],
                             'edad': participante['edad'],
                             'pension_anual': participante['pension_anual'],
                             'años_tributados': participante['años_tributados'],
                             'numero_propiedades': participante['numero_propiedades'],
                             'nacionalidad_española': participante['nacionalidad_española'],
                             'geografico_id': participante['geografico_id'],
                             'ciudad': participante['ciudad'],
                             'comunidad_autonoma': participante['comunidad_autonoma'],
                             'es_costa': participante['es_costa'],
                             'cantidad_hijos': participante['cantidad_hijos'],
                             'estado_civil': participante['estado_civil'],
                             'participacion_anterior': participante['participacion_anterior'],
                             'maltrato': participante['maltrato'],
                             'tipo_discapacidad': participante['tipo_discapacidad'],
                             'enfermedad_nivel': participante['enfermedad_nivel'],
                             'historial_judicial': participante['historial_judicial'],
                             'endeudamiento': participante['endeudamiento'],
                             'participacion_voluntariado': participante['participacion_voluntariado'],
                             'fumador': participante['fumador'],
                             'preferencia_internacional': participante['preferencia_internacional'],
                             'preferencia_viaje_1': participante['preferencia_viaje_1'],
                             'preferencia_viaje_2': participante['preferencia_viaje_2'],
                             'preferencia_viaje_3': participante['preferencia_viaje_3'],
                             'participacion_activa': participante['participacion_activa'],
                             'mes_ultimo_viaje': participante['mes_ultimo_viaje'],
                             'puntos': participante['puntos']}
        participantes_data.append(participante_data)

viajes_df = pd.DataFrame(viajes_data)
participantes_df = pd.DataFrame(participantes_data)

print("DataFrame de Viajes:")
print(viajes_df)
viajes_df.to_csv('viajes.csv', index=False)

print("\nDataFrame de Participantes:")
print(participantes_df)
participantes_df.to_csv('participantes.csv', index=False)
