# MAIN.PY

### Importación de bibliotecas:
```python
import random
from faker import Faker
import psycopg2
import pandas as pd
from gender_guesser.detector import Detector
from unidecode import unidecode
import numpy as np
```
- random: Biblioteca para generación de números aleatorios.
- Faker: Biblioteca para generar datos ficticios.
- psycopg2: Conector PostgreSQL para interactuar con la base de datos.
- pandas: Biblioteca para manipulación de datos en formato tabular.
- gender_guesser: Herramienta para adivinar el género basándose en el nombre.
- unidecode: Biblioteca para quitar acentos y diacríticos de los caracteres.
- numpy: Biblioteca para realizar operaciones numéricas.
### Importación de bibliotecas:
```python
random.seed(42)
```
Establece una semilla para los generadores de números aleatorios, asegurando la reproducibilidad de los resultados.
### Importación de bibliotecas:
```python
gender_detector = Detector()
```
Inicializa el detector de género para adivinar el género basándose en el nombre.
### Conexión a la base de datos PostgreSQL:
```python
conn = psycopg2.connect(
    host="postgres",
    database="root",
    user="root",
    password="root",
    port="5432"
)
```
Establece la conexión a la base de datos PostgreSQL.
### Creación de cursor:
```python
cursor = conn.cursor()
```
Crea un cursor para ejecutar comandos SQL.
### Creación de tablas en la base de datos
En esta sección, se ejecutan comandos SQL para crear la tabla jubilados en la base de datos PostgreSQL. Aquí se definen los campos que formarán parte de la tabla (jubilado_id, nombre, apellido, etc.) junto con sus tipos de datos y restricciones. La clave primaria se establece en jubilado_id con la etiqueta SERIAL para que se incremente automáticamente.

La sentencia DROP TABLE IF EXISTS se utiliza para eliminar la tabla si ya existe, lo que facilita la ejecución repetida del script.

El mismo enfoque se utiliza para la creación de la tabla viajes.
### Generación de datos ficticios:
En estas secciones, se utilizan bucles for para iterar sobre una cantidad determinada de veces y se generan datos ficticios utilizando las funciones previamente definidas (generar_datos_jubilados y generar_datos_viajes). Los datos generados se insertan en las tablas jubilados y viajes de la base de datos.
Para hacer la tabla jubilados usamos la siguientes librerías para:
1. **Generación de un Nombre con Acentos:**  
- `nombre_con_acentos = fake.first_name()`: Utiliza la biblioteca `fake` para generar un nombre ficticio con acentos y lo asigna a la variable `nombre_con_acentos`. 
2. **Eliminación de Acentos del Nombre:**  
- `nombre_sin_acentos = unidecode(nombre_con_acentos)`: Utiliza la función `unidecode` para convertir el nombre con acentos en un nombre sin acentos. Esto puede ser útil para normalizar el nombre y eliminar caracteres especiales. 
3. **Determinación del Género:**  
- `genero = gender_detector.get_gender(nombre_sin_acentos)`: Utiliza una función `get_gender` del objeto `gender_detector` para determinar el género del jubilado basándose en el nombre sin acentos, `gender_detector` es una biblioteca que utiliza algoritmos para inferir el género a partir del nombre.
### Configuración de claves foráneas:
En esta sección, se ejecutan comandos SQL para establecer restricciones de clave foránea entre las tablas. Las claves foráneas aseguran la integridad referencial de la base de datos, estableciendo relaciones entre campos de diferentes tablas. Por ejemplo, la tabla jubilados tiene una clave foránea (geografico_id) que referencia la columna geografico_id en la tabla geografico.
### Commit y cierre de la conexión:
```python
conn.commit()
cursor.close()
conn.close()
```
Se realiza el commit para aplicar los cambios en la base de datos y se cierra la conexión.
### Mensaje de finalización:
```python
print('DONE')
```


