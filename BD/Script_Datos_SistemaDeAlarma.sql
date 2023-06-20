USE SistemaDeAlarma;
INSERT INTO tipos_evento (Nombre) values ('Rotura');
INSERT INTO tipos_evento (Nombre) values ('Fuga');

INSERT INTO Tipos_sensor (Nombre) values ('Temperatura');
INSERT INTO Tipos_sensor (Nombre) values ('Humedad');
INSERT INTO Tipos_sensor (Nombre) values ('Presión');

INSERT INTO lecturas (IdTipo_sensor, fecha_hora, valor)
VALUES (1, '2023-06-01 10:00:00', 25.5),
(2, '2023-06-01 10:00:00', 70),
(3, '2023-06-01 10:00:00', 1013.2),
(1, '2023-06-01 11:00:00', 26.1),
(2, '2023-06-01 11:00:00', 68),
(3, '2023-06-01 11:00:00', 1012.8),
(1, '2023-06-01 12:00:00', 24.8),
(2, '2023-06-01 12:00:00', 72),
(3, '2023-06-01 12:00:00', 1014.5),
(1, '2023-06-17 13:00:00', 23.9),
(2, '2023-06-17 13:00:00', 75),
(3, '2023-06-17 13:00:00', 1015.1),
(1, '2023-06-17 14:00:00', 27.3),
(2, '2023-06-17 14:00:00', 65),
(3, '2023-06-17 14:00:00', 1015.1),
(1, '2023-06-20 19:00:00', 32.3),
(2, '2023-06-20 19:00:00', 65),
(3, '2023-06-20 19:00:00', 1011.9),
(1, '2023-06-20 19:00:00', 38);
    
INSERT INTO eventos (idtipo_evento, fecha_hora)
VALUES
    ('1', '2023-06-01 11:30:00'),
    ('2', '2023-06-01 13:45:00');
    
INSERT INTO eventos (idtipo_evento, fecha_hora)
VALUES
    ('1', '2023-06-15 12:30:00'),
    ('2', '2023-06-14 10:45:00');
 
INSERT INTO Umbrales (idtipo_sensor, umbral)
VALUES (1, 35),
       (2, 30),
       (3, 1012);
       
INSERT INTO Umbrales_fluctuacion (idtipo_sensor, umbral)
VALUES (1, 2.0),
       (2, 5.0),
       (3, 10.0);
       
Select * from tipos_evento;
Select * from lecturas where idtipo_sensor = 1;
SELECT * FROM eventos;
SELECT * FROM umbrales;
