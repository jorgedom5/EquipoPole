--BASE DEL CÓDIGO SQL, TODO ESTÁ SUJETO A CAMBIOS PERO ES UNA BUENA BASE DE POR DONDE CONTINUAR, LAS VARIABLES SON EJEMPLOS

CREATE TABLE IF NOT EXISTS public.jubilados (
    jubilado_id SERIAL PRIMARY KEY,
    nombre varchar(50) NULL,
    apellido varchar(50) NULL,
    edad int NULL,
    nacionalidad_id int null,
    años_tributados int NULL,
    pension_anual int null,
    geografico_id int null,
    genero varchar null,
    vegetariano bool null,
    vegano bool null,
    fumador bool null,
    numero_propiedades int null,
    numero_hijos int null,
    estado_civil varchar null,
    endeudado bool null,
    problemas_justicia bool null,
    religion_id int null,
    nivel_educativo varchar null,
    sector_laboral_id int null   
);

CREATE table if not EXISTS public.geografico (
	geografico_id SERIAL PRIMARY KEY,
	localidad varchar NULL,
	provincia varchar NULL,
	comunidad_autonoma varchar NULL,
	es_capital bool NULL
);

CREATE table if not EXISTS public.viajes (
	viaje_id SERIAL PRIMARY KEY,
	nombre_viaje varchar null,
	geografico_id int NULL, --ESTA VARIABLE REPRESENTA EL LUGAR DE PARTIDA, EN SUBQUERIES SERÍA GUARDAR COMO AS SALIDA O ALGO ASÍ
	tipo_viaje varchar null,
	dias_totales int null,
	capacidad_viaje int null,
	tipo_transporte varchar null,
	tipo_alojamiento varchar null,
	estacion varchar null
);




--PARA CREAR MUCHOS JUBILADOS (NO SE OPTIMIZAR LOS ARRAYS EN SQL)

INSERT INTO public.jubilados (nombre, apellido, edad, años_tributados, pension_anual, geografico_id, numero_propiedades, nacionalidad_id, vegetariano, vegano, fumador, endeudado, problemas_justicia, genero)
SELECT
    nombres.nombre,
    apellidos.apellido,
    CASE
    WHEN RANDOM() < 0.1 THEN FLOOR(RANDOM() * (60 - 58 + 1) + 58) -- 10% de probabilidad para edades de 58 a 60
    WHEN RANDOM() < 0.3 THEN FLOOR(RANDOM() * (65 - 61 + 1) + 61) -- 20% de probabilidad para edades de 61 a 65
    WHEN RANDOM() < 0.6 THEN FLOOR(RANDOM() * (70 - 66 + 1) + 66) -- 30% de probabilidad para edades de 66 a 70
    ELSE FLOOR(RANDOM() * (100 - 71 + 1) + 71) -- 40% de probabilidad para edades de 71 a 100
END AS edad,
    FLOOR(RANDOM() * (42 - 15 + 1) + 15) as años_tributados,
    FLOOR(RANDOM() * (42823 - 10963 + 1) + 10963) as pension_anual,
    FLOOR(RANDOM() * 28) + 1 as geografico_id, --Aquí está del 1 al 28, no se cuantas regiones habrán
    CASE
    WHEN RANDOM() < 0.75 THEN 1 -- 95% españoles
    ELSE FLOOR(RANDOM() * 3) + 2 -- Resto de las nacionalidades
	END AS numero_propiedades,
    CASE
    WHEN RANDOM() < 0.9 THEN 1 -- 95% españoles
    ELSE FLOOR(RANDOM() * 9) + 2 -- Resto de las nacionalidades
	END AS nacionalidad_id,
    CASE WHEN RANDOM() < 0.02 THEN true ELSE false END AS vegetariano,
    CASE WHEN RANDOM() < 0.0008 THEN true ELSE false END AS vegano,
    CASE WHEN RANDOM() < 0.23 THEN true ELSE false END AS fumador,
    CASE WHEN RANDOM() < 0.18 THEN true ELSE false END AS endeudado,
    CASE WHEN RANDOM() < 0.10 THEN true ELSE false END AS problemas_justicia,
    CASE --SI AÑADÍS NOMBRES, PRIMERO EN EL GÉNERO Y LUEGO EN EL TOTAL
        WHEN nombres.nombre IN ('Juan', 'Carlos', 'Luis', 'Miguel', 'Alejandro', 'Javier', 'Francisco', 'José', 'Antonio', 'Daniel', 'David', 'Roberto', 'Pedro', 'Jorge', 'Raúl', 'Fernando', 'Alberto', 'Héctor', 'Sergio', 'Manuel', 'Pablo', 'Eduardo', 'Andrés', 'Mario', 'Diego', 'José Luis', 'Ricardo', 'Felix', 'Hugo', 'Adrian', 'Ángel', 'Ivan', 'Gustavo', 'Emilio', 'Víctor', 'José Antonio') THEN 'Masculino' --Aquí los nombres masculinos
        WHEN nombres.nombre IN ('Ana', 'María', 'Laura', 'Sofía', 'Isabella', 'Valentina', 'Camila', 'Valeria', 'Lucía', 'Mía', 'Emma', 'Martina', 'Julieta', 'Gabriela', 'Renata', 'Elena', 'Diana', 'Adriana', 'Clara', 'Rosa', 'Beatriz', 'Natalia', 'Paola', 'Alejandra', 'Silvia', 'Luisa', 'Carmen', 'Liliana', 'Victoria', 'Patricia', 'Daniela', 'Carolina', 'Mónica', 'Esther', 'Raquel') THEN 'Femenino' --Aquí los nombres femeninos
        ELSE 'Indefinido'
    END as genero --DEBAJO VAN TODOS LOS NOMBRES PRESENTES ARRIBA
FROM unnest(ARRAY['Juan', 'Carlos', 'Luis', 'Miguel', 'Alejandro', 'Javier', 'Francisco', 'José', 'Antonio', 'Daniel', 'David', 'Roberto', 'Pedro', 'Jorge', 'Raúl', 'Fernando', 'Alberto', 'Héctor', 'Sergio', 'Manuel', 'Pablo', 'Eduardo', 'Andrés', 'Mario', 'Diego', 'José Luis', 'Ricardo', 'Felix', 'Hugo', 'Adrian', 'Ángel', 'Ivan', 'Gustavo', 'Emilio', 'Víctor', 'Ana', 'María', 'Laura', 'Sofía', 'Isabella', 'Valentina', 'Camila', 'Valeria', 'Lucía', 'Mía', 'Emma', 'Martina', 'Julieta', 'Gabriela', 'Renata', 'Elena', 'Diana', 'Adriana', 'Clara', 'Rosa', 'Beatriz', 'Natalia', 'Paola', 'Alejandra', 'Silvia', 'Luisa', 'Carmen', 'Liliana', 'Victoria', 'Patricia', 'Daniela', 'Carolina', 'Mónica', 'Esther', 'Raquel', 'José Antonio']) as nombres(nombre),
     unnest(ARRAY['Gómez', 'Fernández', 'López', 'Rodríguez', 'Pérez', 'Martínez', 'González', 'Sánchez', 'Ramírez', 'Díaz', 'Hernández', 'Torres', 'Flores', 'Ortiz', 'Vargas', 'Ruiz', 'Molina', 'Jiménez', 'Moreno', 'Álvarez', 'Romero', 'Herrera', 'García', 'Lara']) as apellidos(apellido)
LIMIT 5000;

--PARA CREAR REGIONES
INSERT INTO public.geografico (localidad,provincia,comunidad_autonoma,es_capital)
	VALUES 
		('Almeria', 'Almeria', 'Andalucia', false),
    ('Cadiz', 'Cadiz', 'Andalucia', false),  --CONTINUAR CON LAS COMUNIDADES
		
	

--PARA CREAR VIAJES, DATOS DE EJEMPLO A CAMBIAR
INSERT INTO public.viajes (nombre_viaje, geografico_id, tipo_viaje, dias_totales, capacidad_viaje, tipo_transporte, tipo_alojamiento, estacion) --VARIABLES EJEMPLO
VALUES
    ('Viaje 1', 1, 'Cultural', 7, 15, 'Autobús', 'Hotel', 'Verano'),
    ('Viaje 2', 2, 'Playa', 10, 20, 'Avión', 'Apartamento', 'Invierno'),
    ('Viaje 3', 3, 'Aventura', 14, 12, 'Tren', 'Casa Rural', 'Primavera'),
    ('Viaje 4', 4, 'Relax', 5, 25, 'Autobús', 'Hotel', 'Otoño'),
    ('Viaje 5', 5, 'Cultural', 8, 18, 'Avión', 'Apartamento', 'Invierno'),
    ('Viaje 6', 6, 'Playa', 12, 30, 'Tren', 'Casa Rural', 'Verano'),
    ('Viaje 7', 1, 'Aventura', 9, 10, 'Autobús', 'Hotel', 'Primavera'),
    ('Viaje 8', 2, 'Relax', 6, 22, 'Avión', 'Apartamento', 'Otoño'),
    ('Viaje 9', 3, 'Cultural', 11, 14, 'Tren', 'Casa Rural', 'Invierno'),
    ('Viaje 10', 4, 'Playa', 7, 28, 'Autobús', 'Hotel', 'Verano');
   


