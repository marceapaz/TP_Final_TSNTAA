from decimal import Decimal
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import winsound   
from conexion_bd import establecer_conexion

def obtener_umbral_tiposensor(idtipo_sensor):
    conexion = establecer_conexion()
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

def control_temperatura():  
    print("Monitoreando lecturas...")
    conexion = establecer_conexion()
    cursor = conexion.cursor()
    consulta = "SELECT valor FROM lecturas where idtipo_sensor = 1 ORDER BY fecha_hora DESC LIMIT 1"
    cursor.execute(consulta)
    temperatura = cursor.fetchone()[0]
    cursor.close()
    conexion.close()
    temperatura_actual = temperatura
    
    #Obtengo el umbral por tipo de sensor = Temperatura
    temperatura_umbral = obtener_umbral_tiposensor(1)
    
    # Verificar si la temperatura supera el umbral establecido
    if temperatura_actual > temperatura_umbral:
        enviar_alerta_correo(temperatura_actual)
        activar_alarma_sonora()
        
def enviar_alerta_correo(temperatura_actual):
    try:
        print('Preparando conexión SMTP...')
        from email.message import EmailMessage
        import smtplib
        remitente = "tsntaa.apazmarcelo@gmail.com"
        destinatario = "marceysoleapazvidela@gmail.com"
        mensaje = f"¡Alerta! La temperatura actual ({temperatura_actual.quantize(Decimal('0.00'))}°C) ha superado el umbral establecido."
        
        email = EmailMessage()
        email["From"] = remitente
        email["To"] = destinatario
        email["Subject"] = "Alerta de temperatura elevada"
        email.set_content(mensaje)
        smtp = smtplib.SMTP_SSL("smtp.gmail.com")
        
        print('Conectando con el servidor de correo electrónico...')
        smtp.login(remitente, "rmfjpcbyrhpaqwiw")    
        print('Enviando correo electrónico...')
        smtp.sendmail(remitente, destinatario, email.as_string())
        smtp.quit()
        print('El correo electrónico ha sido enviado con éxito')
    except Exception as error:
        print(f'Error al enviar el correo electrónico: {error}')
    finally:
        smtp.quit()
        
        
def activar_alarma_sonora():
    # Reproducir alarma
    for _ in range(3):
        winsound.Beep(1000, 2000)  # Reproduce un pitido a 1000 Hz durante 2 segundos
        time.sleep(0.2)  # Pausa de 0.2 segundos entre los pitidos



