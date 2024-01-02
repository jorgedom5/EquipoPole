# JUSTIFICACIÓN HERRAMIENTAS EMPLEADAS

### GITHUB
Trabajar de manera conjunta en un repositorio compartido, donde se puede realizar cambios de código con su respectivo registro y control. Además, gracias al control de versiones somos capaces de revertir errores en caso de que sucedieran. Por último, mediante el uso de Pull Requests nos aseguramos siempre de que el repositorio funciona de la forma correcta.

## PYTHON
Python es el lenguaje seleccionado para elaborar nuestros scripts al ser todos capaces de trabajar en este lenguaje.
#### JUPYTER NOTEBOOK Y COLAB
Para testear poco a poco las ideas que surgen a la hora de crear las bases de datos y los filtros. Por comidad y facilidad hemos empleado estos Notebooks en lugar de otros.
#### VISUAL STUDIO CODE
Para desarrollar los scripts principales hemos hecho uso de VSC al haber trabajado en clase con este. Los archivos docker, markdown... también han sido desarrollados con Visual Studio Code al haberlo usado en clase.

## POSTGRES SQL
Para desarrollar la base de datos y las tablas secundarias, hemos usado Postgres SQL para aprovechar la velocidad en las queries y la capacidad de almacenamiento de Postgres. También para asociar unas tablas con otras. Hemos usado Postgres ya que es el que hemos usado en clase.
#### DBEAVER
Para acceder a nuestra base de datos y ejecutar las queries de prueba que posteriormente están en los archivos .py y .sql, hemos usado DBeaver al haber tratado con este en clase. No hemos usado PGAdmin porque no lo hemos considerado necesario para el proyecto.

## DOCKER
Hemos usado Docker para insertar en un contenedor todos los scripts python y sql, al igual que la base de datos Postgres. De esta forma, con usar docker-compose somos capaces de instalar la base de datos en local en menos de 10 minutos. No hemos creado ningun dockerfile al no haber sido necesario para este proyecto.