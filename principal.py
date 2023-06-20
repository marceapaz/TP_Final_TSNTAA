from alertas import control_temperatura
from consultasavanzadas import contar_lecturas_presion
from fluctuaciones import gestion_fluctuacion
import datoshistoricos
import lecturas
import estadisticas
import tendencias

def mostrar_menu():
    print("Bienvenidos al sistema de alarma de cilos. Por favor seleccione una opción:")
    print("1. Alertas")
    print("2. Consultas")
    print("3. Datos históricos")
    print("4. Estadísticas")
    print("5. Lecturas")
    print("6. Tendencias")
    print("7. Fluctuaciones")
    print("8. Salir")
    print()

# Funciones principales 
def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            control_temperatura()
        elif opcion == "2":
            contar_lecturas_presion()
        elif opcion == "3":
            datoshistoricos.obtener_promedio_humedad()
        elif opcion == "4":
            estadisticas.contar_eventos_rotura_fuga()
        elif opcion == "5":
            lecturas.obtener_lecturas_temperatura()
        elif opcion == "6":
            tendencias.obtener_fechas_presion_elevada(10)
        elif opcion == "7":
            gestion_fluctuacion()
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    # Ejecutar el menú 
    main()
