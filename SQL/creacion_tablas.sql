CREATE TABLE IF NOT EXISTS public.jubilados (
    jubilado_id SERIAL PRIMARY KEY,
    nombre varchar(50) NULL,
    apellido varchar(50) NULL,
    edad int NULL,
    años_tributados int NULL,
    pension_anual int null,
    geografico_id int null
);

CREATE table if not EXISTS public.geografico (
	geografico_id SERIAL PRIMARY KEY,
	localidad varchar NULL,
	provincia varchar NULL,
	comunidad_autonoma varchar NULL,
	es_capital bool NULL
);

--PARA CREAR MUCHOS JUBILADOS (NO SE OPTIMIZAR LOS ARRAYS EN SQL)

INSERT INTO public.jubilados (nombre, apellido, edad, años_tributados, pension_anual, geografico_id)
SELECT
    nombres.nombre,
    apellidos.apellido,
    FLOOR(RANDOM() * (100 - 58 + 1) + 58) as edad, --Entre 58 y 100 años
    FLOOR(RANDOM() * (42 - 15 + 1) + 15) as años_tributados, --Entre 15 y 42 años
    FLOOR(RANDOM() * (42823 - 10963 + 1) + 10963) as pension_anual, --Pension minima anual (10963) y maxima (42823)
    FLOOR(RANDOM() * 20) + 1 as geografico_id --Como aún no hay nada es hasta 20
FROM unnest(ARRAY['Juan', 'María', 'Pedro', 'Ana', 'Carlos', 'Luis', 'Elena', 'Javier', 'Laura', 'Miguel', 'Isabel', 'Rosa', 'David', 'Sandra', 'Alberto', 'Patricia', 'Raúl', 'Carmen', 'Antonio', 'Beatriz', 'Francisco', 'Lorena', 'Diego', 'Monica']) as nombres(nombre),
     unnest(ARRAY['Gómez', 'Fernández', 'López', 'Rodríguez', 'Pérez', 'Martínez', 'González', 'Sánchez', 'Ramírez', 'Díaz', 'Hernández', 'Torres', 'Flores', 'Ortiz', 'Vargas', 'Ruiz', 'Molina', 'Jiménez', 'Moreno', 'Álvarez', 'Romero', 'Herrera', 'García', 'Lara']) as apellidos(apellido)
LIMIT 5000;

