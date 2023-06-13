DROP DATABASE padel;
CREATE DATABASE padel;
\c padel

CREATE TABLE horario (
    id serial,
    horaInicio time,
    horaFin time,
    CONSTRAINT pk_horario PRIMARY KEY (id),
    CONSTRAINT check_horario_horas CHECK (horaFin > horaInicio)
);

CREATE TABLE estadoCancha (
    id serial,
    nombre varchar(50),
    descripcion varchar(200),
    CONSTRAINT pk_estadoCancha PRIMARY KEY (id)
);

CREATE TABLE estadoCliente (
    id serial,
    nombre varchar(50),
    descripcion varchar(200),
    CONSTRAINT pk_estadoCliente PRIMARY KEY (id)
);

CREATE TABLE cancha (
    id serial,
    nombre varchar(50),
    estadoCancha int,
    CONSTRAINT pk_cancha PRIMARY KEY (id),
    CONSTRAINT fk_cancha_estado FOREIGN KEY (estadoCancha) REFERENCES estadoCancha(id)
);

CREATE TABLE cliente (
    id serial,
    nombre varchar(50),
    apellido varchar(50), 
    email varchar(50),
    numeroTelefono bigint CHECK (numeroTelefono > 0 AND numeroTelefono < 99999999999),
    estadoCliente int,
    CONSTRAINT pk_cliente PRIMARY KEY (id),
    CONSTRAINT fk_cliente_estado FOREIGN KEY (estadoCliente) REFERENCES estadoCliente(id)
);

CREATE TABLE turno (
    id serial,
    fecha date,
    cancha int,
    cliente int,
    horario int,
    CONSTRAINT pk_turno PRIMARY KEY (id),
    CONSTRAINT fk_turno_cancha FOREIGN KEY (cancha) REFERENCES cancha(id),
    CONSTRAINT fk_turno_cliente FOREIGN KEY (cliente) REFERENCES cliente(id),
    CONSTRAINT fk_turno_horario FOREIGN KEY (horario) REFERENCES horario(id)
);

