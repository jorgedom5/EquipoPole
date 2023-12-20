--BASE DEL CÓDIGO SQL, TODO ESTÁ SUJETO A CAMBIOS PERO ES UNA BUENA BASE DE POR DONDE CONTINUAR, LAS VARIABLES SON EJEMPLOS

CREATE table if not EXISTS public.geografico (
	geografico_id SERIAL PRIMARY KEY,
	localidad varchar NULL,
	provincia varchar NULL,
	comunidad_autonoma varchar NULL,
	es_capital bool NULL
);


--PARA CREAR REGIONES
INSERT INTO public.geografico (localidad,provincia,comunidad_autonoma,es_capital)
	VALUES 
		('Almeria', 'Almeria', 'Andalucia', false),
    ('Cadiz', 'Cadiz', 'Andalucia', false),  --CONTINUAR CON LAS COMUNIDADES
