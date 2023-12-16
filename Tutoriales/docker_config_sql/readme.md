# CONFIGURACIÓN DOCKER-SQL

<img src="image.png" alt="Alt text" width="20%">



## PASOS A SEGUIR DOCKER
 1. DESCARGA EN LOCAL EL ARCHIVO DOCKER-COMPOSE
 2. EJECUTA `docker-compose up -d` DENTRO DE LA TERMINAL, USANDO LA UBICACIÓN DE LA CARPETA

  UNA VEZ ENCENDIDO EL CONTAINER, PODÉIS USAR O DBEAVER VIENDO EL OTRO TUTORIAL O PGADMIN, LO SIGUIENTE ES TODO PARA PGADMIN.
  
 3. ABRE LA URL `http://localhost:5050`
 4. INGRESA CON LAS CREDENCIALES
    - user: admin@admin.com
    - password: admin

DE MOMENTO NO HAY MÁS

VIDEO TUTORIAL:
URL: https://www.youtube.com/watch?v=uKlRp6CqpDg&t=675s&ab_channel=FaztCode


## UNA VEZ EN PGADMIN U OTRAS

### PARA GUARDAR BASE DE DATOS EN LOCAL
- PASO 1
  
![Alt text](image-1.png)

Lo de Jubilados no saldrá, darle encima de Databases y luego 'Restore'
- PASO 2
  
![Alt text](image-2.png)

Le dais a la carpeta de la derecha de Filename
- PASO 3
  
![Alt text](image-3.png)

Buscáis la ruta donde está el archivo .sql, cambiad el fileformat de bajo a la derecha

- PASO 4

Trabajar, TODO LO QUE SE HAGA TIENE QUE ESTAR DENTRO DEL SCRIPT .sql para pepo

- PARA ABRIR UN SCRIPT
  
  ![Alt text](image-4.png)

Click derecho sobre en panel de la izquierda y escribís código .sql, por ejemplo:
![Alt text](image-5.png)


PARA IMPORTAR DESDE UN CSV MIRAD EL VIDEO: https://www.youtube.com/watch?v=Ikd2xSb00UI&ab_channel=BhaskarReddyPulsani
