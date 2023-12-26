# Explicación del Código Python

## Importación de bibliotecas:
```python
import pandas as pd
import json
```
Abre el archivo 'resultados_viajes.json' en modo lectura y carga su contenido en la variable data utilizando la función json.load().
## Lectura del archivo JSON:
```python
with open('resultados_viajes.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
```
## Procesamiento de datos y construcción de DataFrames:
```python
viajes_data = []
participantes_data = []

for viaje_key, viaje_value in data.items():
    # Información del viaje
    viaje_info = viaje_value['info_viaje']
    participantes = viaje_value['participantes']

    # Construcción de DataFrame para viajes
    viaje_data = {'viaje_id': viaje_info['viajes_id'],
                  'geografico_id': viaje_info['geografico_id'],
                  # ... (otros campos de información)
                  'puntos': participante['puntos']}
    viajes_data.append(viaje_data)

    # Construcción de DataFrame para participantes
    for participante in participantes:
        participante_data = {'viaje_id': viaje_info['viajes_id'],
                             'jubilado_id': participante['jubilado_id'],
                             # ... (otros campos de información)
                             'puntos': participante['puntos']}
        participantes_data.append(participante_data)
```
- Bucles de Iteración:
- 
El código utiliza un bucle for para iterar a través de los elementos del diccionario data. Cada elemento del diccionario representa un viaje, y viaje_key es la clave (ID del viaje) y viaje_value es el valor asociado a esa clave (información del viaje y participantes).

- Información del Viaje:

Se extrae la información del viaje de viaje_value['info_viaje'] y se almacena en la variable viaje_info.

- Construcción de DataFrame para Viajes:

Se crea un diccionario viaje_data que contiene los detalles específicos de cada viaje, utilizando la información extraída de viaje_info.
Este diccionario se agrega a la lista viajes_data, que se utilizará posteriormente para construir el DataFrame de viajes.

- Construcción de DataFrame para Participantes:

Se utiliza otro bucle for para iterar a través de la lista de participantes (viaje_value['participantes']).
Para cada participante, se crea un diccionario participante_data que contiene detalles específicos del participante, combinando información del viaje (viaje_info) y del participante.
## Creación de DataFrames de pandas:
```python
viajes_df = pd.DataFrame(viajes_data)
participantes_df = pd.DataFrame(participantes_data)
```
Se construyen dos DataFrames utilizando los datos recopilados: viajes_df para la información de los viajes y participantes_df para la información de los participantes.
## Impresión de DataFrames y Exportación a archivos CSV:
```python
print("DataFrame de Viajes:")
print(viajes_df)
viajes_df.to_csv('viajes.csv', index=False)

print("\nDataFrame de Participantes:")
print(participantes_df)
participantes_df.to_csv('participantes.csv', index=False)
```
Imprime en la consola los DataFrames de viajes y participantes.
Exporta los DataFrames a archivos CSV ('viajes.csv' y 'participantes.csv') sin incluir el índice.