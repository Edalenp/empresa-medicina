def validar_entero(mensaje: str, minimo=None, opciones=None) -> int:
    while True:
        try:
            valor = int(input(mensaje))
            if opciones and valor not in opciones:
                print(f"Ingrese una opción válida: {opciones}")
                continue
                
            if minimo is not None and valor < minimo:
                print(f"La edad debe ser mayor o igual a {minimo}.")
                continue
                
            return valor
        except ValueError:
            print("Ingrese un número entero válido.")


def ingresar_paciente() -> dict:
    nombre = str(input("Nombre del paciente: ")).strip()
    genero = validar_entero("Género (1 - Masculino / 2 - Femenino): ", opciones=[1, 2])
    edad = validar_entero("Edad (mayor o igual a 10 años): ", minimo=10)
    diabetes = validar_entero("Antecedentes diabeticos (1 - Sí / 2 - No): ", opciones=[1, 2])
    hipertension = validar_entero("Antecedentes hipertensivos (1 - Sí / 2 - No): ", opciones=[1, 2])
    cardiovascular = validar_entero("Antecedentes cardiovasculares (1 - Sí / 2 - No): ", opciones=[1, 2])

    while True:
        try:
            imc = float(input("Índice de Masa Corporal (IMC): "))
            break
        except ValueError:
            print("Ingrese un número válido para el IMC.")

    print("\n" + "=" * 60 + "\n")

    return {
        "nombre": nombre,
        "genero": genero,
        "edad": edad,
        "diabetes": diabetes,
        "hipertension": hipertension,
        "cardiovascular": cardiovascular,
        "imc": imc
    }
