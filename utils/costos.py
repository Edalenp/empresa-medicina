def calcular_costos(paciente: dict) -> list:
    costos = []

    # Tarifa base
    costos.append(100000)

    # Costo por género y edad
    if paciente["edad"] < 30:
        costo_edad = 0
    elif 30 <= paciente["edad"] <= 60:
        costo_edad = 50000 if paciente["genero"] == 1 else 55000
    elif 60 < paciente["edad"] <= 70:
        costo_edad = 65000 if paciente["genero"] == 1 else 60000
    else:
        costo_edad = 75000
    costos.append(costo_edad)

    # Costo por enfermedades preexistentes
    costo_enf = ((25000 if paciente["diabetes"] == 1 else 0) 
                + (60000 if paciente["hipertension"] == 1 else 0)
                + (40000 if paciente["cardiovascular"] == 1 else 0)
                )
    costos.append(costo_enf)

    # Costo por IMC
    imc = paciente["imc"]
    if imc < 18.5:
        costo_imc = 15000
    elif imc < 25:
        costo_imc = 0
    elif imc < 27:
        costo_imc = 10000
    elif imc < 30:
        costo_imc = 15000
    elif imc < 35:
        costo_imc = 20000
    elif imc < 40:
        costo_imc = 35000
    elif imc <= 50:
        costo_imc = 50000
    else:
        costo_imc = 100000
    costos.append(costo_imc)

    return costos