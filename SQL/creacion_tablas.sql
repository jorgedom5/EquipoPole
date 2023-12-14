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