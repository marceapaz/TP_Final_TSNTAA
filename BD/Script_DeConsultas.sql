/*Lecturas de temperatura registradas en los últimos 24 horas*/
SELECT FORMAT(valor, 2) as Valor, DATE_FORMAT(fecha_hora, '%d/%m/%Y %H:%i') as FechaHora 
FROM lecturas WHERE fecha_hora >= NOW() - INTERVAL 24 HOUR 
and idtipo_sensor = 1
ORDER BY fecha_hora;

/*Lecturas de presión:*/
SELECT count(*) as Cantidad
FROM lecturas 
where idtipo_sensor = 3
and fecha_hora BETWEEN '2023-06-01' AND '2023-06-30' ;

/*Promedio de humedad:*/
SELECT FORMAT(AVG(valor), 2) AS promedio_humedad FROM lecturas where idtipo_sensor = 2;

/* Escribe una consulta en SQL para obtener una lista de fechas en las que la presión registrada estuvo por encima de un umbral definido.*/
SELECT DISTINCT t.nombre as TipoSensor, FORMAT(l.valor, 2) as Valor, DATE_FORMAT(l.fecha_hora, '%d/%m/%Y %H:%i') as FechaHora
FROM lecturas l inner join tipos_sensor t on t.id = l.idtipo_sensor 
WHERE idtipo_sensor = 3 
and valor > 1012;

/*cantidad total de eventos de rotura y fuga registrados en la base de datos en los últimos 7 días.*/
Select t.Nombre as TipoDeEvento, count(*) from eventos e
inner join tipos_evento t on t.Id = e.IdTipo_evento
WHERE e.fecha_hora >= NOW() - INTERVAL 7 day
group by t.Nombre 


