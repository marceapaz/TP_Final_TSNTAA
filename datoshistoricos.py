from decimal import Decimal
import mysql.connector
from conexion_bd import establecer_conexion

def obtener_promedio_humedad():
    try:
        print("Consultando promedio de humedad...")
        conexion = establecer_conexion()
        cursor = conexion.cursor()

        # Consulta SQL
        consulta = "SELECT FORMAT(AVG(valor), 2) AS promedio_humedad FROM lecturas WHERE idtipo_sensor = 2"
        cursor.execute(consulta)

        # Resultado de la consulta
        resultado = cursor.fetchone()
        promedio_humedad = resultado[0]

        # Mostrar resultado
        print("Promedio de humedad: ", promedio_humedad)
    except mysql.connector.Error as error:
        print(f"Error al ejecutar la consulta: {error}")
    finally:
        cursor.close()
        conexion.close()





