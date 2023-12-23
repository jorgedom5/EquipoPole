--TABLA GEOGRAFICO
DROP TABLE IF EXISTS public.geografico;
CREATE TABLE IF NOT EXISTS public.geografico (
    geografico_id SERIAL PRIMARY KEY,
    ciudad varchar(50),
    comunidad_autonoma varchar(50),
    es_costa BOOLEAN
);

INSERT INTO public.geografico (ciudad, comunidad_autonoma, es_costa)
    VALUES
    ('Almeria', 'Andalucia', true),
    ('Cadiz', 'Andalucia', true),
    ('Cordoba', 'Andalucia', false),
    ('Granada', 'Andalucia', false),
    ('Huelva', 'Andalucia', true),
    ('Jaen', 'Andalucia', false),
    ('Malaga', 'Andalucia', true),
    ('Sevilla', 'Andalucia', false),
    ('Huesca', 'Aragon', false),
    ('Teruel', 'Aragon', false),
    ('Zaragoza', 'Aragon', false),
    ('Oviedo', 'Principado de Asturias', false),
    ('Gijon', 'Principado de Asturias', true),
    ('Mallorca', 'Islas Baleares', true),
    ('Menorca', 'Islas Baleares', true),
    ('Ibiza', 'Islas Baleares', true),
    ('Formentera', 'Islas Baleares', true),
    ('Las Palmas', 'Canarias', true),
    ('Santa Cruz de Tenerife', 'Canarias', true),
    ('El Hierro', 'Canarias', true),
    ('La Gomera', 'Canarias', true),
    ('Santander', 'Cantabria', true),
    ('Albacete', 'Castilla-La Mancha', false),
    ('Ciudad Real', 'Castilla-La Mancha', false),
    ('Cuenca', 'Castilla-La Mancha', false),
    ('Guadalajara', 'Castilla-La Mancha', false),
    ('Toledo', 'Castilla-La Mancha', false),
    ('Avila', 'Castilla y Leon', false),
    ('Burgos', 'Castilla y Leon', false),
    ('Leon', 'Castilla y Leon', false),
    ('Palencia', 'Castilla y Leon', false),
    ('Salamanca', 'Castilla y Leon', false),
    ('Segovia', 'Castilla y Leon', false),
    ('Soria', 'Castilla y Leon', false),
    ('Valladolid', 'Castilla y Leon', false),
    ('Zamora', 'Castilla y Leon', false),
    ('Barcelona', 'Cataluna', true),
    ('Gerona', 'Cataluna', false),
    ('Lerida', 'Cataluna', false),
    ('Tarragona', 'Cataluna', true),
    ('Alicante', 'Comunidad Valenciana', true),
    ('Castellon', 'Comunidad Valenciana', true),
    ('Valencia', 'Comunidad Valenciana', true),
    ('Badajoz', 'Extremadura', false),
    ('Caceres', 'Extremadura', false),
    ('La Coruna', 'Galicia', true),
    ('Lugo', 'Galicia', true),
    ('Orense', 'Galicia', true),
    ('Pontevedra', 'Galicia', true),
    ('Logrono', 'La Rioja', false),
    ('Madrid', 'Comunidad de Madrid', false),
    ('Murcia', 'Region de Murcia', true),
    ('Cartagena', 'Region de Murcia', true),
    ('Pamplona', 'Comunidad Foral de Navarra', true),
    ('Alava', 'Pais Vasco', false),
    ('Guipuzcoa', 'Pais Vasco', true),
    ('Vizcaya', 'Pais Vasco', true),
    ('Ceuta', 'Ceuta', true),
    ('Melilla', 'Melilla', true),
    ('Europa', 'Europa', true),
    ('America', 'America', true),
    ('Africa', 'Africa', true),
    ('Oceania', 'Oceania', true);


--TABLA TURISMO
drop table if exists public.tipo_turismo;
create table if not exists public.tipo_turismo(
	tipo_turismo_id serial primary key,
	tipo_turismo varchar(50) not null
);

insert into public.tipo_turismo (tipo_turismo)
values
('Capital de provincia'), 
('Turismo de naturaleza'), 
('Turismo cultural'),
('Turismo de descanso');

--TABLA MES
drop table if exists public.mes;
create table if not exists public.mes(
	mes_id serial primary key,
	mes varchar(50) not null
);

insert into public.mes (mes)
values
('Enero'),
('Febrero'),
('Marzo'),
('Abril'),
('Mayo'),
('Junio'),
('Julio'),
('Agosto'),
('Septiembre'),
('Octubre'),
('Noviembre'),
('Diciembre');

--TABLA RESIDENCIA
drop table if exists public.tipo_residencia;
create table if not exists public.tipo_residencia(
	tipo_residencia_id serial primary key,
	residencia varchar(50) not null
);

insert into public.tipo_residencia (residencia)
values
('Hotel'),
('Hostal'),
('Albergue'),
('Apartamento'),
('Casa rural');

--TABLA HISTORIAL JUDICIAL
drop table if exists public.historial;
create table if not exists public.historial(
	tipo_historial_id serial primary key,
	historial varchar(50) not null );
	
insert into public.historial (historial)
values
('Sin delitos'),
('Falta'),
('Leve'),
('Grave'),
('Muy grave');

--TABLA DISCAPACIDAD
drop table if exists public.discapacidad;
create table if not exists public.discapacidad(
	tipo_discapacidad_id serial primary key,
	tipo_discapacidad varchar(50) not null);

insert into public.discapacidad (tipo_discapacidad)
values
('Grado 0'),
('Grado 1'),
('Grado 2'),
('Grado 3'),
('Grado 4');


--TABLA ESTADO CIVIL
drop table if exists public.estado_civil;
create table if not exists estado_civil(
	estado_civil_id serial primary key,
	estado_civil varchar(50) not null);
	
insert into estado_civil (estado_civil)
values
('Soltero'),
('Casado'),
('Viudo');

--TABLA TIPO PENSIONISTA
drop table if exists public.tipo_pensionista;
create table if not exists tipo_pensionista(
	tipo_pensionista_id serial primary key,
	tipo_pensionista varchar(500) not null);
	
insert into tipo_pensionista (tipo_pensionista)
values
('Ser pensionista de jubilación del sistema de Seguridad Social español'),
('Ser pensionista de viudedad del sistema de Seguridad Social español'),
('Ser pensionista por otros conceptos del sistema de Seguridad Social español o perceptor de prestaciones o subsidios de desempleo'),
('Ser asegurado o beneficiario del Sistema de la Seguridad Social español'),
('Españoles residentes en el extranjero siempre que reúnan alguno de los requisitos incluidos en el apartado 1.a). Así, los españoles residentes en Alemania, Andorra, Austria, Bélgica, Dinamarca, Finlandia, Francia, Holanda, Italia, Luxemburgo, Noruega, Portugal, Reino Unido, Suecia y Suiza, podrán tramitarlo en las correspondientes Consejerías de Trabajo, Migraciones y Seguridad Social. '),
('Españoles de origen emigrantes que hayan retornado a España, siempre que sean pensionistas de los sistemas públicos de Seguridad Social del país o países a los que hubieran emigrado.');
