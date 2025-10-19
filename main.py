from utils.paciente import ingresar_paciente
from utils.costos import calcular_costos
from utils.menu import mostrar_menu
from utils.factura import mostrar_factura

print("SALUD-CARE")
print("_" * 10 + "\n")

infoPacientes = {}
costosPacientes = {}

while True:
    try:
        cantidadPacientes = int(input("Cantidad de pacientes a registrar: "))
        if cantidadPacientes > 0:
            print("\n" + "=" * 60 + "\n")
            break
        else:
            print("Ingrese un número mayor a 0.")
    except ValueError:
        print("Ingrese un número entero válido.")

for numeroPaciente in range(cantidadPacientes):
    paciente = ingresar_paciente()
    nombre = paciente["nombre"]

    infoPacientes[f"Paciente {numeroPaciente + 1}"] = paciente
    costosPacientes[f"Paciente {numeroPaciente + 1}"] = calcular_costos(paciente)

    mostrar_factura(nombre, costosPacientes[f"Paciente {numeroPaciente + 1}"])

print("\n" + "=" * 60 + "\n")

# Mostrar menú de estadísticas
mostrar_menu(infoPacientes, costosPacientes)

print("\nGracias por usar SALUD-CARE Ltda. ¡Hasta pronto!")
