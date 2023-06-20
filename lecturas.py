from decimal import Decimal
import MySQLdb
from conexion_bd import establecer_conexion

def obtener_lecturas_temperatura():
    try:
        # Conexión a la base de datos
        conexion = establecer_conexion()
        print("Consultando temperaturas registradas en las últimas 24hs:")
        
        cursor = conexion.cursor()   
        # Consulta SQL
        consulta = "SELECT FORMAT(valor, 2) as Valor, DATE_FORMAT(fecha_hora, '%d/%m/%Y %H:%i') as FechaHora FROM lecturas WHERE fecha_hora >= NOW() - INTERVAL 24 HOUR and idtipo_sensor = 1 ORDER BY fecha_hora"
        cursor.execute(consulta)
        resultados = cursor.fetchall()

        temperaturas = [str(resultado[0]) for resultado in resultados]
        print("Temperaturas registradas: ", temperaturas)

    except MySQLdb.connector.Error as error:
        print(f"Error al ejecutar la consulta: {error}")
    finally:
        cursor.close()
        conexion.close()
