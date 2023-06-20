import datetime
import mysql.connector
from conexion_bd import establecer_conexion

from datetime import datetime

def contar_lecturas_presion():
    # Conexión a la base de datos
    conexion = establecer_conexion()
    print("Lecturas de presión por rango de fecha:")
    fechadesde = input("Ingrese fecha desde (DD/MM/YYYY):")
    fechahasta = input("Ingrese fecha hasta (DD/MM/YYYY):")

    try:
        fecha_desde = datetime.strptime(fechadesde, "%d/%m/%Y").strftime("%Y-%m-%d")
        fecha_hasta = datetime.strptime(fechahasta, "%d/%m/%Y").strftime("%Y-%m-%d")

        cursor = conexion.cursor()
        consulta = """SELECT COUNT(*) AS cantidad_lecturas 
                      FROM lecturas 
                      WHERE fecha_hora BETWEEN %s AND %s 
                      AND idtipo_sensor = 3"""
        parametros = (fecha_desde, fecha_hasta)

        cursor.execute(consulta, parametros)
        resultado = cursor.fetchone()
        cantidad_lecturas = resultado[0]
        print(f"La cantidad de lecturas de presión en el rango {fechadesde} - {fechahasta} es: {cantidad_lecturas}")

    except mysql.connector.Error as error:
        print(f"Error al ejecutar la consulta: {error}")
    finally:
        cursor.close()
        conexion.close()

            
