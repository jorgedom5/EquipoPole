create table if not exists tipo_turismo(
	tipo_turismo_id serial primary key,
	tipo_turismo varchar(50) not null
);

insert into tipo_turismo (tipo_turismo)
values
('Capital de provincia'), ('Turismo de naturaleza'), ('Turismo cultural'),('Turismo de descanso');


create table if not exists mes(
	mes_id serial primary key,
	mes varchar(50) not null
);

insert into mes (mes)
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

create table if not exists tipo_residencia(
	tipo_residencia_id serial primary key,
	residencia varchar(50) not null
);

insert into tipo_residencia (residencia)
values
('Hotel'),
('Hostal'),
('Albergue'),
('Apartamento'),
('Casa rural');
