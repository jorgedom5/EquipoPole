# TUTORIAL CREAR DATAFRAME A PARTIR DE SQL CON PYTHON

## Importación de librerías:

```python
import pandas as pd
import sqlite3
import pyodbc as pdb
import psycopg2 
```
## Definición de variables para acceder a Postgres
```python
host = "localhost"
database = "postgres"
user = "root"
password = "root"
port = "5432"
```

## Conectar con Postgres
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

## A partir de una query, obtener un DataFrame de pandas para poder trabajar con Python
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

A partir de aqui ya se puede trabajar con el dataframe