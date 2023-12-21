create table if not exists tipo_turismo(
	tipo_turismo_id serial primary key,
	tipo_turismo varchar(50) not null
)

insert into tipo_turismo (tipo_turismo)
values
('Capital de provincia'), ('Turismo de naturaleza'), ('Turismo cultural'),('Turismo de descanso')
