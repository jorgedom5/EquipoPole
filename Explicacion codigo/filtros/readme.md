# FILTROS.PY
Este código realiza una serie de operaciones en Python utilizando pandas, numpy y psycopg2 para manipular y analizar datos almacenados en una base de datos PostgreSQL. Aquí está el desglose paso a paso:
### Importación de Bibliotecas:
```python
import pandas as pd
import psycopg2
import numpy as np
import time
import json
```
- pandas: Biblioteca para manipulación y análisis de datos.
- psycopg2: Conector PostgreSQL para Python.
- numpy: Biblioteca para operaciones matemáticas.
- time: Módulo para trabajar con funciones relacionadas con el tiempo.
- json: Módulo para trabajar con datos JSON.
### Configuración de Opciones de Pandas:
```python
pd.set_option('mode.chained_assignment', None)
```
Desactiva las advertencias de "chained assignment" en pandas.
### Conexión a la Base de Datos:
```python
host = "postgres"
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
```
Se establece una conexión a una base de datos PostgreSQL utilizando los parámetros de conexión especificados.
### Consulta y Conversión a DataFrame (jubilados):
```python
query_jubilados = "..."  # Consulta SQL para obtener datos de jubilados
cur_target.execute(query_jubilados)
rows = cur_target.fetchall()
# Se crea un DataFrame utilizando los datos obtenidos de la consulta
jubilados_df = pd.DataFrame(rows, columns=[desc[0] for desc in cur_target.description])
```
### Consulta y Conversión a DataFrame (viajes):
```python
query_viajes = "..."  # Consulta SQL para obtener datos de viajes
cur_target.execute(query_viajes)
rows = cur_target.fetchall()
# Se crea un DataFrame utilizando los datos obtenidos de la consulta
viajes_df = pd.DataFrame(rows, columns=[desc[0] for desc in cur_target.description])
```
### Inicialización de Variables y Filtros:
```python
resultados_viajes = {}  # Diccionario para almacenar resultados de los viajes
```
### Bucle para Filtrar y Calcular Puntos:
```python
for viaje, fila_aleatoria in viajes_df.iterrows():
    # ... (filtrado y cálculo de puntos)
```
Se itera a través de los viajes y se aplican una serie de filtros y cálculos de puntos a los jubilados.
### Guardado de Resultados en JSON:
```python
json_path = '/app/resultados_viajes.json'
with open(json_path, 'w') as json_file:
    json.dump(resultados_viajes, json_file)
```
Los resultados del análisis se guardan en un archivo JSON.





