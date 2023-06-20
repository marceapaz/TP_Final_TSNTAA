DROP DATABASE IF EXISTS SistemaDeAlarma;
CREATE DATABASE SistemaDeAlarma CHARACTER SET utf8mb4;
USE SistemaDeAlarma;

CREATE TABLE Lecturas (
    Id INT auto_increment not null,
    IdTipo_sensor int not null,
    fecha_hora datetime not null,
    valor decimal(17, 4) not null,
    PRIMARY KEY(Id)
);

CREATE TABLE Tipos_Evento (
    Id INT auto_increment not null,
	Nombre nvarchar(50) not null,
    PRIMARY KEY(Id)
);

CREATE TABLE Eventos (
    Id INT auto_increment not null,
    IdTipo_evento INT not null,
    fecha_hora   datetime not null,
    PRIMARY KEY(Id)
);

CREATE TABLE Tipos_sensor (
  Id INT PRIMARY KEY AUTO_INCREMENT,
  Nombre VARCHAR(50)
);

CREATE TABLE Umbrales (
  Id INT PRIMARY KEY AUTO_INCREMENT,
  IdTipo_sensor int,
  Umbral DECIMAL(10, 2)
);

CREATE TABLE Umbrales_fluctuacion(
  Id INT PRIMARY KEY AUTO_INCREMENT,
  IdTipo_sensor int,
  Umbral DECIMAL(10, 2)
);

CREATE TABLE Fluctuaciones (
    Id INT auto_increment not null,
    IdTipo_sensor int not null,
    lectura_anterior decimal(17, 4) not null,
    lectura_actual decimal(17, 4) not null,
    magnitud_fluctuacion decimal(17, 4) not null,
    fecha_hora datetime not null,
    PRIMARY KEY(Id)
);

ALTER TABLE Lecturas ADD FOREIGN KEY(IdTipo_sensor) REFERENCES Tipos_sensor(Id);
ALTER TABLE Eventos ADD FOREIGN KEY(IdTipo_evento) REFERENCES Tipos_Evento(Id);
ALTER TABLE Umbrales ADD FOREIGN KEY(IdTipo_sensor) REFERENCES Tipos_sensor(Id);
ALTER TABLE Umbrales_fluctuacion ADD FOREIGN KEY(IdTipo_sensor) REFERENCES Tipos_sensor(Id);
ALTER TABLE Fluctuaciones ADD FOREIGN KEY(IdTipo_sensor) REFERENCES Tipos_sensor(Id);