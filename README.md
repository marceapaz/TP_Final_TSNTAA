# TP_Final_TSNTAA

# Trabajo Práctico Final:

Sistema de Alarma para Silos Bolsa
En este trabajo práctico final, se te solicita desarrollar un sistema de alarma para
silos bolsa que permita detectar y notificar rápidamente cualquier rotura o fuga en
el almacenamiento de granos. Para ello, se utilizará un enfoque basado en la
recolección y análisis de datos a través de sensores. El sistema estará compuesto
por una base de datos, una aplicación de monitoreo y alerta, y se implementarán
consultas en lenguaje Python y SQL para realizar diversas operaciones sobre los
datos.

# Problemática a solucionar

La falta de un sistema de alarma para silos bolsa puede generar pérdidas
económicas importantes en el sector agropecuario. Al no contar con una
herramienta que permita detectar a tiempo la rotura de los silos, el grano
almacenado puede perderse, lo que representa una gran inversión desperdiciada.
Es por eso que se necesita un sistema de alarma para silos bolsa que permita
detectar rápidamente cualquier rotura o fuga y notificar al usuario para que pueda
tomar medidas a tiempo.

# Propuesta de solución

Se propone la creación de un sistema de alarma para silos bolsa que se base en
la recolección y análisis de datos a través de sensores. El sistema estará
compuesto por una serie de sensores de temperatura y humedad colocados en
diferentes puntos del silo bolsa, así como de un sensor de presión que permita
detectar cualquier cambio en la estructura del silo.
La información recolectada por los sensores será enviada a una base de datos en
tiempo real, donde será analizada y procesada para detectar cualquier cambio en
los valores de temperatura, humedad o presión que puedan indicar una rotura o
fuga en el silo.
Una vez que se detecte una anomalía, el sistema enviará una alerta al usuario a
través de una aplicación móvil o por correo electrónico, para que pueda tomar
medidas inmediatas para evitar la pérdida del grano almacenado.
Puntos para reflexionar y debatir en cuanto a la ética y legislación:
Es importante considerar la protección de datos personales de los usuarios que
utilizarán el sistema, así como el cumplimiento de las regulaciones locales y
nacionales en cuanto a la recolección y manejo de datos.
También se debe garantizar la seguridad de la información almacenada en la base
de datos, para evitar posibles vulnerabilidades o ataques externos.

Se solicita la aprobación del proyecto para su desarrollo en el marco del módulo
programador de la Tecnicatura Superior en Nuevas Tecnologías Aplicadas al
Agro. El proyecto cumple con los requisitos establecidos en la consigna y se
propone como una solución viable a la problemática planteada.

# Ejercicios:
1. Creación de la base de datos:
    a) Diseña e implementa la estructura de la base de datos que permita
    almacenar las lecturas de temperatura, humedad y presión, así como
    los eventos de rotura y fuga.
    b) Carga datos de ejemplo en las tablas correspondientes para realizar
    pruebas posteriores.

2. Consultas básicas:
    a) Escribe una consulta en SQL para obtener todas las lecturas de
    temperatura registradas en los últimos 24 horas.
    b) Implementa una función en Python que ejecute la consulta anterior y
    muestre las lecturas de temperatura en forma de lista.

3. Alertas de temperatura:
    a) Crea un script en Python que consulte la temperatura más reciente en
    la base de datos y verifique si supera un umbral predefinido. Si la
    temperatura supera el umbral, genera una alerta y envía un correo
    electrónico al usuario.
    b) Modifica el script anterior para utilizar una estructura condicional y
    determinar si se debe activar una alarma sonora en caso de
    temperatura elevada.

4. Análisis de datos históricos:
    a) Realiza una consulta en SQL para obtener el promedio de humedad de
    todas las lecturas registradas en la base de datos. b.
    b) Implementa una función en Python que ejecute la consulta anterior y
    muestre el promedio de humedad.

5. Estadísticas de eventos:
    a) Desarrolla una consulta en SQL para contar la cantidad total de
    eventos de rotura y fuga registrados en la base de datos en los últimos
    7 días.
    b) Crea una función en Python que ejecute la consulta anterior y muestre
    la cantidad de eventos de rotura y fuga.
    2


6. Análisis de tendencias:
    a) Escribe una consulta en SQL para obtener una lista de fechas en las
    que la presión registrada estuvo por encima de un umbral definido.
    b) Implementa una función en Python que ejecute la consulta anterior y
    muestre las fechas con presión elevada.

7. Consultas avanzadas:
    a) Crea una consulta en SQL que cuente la cantidad de lecturas de
    presión por rango de fechas especificado por el usuario.
    b) Desarrolla una función en Python que permita ingresar las fechas de
    inicio y fin, ejecute la consulta anterior y muestre la cantidad de
    lecturas de presión en el rango especificado.

8. Mejoras y optimizaciones:
    a) Haz una propuesta y realiza mejoras en la estructura de la base de
    datos para optimizar las consultas realizadas en los ejercicios
    anteriores.
    b) Implementa alguna funcionalidad adicional en el sistema de alarma,
    como la detección de fluctuaciones abruptas en los sensores, y
    documenta.

9. Aplicación de contenidos de Ejercicio Profesional

Juan Amuchástegui, es un técnico superior egresado del Instituto Superior Politécnico
Córdoba.

Recién comienza la actividad y empieza a realizar publicidad en relación de sus
Servicios informáticos. Si bien sus competencias técnicas y preparación
profesional se circunscriben solo a la programación, con la intención de captar
al mayor número de potenciales clientes, publicita que también brinda servicios
de soluciones empresariales integrales en lo relativo a hardware y software más
allá que no cuenta con la debida preparación al respecto.

En su desarrollo profesional, se vincula con diversas empresas que
comercializan software. En este marco, acepta en su propio beneficio regalos y
bonificaciones con el objeto de que ella recomiende estos productos a sus
futuros clientes.

Luego de algunos años de ejercicio profesional, el técnico superior tiene varios
clientes que le piden trabajos múltiples. En ese contexto y para no perder los
trabajos pedidos, empieza a realizar productos de baja calidad y apropiándose
sin autorización de imágenes de otros sitios web.
El solo quiere cumplir con su obligación de entregar el trabajo, sin importar el
“como” lo haría.

Juan, le gusta comentar en detalle de sus trabajos de diseño anteriores con otros
clientes e incluso con otros profesionales. No le importa mucho guardar el
secreto profesional de sus trabajos.

¿Qué opinión le merece el comportamiento de Juan Amuchástegui en el relato?

ISPC / Tecnicatura Superior en Nuevas Tecnologías Aplicadas al Agro
A su entender, ¿Cómo debería ser una actuación profesional bajo los principios
De la ética informática? Explique y fundamente.
Las respuestas se deben realizar en función del material bibliográfico disponible
Y de la legislación respectiva Ley 7642 - Ejercicio profesional de las ciencias
informáticas en la provincia de Córdoba.

# PROPUESTA:

# Base de datos:

Para la resolución de este trabajo, se propusieron las siguientes tablas:

Tipos_Evento: Rotura/Fuga
Tipos_sensor: Temperatura, Humedad, Presión
Umbrales: Tabla que permitirá almacenar por tipo de sensor, los umbrales permitidos para el cálculo de datos. 
Umbrales_fluctuacion: Tabla que permitirá almacenar por tipo de sensor, los umbrales permitidos para el cálculo de fluctuaciones. 
Lecturas: Tabla que almacenará las lecturas que se registren/manipulen por tipo de sensor.
Eventos: Tabla que almacenará los eventos que se registren/manipulen(por tipo de evento).
Fluctuaciones: Tabla que almacenará las fluctuaciones que se registren/manipulen por tipo de sensor.

En la carpeta BD del proyecto, se encontrará el DER, la query de creación de la BD, query con inserciones de datos y querys usadas para generar las consultas que luego se consumen desde el sistema.

# Sistema:

Se propone el siguiente menú de opciones:

Bienvenidos al sistema de alarma de cilos. Por favor seleccione una opción:
1. Alertas
2. Consultas
3. Datos históricos
4. Estadísticas
5. Lecturas
6. Tendencias
7. Fluctuaciones
8. Salir

    1. Accede al sistema de alertas. Cuando la temperatura es superior al umbral establecido para el tipo de sensor temperatura, se envía un e-mail y un alerta sonora. 
    El umbral establecido se carga en la tabla Umbrales.

    2. Lecturas de presión por rango de fecha.

    3. Se obtiene el promedio de humedad de todas las lecturas registradas en la base de datos.

    4. Cantidad total de eventos de rotura y fuga registrados en la base de datos en los últimos 7 días.

    5. Temperaturas registradas en las últimas 24hs.

    6. Presiones con umbral superior al definido.

    7. 
        # Fluctuaciones:
        Para el sistema de fluctuaciones, se propone lo siguiente:

        Almacenar en una tabla de la base de datos, cuáles serán los umbrales permitidos para cada tipo de sensor.

        Por ejemplo:
            Los umbrales para el tipo de sensor temperadura, es de 2.

        Para calcular si existe o no una fluctuación, se obtendrá la lectura enterior por tipo de sensor y si la diferencia entre 
        las lecturas (anterior y actual) supera el umbral establecido, se registrará la fluctuación y a su vez se emitirá un alerta de fluctuación (por e-mail, sonara y se registrará en un txt.)

        En caso de que la diferencia este dentro de los párametros permitos como variación normal, el sistema simplemente registrará la lectura.

    8. Salir del sistema.
