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
	mes varchar(50) not null,
    cuatrimestre integer
);

insert into public.mes (mes, cuatrimestre)
values
('Enero', 1),
('Febrero', 1),
('Marzo', 1),
('Abril', 1),
('Mayo', 2),
('Junio', 2),
('Julio', 2),
('Agosto', 2),
('Septiembre', 3),
('Octubre', 3),
('Noviembre', 3),
('Diciembre', 3);

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
drop table if exists public.historial_judicial;
create table if not exists public.historial_judicial(
	historial_judicial_id serial primary key,
	historial_judicial varchar(50) not null );
	
insert into public.historial_judicial (historial_judicial)
values
('Sin delitos'),
('Falta'),
('Leve'),
('Grave'),
('Muy grave');

--TABLA DISCAPACIDAD
drop table if exists public.discapacidad;
create table public.discapacidad(
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
create table public.estado_civil(
	estado_civil_id serial primary key,
	estado_civil varchar(50) not null);
	
insert into public.estado_civil (estado_civil)
values
('Soltero'),
('Casado'),
('Viudo');

--TABLA ENFERMEDADES
drop table if exists public.enfermedades;
create table public.enfermedades(
	enfermedad_id serial primary key,
	enfermedad_nivel varchar(50) not null);

insert into public.enfermedades (enfermedad_nivel)
values
('Ninguna'),
('Leve'),
('Media'),
('Grave');