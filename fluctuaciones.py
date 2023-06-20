from datetime import date
from decimal import Decimal
import smtplib
import winsound
import mysql.connector
from alertas import activar_alarma_sonora, enviar_alerta_correo
from conexion_bd import establecer_conexion

def gestion_fluctuacion():
    try:
        while True:
            idtipo_sensor = input("Ingrese el tipo de sensor (1:Temperatura, 2:Humedad, 3:Presión): ")
            if idtipo_sensor in ["1", "2", "3"]:
                break
            else:
                print("Opción incorrecta. Por favor, ingrese una opción válida.")

        lectura_actual = float(input("Ingrese lectura actual: "))

        conexion = establecer_conexion()
        cursor = conexion.cursor()
        # Obtener la lectura anterior de la base de datos 
        consulta = "SELECT valor FROM lecturas WHERE idtipo_sensor = %s ORDER BY fecha_hora DESC LIMIT 1"
        parametros = (idtipo_sensor,)
        cursor.execute(consulta, parametros)
        resultado = cursor.fetchone()
        lectura_anterior = resultado[0] if resultado else None
        
        # Comparar la diferencia con el umbral de fluctuación
        umbral_fluctuacion = obtener_umbral_fluctuacion(idtipo_sensor)  # Función para obtener el umbral correspondiente
        
        if lectura_anterior is not None:
            diferencia = abs(lectura_actual - float(lectura_anterior))
            if diferencia > umbral_fluctuacion:
                # Registrar la fluctuación en la base de datos
                registrar_fluctuacion(idtipo_sensor, lectura_anterior, lectura_actual, diferencia)     
                # Envío de alerta por e-mail
                enviar_alerta_correo(idtipo_sensor, diferencia)
                # Se reutiliza el disparo de alarma desde el archivo alertas.py
                activar_alarma_sonora()
                # Registro en un archivo txt
                registrar_en_archivo(idtipo_sensor, diferencia)
        
        # Actualizar la lectura actual en la base de datos
        registrar_lectura_actual(idtipo_sensor, lectura_actual)
    except mysql.connector.Error as error:
        print(f"Error al ejecutar la consulta: {error}")
    finally:
        cursor.close()
        conexion.close()

def enviar_alerta_correo(idtipo_sensor, diferencia):
        print('Preparando conexión SMTP...')
        from email.message import EmailMessage
        import smtplib
        remitente = "tsntaa.apazmarcelo@gmail.com"
        destinatario = "marceysoleapazvidela@gmail.com"
        
        tipodesensor = obtener_tipo_sensor(idtipo_sensor)
        diferencia_decimal = Decimal(diferencia)
        mensaje = f"Se detectó una fluctuación de {diferencia_decimal.quantize(Decimal('0.00'))} en el sensor {tipodesensor}."
        
        email = EmailMessage()
        email["From"] = remitente
        email["To"] = destinatario
        email["Subject"] = "Alerta de fluctuación detectada"
        email.set_content(mensaje)
        smtp = smtplib.SMTP_SSL("smtp.gmail.com")
        
        print('Conectando con el servidor de correo electrónico...')
        smtp.login(remitente, "rmfjpcbyrhpaqwiw")    
        print('Enviando correo electrónico...')
        smtp.sendmail(remitente, destinatario, email.as_string())
        smtp.quit()
        print('El correo electrónico ha sido enviado con éxito')
    
def registrar_en_archivo(idtipo_sensor, diferencia):
    try:
        tipodesensor = obtener_tipo_sensor(idtipo_sensor)
        diferencia_decimal = Decimal(diferencia) 
        with open("registro.txt", "a") as archivo:
            # Escribir la información de la fluctuación en un archivo llamado registro.txt
            archivo.write(f"Fluctuación detectada en el sensor {tipodesensor}: {diferencia_decimal.quantize(Decimal('0.00'))}\n")
    except Exception as error:
        print(f'Error al enviar el correo electrónico: {error}')
        
def obtener_umbral_fluctuacion(idtipo_sensor):
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()
        consulta = "SELECT umbral FROM Umbrales_fluctuacion WHERE idtipo_sensor = %s LIMIT 1"
        parametros = (idtipo_sensor,)
        cursor.execute(consulta, parametros)
        resultado = cursor.fetchone()
        if resultado:
            umbral = resultado[0]
            return umbral
        else:
            return None
    except mysql.connector.Error as error:
        print(f"Error al ejecutar la consulta: {error}")
    finally:
        cursor.close()
        conexion.close()

def obtener_tipo_sensor(idtipo_sensor):
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()
        consulta = "SELECT nombre FROM Tipos_sensor WHERE id = %s LIMIT 1"
        parametros = (idtipo_sensor,)
        cursor.execute(consulta, parametros)
        resultado = cursor.fetchone()
        if resultado:
            umbral = resultado[0]
            return umbral
        else:
            return None
    except mysql.connector.Error as error:
        print(f"Error al ejecutar la consulta: {error}")
    finally:
        cursor.close()
        conexion.close()
    
def registrar_fluctuacion(idtipo_sensor, lectura_anterior, lectura_actual, diferencia):
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()

        # Insertar los datos en la tabla de fluctuaciones
        consulta = """INSERT INTO fluctuaciones (idtipo_sensor, lectura_anterior, lectura_actual, magnitud_fluctuacion, fecha_hora) 
                    VALUES (%s, %s, %s, %s, NOW())"""
        valores = (idtipo_sensor, lectura_anterior, lectura_actual, diferencia)
        cursor.execute(consulta, valores)

        # Commit de query
        conexion.commit()
    except mysql.connector.Error as error:
        print(f"Error al ejecutar la consulta: {error}")
    finally:
        cursor.close()
        conexion.close()

def registrar_lectura_actual(idtipo_sensor, valor):
    try:
        conexion = establecer_conexion()
        cursor = conexion.cursor()

        # Registrar lectura
        consulta = "INSERT INTO lecturas (idtipo_sensor, valor, fecha_hora) VALUES (%s, %s, NOW())"
        valores = (idtipo_sensor, valor)
    
        cursor.execute(consulta, valores)
        # Commit de query
        conexion.commit()

        print("Lectura actual registrada en la base de datos.")
    except mysql.connector.Error as error:
        print("Error al registrar la lectura actual:", error)
    finally:
        # Cerrar el cursor y la conexión a la base de datos
        cursor.close()
        conexion.close()

# registrar_lectura_actual(1, 25.5)
# registrar_lectura_actual(2, 65.2)
# registrar_lectura_actual(3, 1013.2)
    
# Llamada al método de gestión de fluctuacion
#gestion_fluctuacion()