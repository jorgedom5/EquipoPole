CREATE TABLE IF NOT EXISTS public.jubilados (
    jubilado_id int NULL,
    nombre varchar(50) NULL,
    apellido varchar(50) NULL,
    edad int NULL,
    años_tributados int NULL,
    pension_anual int null,
    geografico_id int null
);

CREATE table if not EXISTS public.geografico (
	geografico_id int NULL,
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
    FLOOR(RANDOM() * (80 - 60 + 1) + 60) as edad,
    FLOOR(RANDOM() * (40 - 20 + 1) + 20) as años_tributados,
    FLOOR(RANDOM() * (50000 - 30000 + 1) + 30000) as pension_anual,
    FLOOR(RANDOM() * 1000) as geografico_id
FROM unnest(ARRAY['Juan', 'María', 'Pedro', 'Ana', 'Carlos', 'Luis', 'Elena', 'Javier', 'Laura', 'Miguel', 'Isabel', 'Rosa', 'David', 'Sandra', 'Alberto', 'Patricia', 'Raúl', 'Carmen', 'Antonio', 'Beatriz', 'Francisco', 'Lorena', 'Diego', 'Monica']) as nombres(nombre),
     unnest(ARRAY['Gómez', 'Fernández', 'López', 'Rodríguez', 'Pérez', 'Martínez', 'González', 'Sánchez', 'Ramírez', 'Díaz', 'Hernández', 'Torres', 'Flores', 'Ortiz', 'Vargas', 'Ruiz', 'Molina', 'Jiménez', 'Moreno', 'Álvarez', 'Romero', 'Herrera', 'García', 'Lara']) as apellidos(apellido)
LIMIT 5000;
