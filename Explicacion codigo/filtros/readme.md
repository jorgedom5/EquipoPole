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
# Paso 1: Obtener la capacidad del viaje a partir del diccionario info_viaje
capacidad_viaje = info_viaje['numero_plazas']

# Paso 2: Seleccionar a los abuelos (jubilados) para el viaje basándose en la capacidad
abuelos_seleccionados = df_sorted.head(capacidad_viaje)

# Paso 3: Marcar a los jubilados seleccionados como participantes activos
jubilados_df.loc[jubilados_df['jubilado_id'].isin(abuelos_seleccionados['jubilado_id']), 'participacion_activa'] = True

# Paso 4: Establecer el mes del último viaje para los jubilados seleccionados
jubilados_df.loc[jubilados_df['jubilado_id'].isin(abuelos_seleccionados['jubilado_id']), 'mes_ultimo_viaje'] = mes_viaje_aleatorio

# Paso 5: Imprimir los abuelos seleccionados (posiblemente para revisión o seguimiento)
print(abuelos_seleccionados)

# Paso 6: Crear un diccionario con la información del viaje y los participantes seleccionados
info_viaje_dict = info_viaje.copy()
resultados_viajes[f'viaje_{viaje + 1}'] = {
    "info_viaje": info_viaje_dict,
    "participantes": abuelos_seleccionados.to_dict(orient='records')
}
```



Explicación detallada: 
1. **Capacidad del Viaje:**  Se obtiene la capacidad del viaje desde el diccionario `info_viaje` utilizando la clave `'numero_plazas'`. 
2. **Selección de Abuelos:**  Selecciona a los abuelos (jubilados) para el viaje basándose en la capacidad del viaje. Esto se realiza utilizando el método `head` del DataFrame `df_sorted`, que probablemente contiene información sobre los jubilados ordenados de alguna manera. 
3. **Marca de Participación Activa:**  Marca a los jubilados seleccionados como participantes activos. Esto se logra modificando la columna `'participacion_activa'` en el DataFrame `jubilados_df`. 
4. **Registro del Mes del Último Viaje:**  Registra el mes del último viaje para los jubilados seleccionados. Esto se realiza modificando la columna `'mes_ultimo_viaje'` en el DataFrame `jubilados_df` con el valor de la variable `mes_viaje_aleatorio`. 
5. **Impresión de Abuelos Seleccionados:**  Imprime la información de los abuelos seleccionados, posiblemente para visualizar o verificar. 
6. **Registro de Resultados del Viaje:**  Crea un diccionario llamado `resultados_viajes` que contiene la información del viaje (`info_viaje_dict`) y los participantes seleccionados (`abuelos_seleccionados`) en el formato específico. La clave del diccionario es una cadena que incluye el número del viaje.
Los resultados del análisis se guardan en un archivo JSON.





