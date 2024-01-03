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
#### ÚLTIMO FILTRADO DF
```python
# Iterar a través de filas en el DataFrame de viajes
for viaje, fila_aleatoria in viajes_df.iterrows():
    print(f'analizando viaje {viaje + 1}')

    # Paso 1: Obtener el valor de geografico_id del viaje actual
    geografico_id_aleatorio = fila_aleatoria['geografico_id']
    mes_viaje_aleatorio = fila_aleatoria['mes']

    # Paso 2: Convertir la fila actual a un diccionario (info_viaje) para facilitar el acceso a los valores
    info_viaje = fila_aleatoria.to_dict()

    # Paso 3: Filtrar el DataFrame jubilados_df
    # - Seleccionar jubilados que no viven en el mismo lugar (geografico_id diferente)
    # - Eliminar aquellos que han viajado en el mismo mes
    df_filtrado = jubilados_df[
        (jubilados_df['geografico_id'] != geografico_id_aleatorio) &
        (jubilados_df['mes_ultimo_viaje'] != mes_viaje_aleatorio)
    ]
```
Explicación detallada: 
1. **Iteración sobre Filas:**  El código utiliza un bucle `for` para iterar sobre las filas del DataFrame `viajes_df`. Cada iteración representa un viaje. 
2. **Impresión del Análisis del Viaje:**  Imprime un mensaje indicando que se está analizando un viaje específico, utilizando el índice del viaje más 1 (`viaje + 1`). 
3. **Obtención de Valores del Viaje Actual:**  
- `geografico_id_aleatorio`: Obtiene el valor de la columna `'geografico_id'` de la fila actual del DataFrame `viajes_df`. 
- `mes_viaje_aleatorio`: Obtiene el valor de la columna `'mes'` de la fila actual del DataFrame `viajes_df`. 
4. **Creación de un Diccionario con la Información del Viaje:**  
- `info_viaje`: Convierte la fila actual del DataFrame `viajes_df` en un diccionario. Esto facilita el acceso a los valores de la fila para su posterior uso. 
5. **Filtrado del DataFrame de Jubilados:**  
- `df_filtrado`: Filtra el DataFrame `jubilados_df`:
- Selecciona jubilados que no viven en el mismo lugar (geografico_id diferente).
- Elimina aquellos que han viajado en el mismo mes que el viaje actual.
Se itera a través de los viajes y se aplican una serie de filtros y cálculos de puntos a los jubilados.
#### SUMA DE PUNTOS
1. **Creación de la Columna 'puntos':**  
- `df_filtrado['puntos'] = 0.0`: Se crea una nueva columna llamada 'puntos' en el DataFrame `df_filtrado` y se le asigna el valor inicial de 0.0 para todas las filas. Esto significa que inicialmente, todos los jubilados en el DataFrame tienen 0.0 puntos. 
2. **Cambio del Tipo de Datos a Decimal:**  
- `df_filtrado['puntos'] = df_filtrado['puntos'].astype(float)`: Se realiza una conversión explícita del tipo de datos de la columna 'puntos' a punto flotante (`float`). Aunque inicialmente se asignó un valor decimal (0.0), este paso asegura que la columna esté explícitamente configurada como un tipo de dato decimal, lo cual puede ser útil en operaciones matemáticas y cálculos que involucren esta columna.
3. **Suma y resta de puntos según características**

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





