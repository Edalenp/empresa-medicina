from utils.estadisticas import (
    porcentaje_genero,
    informacion_paciente,
    promedio_obesidad,
    preexistencias,
    dinero_recaudado
)


def mostrar_menu(info, costos):
    while True:
        print("\n----------- Menú de opciones -----------")
        print("1. Porcentaje de hombres y mujeres atendidos")
        print("2. Información de cada paciente")
        print("3. Promedio de edad con obesidad")
        print("4. Preexistencias más y menos frecuentes")
        print("5. Total recaudado")
        print("6. Salir")
        print("---------------------------------------")

        try:
            opcion = int(input("Opción: "))
        except ValueError:
            print("Ingrese un número válido.")
            continue

        if opcion == 1:
            porcentaje_genero(info)
        elif opcion == 2:
            informacion_paciente(info, costos)
        elif opcion == 3:
            promedio_obesidad(info)
        elif opcion == 4:
            preexistencias(info)
        elif opcion == 5:
            dinero_recaudado(costos)
        elif opcion == 6:
            break
        else:
            print("Opción no válida.")
