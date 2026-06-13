CREATE TABLE usuarios (
    id_usuario serial primary key,
    nombre varchar (100) not null,
    correo varchar (100) not null,
    edad integer
)