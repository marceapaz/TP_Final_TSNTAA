import mysql.connector

def establecer_conexion():
    # Establecer conexión con la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sistemadealarma"
    )
    
    return conexion
