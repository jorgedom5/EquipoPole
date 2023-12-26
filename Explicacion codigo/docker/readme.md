# DOCKER-COMPOSE
Este código es un archivo YAML que describe un entorno Docker Compose con dos servicios: uno de PostgreSQL y otro de Python. A continuación, se explica paso a paso:
# Versión de Docker Compose:
```docker
version: "latest"
```
Indica que se está utilizando la versión más reciente de Docker Compose.
### Definición de servicios:
#### Servicio PostgreSQL
```docker
postgres:
  image: postgres
  restart: always
  ports:
    - "5432:5432"
  volumes:
    - ./init.sql:/docker-entrypoint-initdb.d/init.sql 
  environment:
    - POSTGRES_USER=root
    - POSTGRES_PASSWORD=root
    - POSTGRES_DB=root
```
- image: postgres: Utiliza la imagen oficial de PostgreSQL desde Docker Hub.
- restart: always: Indica que el contenedor se reiniciará siempre que se detenga.
- ports: - "5432:5432": Mapea el puerto 5432 del host al puerto 5432 del contenedor (puerto por defecto de PostgreSQL).
- volumes: - ./init.sql:/docker-entrypoint-initdb.d/init.sql: Monta el archivo init.sql en el directorio docker-entrypoint-initdb.d del contenedor, lo que permite ejecutar scripts de inicialización en la base de datos.
- environment: - POSTGRES_USER=root - POSTGRES_PASSWORD=root - POSTGRES_DB=root: Configura variables de entorno para el contenedor de PostgreSQL, estableciendo el usuario, la contraseña y la base de datos.
#### Servicio Python
```docker
python:
image: python:3.11.7
  restart: no
  volumes:
    - .:/app  # Monta el directorio actual completo en /app dentro del contenedor
  command: bash -c "pip install -r /app/requirements.txt && python /app/main.py && python /app/filtros.py"
```
- image: python:3.11.7: Utiliza la imagen oficial de Python 3.11.7 desde Docker Hub.
- restart: no: Indica que el contenedor de Python no se reiniciará automáticamente.
- volumes: - .:/app: Monta el directorio actual en el directorio /app dentro del contenedor, permitiendo compartir archivos entre el host y el contenedor.
- command: bash -c "pip install -r /app/requirements.txt && python /app/main.py && python /app/filtros.py": Especifica el comando que se ejecutará al iniciar el contenedor de Python. En este caso, instala las dependencias del archivo requirements.txt y luego ejecuta dos scripts Python (main.py y filtros.py).
### Definición de volúmenes
```docker
volumes:
  postgres:
```
Define un volumen llamado postgres que se utiliza en el servicio de PostgreSQL. Los volúmenes en Docker permiten persistir datos incluso si los contenedores se detienen o se eliminan.