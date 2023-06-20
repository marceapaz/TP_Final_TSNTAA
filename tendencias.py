import mysql.connector
from conexion_bd import establecer_conexion

def obtener_umbral_tiposensor(idtipo_sensor):
    conexion = establecer_conexion()
    print("Presiones con umbral superior al definido")
    cursor = conexion.cursor()
    consulta = "SELECT umbral FROM umbrales WHERE idtipo_sensor = %s LIMIT 1"
    parametros = (idtipo_sensor,)
    cursor.execute(consulta, parametros)
    resultado = cursor.fetchone()
    if resultado:
        umbral = resultado[0]
        return umbral
    else:
        return None
    
def obtener_fechas_presion_elevada(umbral):
    try:
        # Conexión con la base de datos
        conexion = establecer_conexion()
        cursor = conexion.cursor()
        #Umbral definido de presión:
        umbral = obtener_umbral_tiposensor(3)
        
        # Ejecutar consulta SQL
        consulta = """SELECT DISTINCT t.nombre as TipoSensor, FORMAT(l.valor, 2) as Valor, 
                    DATE_FORMAT(l.fecha_hora, '%d/%m/%Y %H:%i') as FechaHora 
                    FROM lecturas l inner join tipos_sensor t on t.id = l.idtipo_sensor 
                    WHERE idtipo_sensor = 3 and valor > %s"""
        
        cursor.execute(consulta, (umbral,))
        # Resultados
        resultados = cursor.fetchall()
        
        # Mostrar las fechas con presión elevada
        for registro in resultados:
            print("Tipo de sensor:", registro[0], "Valor:", registro[1], "Fecha:", registro[2])
            
    except mysql.connector.Error as error:
        print(f"Error al ejecutar la consulta: {error}")
    finally:
        cursor.close()
        conexion.close()
    


