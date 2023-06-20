from conexion_bd import establecer_conexion

import mysql.connector

def contar_eventos_rotura_fuga():
    conexion = establecer_conexion()
    print("Consultando cantidad de eventos registrados...")
    cursor = conexion.cursor()

    # Consulta SQL
    consulta = """
        Select count(*) as cantidad from eventos e
        inner join tipos_evento t on t.Id = e.IdTipo_evento
        WHERE fecha_hora >= NOW() - INTERVAL 7 day"""

    try:
        cursor.execute(consulta)
        # Resultado
        resultado = cursor.fetchone()
        # Mostrar resultado
        print("Cantidad de eventos de rotura y fuga en los últimos 7 días:", resultado[0])
    except mysql.connector.Error as error:
        print("Error al ejecutar la consulta:", error)
        
    # Cerrar conexión BD
    cursor.close()
    conexion.close()

