def empresa():
    print("SALUD-CARE")
    print("__________")
    infoPacientes = {}
    costosPacientes = {}

    # Ingreso de datos 

    cant = int(input("\nCantidad de pacientes: "))
    print("===============================================================")
    
    while cant <= 0:
        cant = int(input("\nCantidad de pacientes: "))
        print("===============================================================")
            
    for i in range(cant):
        info = []
        name = str(input("Ingrese los nombres y apellidos: "))
        gender = int(input("Género (1 - Masculino / 2 - Femenino): "))
        
        while gender != 1 and gender != 2:
            gender = int(input("Género (1 - Masculino / 2 - Femenino): "))
                
        age = int(input("Edad (mayor o igual a 10 años): "))  
        
        while age < 10:
            age = int(input("Edad (mayor o igual a 10 años): "))
            
        antDia = int(input("Antecedentes diabeticos (1 - Sí / 2 - No): "))
        
        while antDia != 1 and antDia != 2:
            antDia = int(input("Antecedentes diabeticos (1 - Sí / 2 - No): "))
        
        antHiper = int(input("Antecedentes hipertensicos (1 - Sí / 2 - No): "))
        
        while antHiper != 1 and antHiper != 2:
            antHiper = int(input("Antecedentes hipertensicos (1 - Sí / 2 - No): "))
        
        antCardio = int(input("Antecedentes cardiovasculares (1 - Sí / 2 - No): "))
        
        while antCardio != 1 and antCardio != 2:
            antCardio = int(input("Antecedentes cardiovasculares (1 - Sí / 2 - No): "))
            
        imc = float(input("IMC: "))
        print("===============================================================")
        
        # Metemos los valores en la lista "info"
        info.append(gender)
        info.append(age)
        info.append(antDia)
        info.append(antHiper)
        info.append(antCardio)
        info.append(imc)
        
        # Metemos el nombre en el diccionario con sus datos
        infoPacientes[name] = info
        
        # Condicionales de género/edad
        hombres = 0
        mujeres = 0
            
        for i in infoPacientes:
            costo = []
            costo.append(100000)
            
            if infoPacientes[i][0] == 1:
                hombres += 1
                if infoPacientes[i][1] >= 30 and infoPacientes[i][1] <= 60:
                    costo.append(50000)
                elif infoPacientes[i][1] > 60 and infoPacientes[i][1] <= 70:
                    costo.append(65000)
                    
            if infoPacientes[i][0] == 2:
                mujeres += 1
                if infoPacientes[i][1] >= 30 and infoPacientes[i][1] <= 60:
                    costo.append(55000)
                elif infoPacientes[i][1] > 60 and infoPacientes[i][1] <= 70:
                    costo.append(60000)
                    
            if infoPacientes[i][1] > 70:
                costo.append(75000)
                
            if infoPacientes[i][1] < 30:
                costo.append(0)
                
            costosPacientes[i] = costo
        
        # Porcentaje de hombres y mujeres
        pjHombres = round((hombres * 100) / cant)
        pjMujeres = round((mujeres * 100) / cant)
        

        # Condicionales de antecedentes    
        for i in infoPacientes:
            costo = costosPacientes[i]
            enfPree = 0
            costoEnf = 0
            
            if infoPacientes[i][2] == 1:
                costoEnf = 25000
                enfPree += costoEnf

            if infoPacientes[i][3] == 1:
                costoEnf = 60000
                enfPree += costoEnf

            if infoPacientes[i][4] == 1:
                costoEnf = 40000
                enfPree += costoEnf
                
            costo.append(enfPree)    
            costosPacientes[i] = costo

        # Condicionales IMC 
        for i in infoPacientes:
            costo = costosPacientes[i]
            costoIMC = 0
            
            if infoPacientes[i][5] < 18.5:
                costoIMC = 15000
                costo.append(costoIMC)
                
            elif infoPacientes[i][5] >= 18 and infoPacientes[i][5] < 25:
                costoIMC = 0
                costo.append(costoIMC)
                
            elif infoPacientes[i][5] >= 25 and infoPacientes[i][5] < 27:
                costoIMC = 10000
                costo.append(costoIMC)
                
            elif infoPacientes[i][5] >= 27 and infoPacientes[i][5] < 30:
                costoIMC = 15000
                costo.append(costoIMC)
                
            elif infoPacientes[i][5] >= 30 and infoPacientes[i][5] < 35:
                costoIMC = 20000
                costo.append(costoIMC)
                
            elif infoPacientes[i][5] >= 35 and infoPacientes[i][5] < 40:
                costoIMC = 35000
                costo.append(costoIMC)
                
            elif infoPacientes[i][5] >= 40 and infoPacientes[i][5] <= 50:
                costoIMC = 50000
                costo.append(costoIMC)
                
            elif infoPacientes[i][5] > 50:
                costoIMC = 100000
                costo.append(costoIMC)
                
            costosPacientes[i] = costo
            
    print("\n-----------Menú de opciones-----------")
    print("1. Porcentaje de hombres y mujeres atendidos.")
    print("2. Información de cada paciente.")
    print("3. Promedio de edad de los clientes con alguna condición de obesidad.")
    print("4. Cantidad de clientes con preexistencias de diabetes, hipertensión o problemas cardiovasculares.")
    print("Indique cuál es el tipo de preexistencia que se presenta con mayor frecuencia y cual con menor frecuencia.")
    print("5. Cantidad total de dinero recaudado de clientes registrados.\n")     
        
    while True:
        opcion = int(input("Opción: "))
        print("---------------------------------------")
        if opcion == 1:
            print(f"Porcentaje de hombres: {pjHombres}%")
            print(f"Porcentaje de mujeres: {pjMujeres}%")

        elif opcion == 2:
            for i in infoPacientes:
                costoTotal = 0
                total = 0
                for x in range(len(costosPacientes[i])):
                    total += costosPacientes[i][x]
                print("Nombres y apellidos:", i)
                print("Género:", infoPacientes[i][0])
                print("Edad:", infoPacientes[i][1])
                print("Antecedentes diabeticos:", infoPacientes[i][2])
                print("Antecedentes hipertensicos:", infoPacientes[i][3])
                print("Antecedentes cardiovasculares:", infoPacientes[i][4])
                print("IMC:", infoPacientes[i][5])
                print("Costo total a pagar:", total)
                print("---------------------------------------")
          
        elif opcion == 3:
            total = 0
            edadObesidad = 0
            promedioObesidad = 0
            
            for i in infoPacientes:
                if infoPacientes[i][5] >= 30:
                    edadObesidad += infoPacientes[i][1]
                    total += 1
                            
            if total == 0:
                print("No hay ninguna persona con condición de obesidad.")
            elif total != 0:       
                promedioObesidad = round(edadObesidad / total)
                print(f"Promedio de edad de pacientes con alguna condición de obesidad: {promedioObesidad}%")
                
        elif opcion == 4:
            totalDia = 0
            totalHiper = 0
            totalCardio = 0
                
            for i in infoPacientes:
                if infoPacientes[i][2] == 1:
                    totalDia += 1
                    
                if infoPacientes[i][3] == 1:
                    totalHiper += 1
                    
                if infoPacientes[i][4] == 1:
                    totalCardio += 1
                    
            print(f"Diabetes: {totalDia}")
            print(f"Hipertensión:{totalHiper}")
            print(f"Cardiovascular:{totalCardio}")
            
            
            if totalDia > totalHiper > totalCardio:
                print("La preexistencia con mayor frecuencia es diabetes.")
                print("La preexistencia con menor frecuencia es cardiovascular.")
            elif totalHiper < totalCardio < totalDia:
                print("La preexistencia con mayor frecuencia es diabetes.")
                print("La preexistencia con menor frecuencia es hipertensión.")
            elif totalHiper > totalDia > totalCardio:
                print("La preexistencia con mayor frecuencia es hipertensión.")
                print("La preexistencia con menor frecuencia es cardiovasculares.")
            elif totalDia < totalCardio < totalHiper:
                print("La preexistencia con mayor frecuencia es hipertensión.")
                print("La preexistencia con menor frecuencia es diabetes.")
            elif totalCardio > totalHiper > totalDia:
                print("La preexistencia con mayor frecuencia es cardiovascular.") 
                print("La preexistencia con menor frecuencia es diabetes.")  
            elif totalHiper < totalDia < totalCardio:
                print("La preexistencia con mayor frecuencia es cardiovascular.")
                print("La preexistencia con menor frecuencia es hipertensión.")
            elif totalDia > totalHiper == totalCardio:
                print("La preexistencia con mayor frecuencia es diabetes.")
                print("La preexistencias con menor frecuencia es hipertensión y cardiovasculares.")
            elif totalDia < totalHiper == totalCardio:
                print("La preexistencias con mayor frecuencia es hipertensión y cardiovasculares.")
                print("La preexistencias con menor frecuencia es diabetes.")
            elif totalDia == totalHiper > totalCardio:
                print("La preexistencias con mayor frecuencia es hipertensión y diabetes.")
                print("La preexistencia con menor frecuencia es cardiovascular.")
            elif totalDia == totalHiper < totalCardio:   
                print("La preexistencias con mayor frecuencia es cardiovascular.")
                print("La preexistencias con menor frecuencia es hipertensión y diabetes.")
            elif totalDia == totalCardio > totalHiper:
                print("La preexistencias con mayor frecuencia es diabetes y cardiovasculares.")
                print("La preexistencias con menor frecuencia es hipertensión.")
            elif totalDia == totalCardio < totalHiper:
                print("La preexistencias con mayor frecuencia es hipertensión.")
                print("La preexistencias con menor frecuencia es diabetes y cardiovasculares.")
            elif totalDia == totalHiper == totalCardio:
                print("No hay mayor ni menor frecuencia, todas son iguales")
                    
        elif opcion == 5:
            total = 0
            for i in infoPacientes:
                for n in range(len(costosPacientes[i])):
                    total += costosPacientes[i][n]
                                   
            print(f"Dinero recaudado:", total)
                                   
        print("---------------------------------------")                                
        continuar = str(input("¿Quisiera ver otra opción? s/n:"))
                            
        if continuar == "s" or continuar == "S":
            continue 
        elif continuar == "n" or continuar == "N":
            print("\n¡Gracias por usar el programa! Ahora mismo se imprimirán la cotizaciones de cada paciente.")
            break
        else:
            print("Sí o no, por favor")
            break
        
    for i in infoPacientes:
        total = 0
        for n in costosPacientes[i]:
            total += n 
        iva = ((total * 19)/100)
        print("_______________________________________________________________")
        print("                      SALUD CARE Ltda.")
        print()
        print(" Fecha: 11/11/2022")
        print(" Nombre del cliente:", i)
        print()
        print(" Item     Descripción                        Valor/mes")
        print(" 01      Tarifa básica                      $",costosPacientes[i][0])
        print(" 02 Costo mensual género/edad               $",costosPacientes[i][1])
        print(" 03 Costo mensual enf. preexistentes        $",costosPacientes[i][2])
        print(" 04       Costo x IMC                       $",costosPacientes[i][3])
        print("                            ------------------------------------")
        print("                                     Subtotal    $", total)
        print("                                     iva(19%)    $", iva )
        print("                            ------------------------------------")
        print("                                     Total       $", total + iva)
        print()
        print(" Firma asesor Comercial_______________________________")
        print("                     Estamos para servirle")
        print()
        print()
        print("_________________________________________________________________")
        print()
                 
empresa()