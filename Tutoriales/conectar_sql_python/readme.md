# TUTORIAL CREAR DATAFRAME A PARTIR DE SQL CON CÓDIGO PYTHON
El contenedor docker tiene que estar encendido para acceder a la base de datos, mirad ese tutorial primero
## Importación de librerías y conexión SQL:

```python
import pandas as pd
import sqlite3
import pyodbc as pdb
import psycopg2 
```
### Definición de variables para acceder a Postgres
```python
host = "localhost"
database = "postgres"
user = "root"
password = "root"
port = "5432"
```

### Conectar con Postgres
```python
con = sqlite3.connect("postgres-1.db")

connection_target = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port
    )

# Cursor
cur_target = connection_target.cursor()
```

### A partir de una query, obtener un DataFrame de pandas para poder trabajar con Python
Tabla jubilados (df en el codigo)
```python
query = """
SELECT *
FROM jubilados
"""

cur_target.execute(query)
rows = cur_target.fetchall()

list_of_rows = []

# Para guardar todas las filas
for row in rows:
    list_of_rows.append(row)

# Obtener los nombres de las columnas desde la descripción del cursor
column_names = [desc[0] for desc in cur_target.description]

# Crea el DataFrame con los datos y los nombres de las columnas
df = pd.DataFrame(list_of_rows, columns=column_names)
head = df.head()
print(head)
```
Tabla de viajes (df_viajes en el código)
```python
query = """
SELECT *
FROM viajes
"""

cur_target.execute(query)
rows = cur_target.fetchall()

list_of_rows = []

#Para guardar todas las filas
for row in rows:
    list_of_rows.append(row)

# Obtener los nombres de las columnas desde la descripción del cursor
column_names = [desc[0] for desc in cur_target.description]

# Crea el DataFrame con los datos y los nombres de las columnas
df_viajes = pd.DataFrame(list_of_rows, columns=column_names)
display(df_viajes)
```

A partir de aqui ya se puede trabajar con el dataframe

## FILTROS

### Elegimos un viaje al azar y filtramos por lugar de salida de viaje, de forma que obtengamos los que viven ahí
```python
fila_aleatoria = df_viajes.sample(n=1, random_state=42)

# Obtiene el valor de geografico_id del viaje elegido al azar
geografico_id_aleatorio = fila_aleatoria['geografico_id'].values[0]
info_viaje = fila_aleatoria.to_dict(orient='records')[0] #guarda la info del viaje en un diccionario

# Filtra df basándose en geografico_id, de forma que puedan acceder los que viven ahí
df_filtrado = df[df['geografico_id'] == geografico_id_aleatorio]
```
### Se crean los filtros (los que hay aquí son ejemplos)
```python
# PUNTOS INICIALES
df_filtrado['puntos'] = 0
df_filtrado['puntos'] = df_filtrado['puntos'].astype(float)  # Para insertar decimales

# EDAD
df_filtrado.loc[df_filtrado['edad'] > 70, 'puntos'] += 2

# AÑOS TRIBUTADOS
df_filtrado.loc[df_filtrado['años_tributados'] > 40, 'puntos'] += 5
df_filtrado.loc[(df_filtrado['años_tributados'] > 20) & (df_filtrado['años_tributados'] < 40), 'puntos'] += 3

# PENSIÓN ANUAL
df_filtrado.loc[df_filtrado['pension_anual'] < 12000, 'puntos'] += 7
df_filtrado.loc[(df_filtrado['pension_anual'] > 12000) & (df_filtrado['pension_anual'] < 18000), 'puntos'] += 5

# GÉNERO
df_filtrado.loc[df_filtrado['genero'] == "Femenino", 'puntos'] += 0.1
```
### Filtramos por la capacidad de viaje gracias al diccionario previamente creado, y seleccionamos los elegidos con mayor puntuación
```python
#CAPACIDAD VIAJE
df_sorted = df_filtrado.sort_values(by='puntos', ascending=False) #para ordenar de más puntos a menos
capacidad_viaje = info_viaje['capacidad_viaje'] #crear una variable con la capacidad del viaje a partir del diccionario anterior

# RESULTADO
abuelos_seleccionados = df_sorted.head(capacidad_viaje) #limitamos por capacidad y mostramos
print(abuelos_seleccionados)
```