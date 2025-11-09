def porcentaje_genero(info: dict):
    totalHombres = sum(1 for paciente in info.values()
                       if paciente["genero"] == 1)
    totalMujeres = sum(1 for paciente in info.values()
                       if paciente["genero"] == 2)
    total = len(info)
    print(f"Porcentaje de hombres: {round((totalHombres / total) * 100)}%")
    print(f"Porcentaje de mujeres: {round((totalMujeres / total) * 100)}%")


def informacion_paciente(info: dict, costos: dict):
    for paciente in info:
        costoTotal = sum(costos[paciente])
        print(f"Nombre del paciente: {info[paciente]["nombre"]}")
        print(
            f"Género: {"Masculino" if info[paciente]["genero"] == 1 else "Femenino"}")
        print(f"Edad: {info[paciente]["edad"]}")
        print(
            f"Antecedentes diabeticos: {"Sí" if info[paciente]["diabetes"] == 1 else "No"}")
        print(
            f"Antecedentes hipertensicos: {"Sí" if info[paciente]["hipertension"] == 1 else "No"}")
        print(
            f"Antecedentes cardiovasculares: {"Sí" if info[paciente]["cardiovascular"] == 1 else "No"}")
        print(f"IMC: {info[paciente]["imc"]}")
        print(f"Costo total a pagar: {costoTotal}")
        print("\n" + "=" * 60 + "\n")


def promedio_obesidad(info: dict):
    obesos = [paciente["edad"]
              for paciente in info.values() if paciente["imc"] >= 30]
    if not obesos:
        print("No hay pacientes con condición de obesidad.")
    else:
        promedio = round(sum(obesos) / len(obesos))
        print(
            f"Promedio de edad de pacientes con alguna condición de obesidad: {promedio} años.")


def preexistencias(info: dict):
    totalDia = sum(1 for paciente in info.values()
                   if paciente["diabetes"] == 1)
    totalHiper = sum(1 for paciente in info.values()
                     if paciente["hipertension"] == 1)
    totalCardio = sum(1 for paciente in info.values()
                      if paciente["cardiovascular"] == 1)

    print(f"Diabetes: {totalDia}")
    print(f"Hipertensión: {totalHiper}")
    print(f"Cardiovascular: {totalCardio}")

    # Determinar mayor y menor frecuencia
    preex = {"Diabetes": totalDia, "Hipertensión": totalHiper,
             "Cardiovascular": totalCardio}
    max_enf = max(preex)
    min_enf = min(preex)
    print("\n-------Enfermedad preexistente más y menos frecuente-------\n")
    print(f"Más frecuente: {max_enf}")
    print(f"Menos frecuente: {min_enf}")


def dinero_recaudado(costos: dict):
    total_recaudado = sum(sum(costo) for costo in costos.values())
    print(f"Dinero total recaudado por la clínica: ${total_recaudado}")
