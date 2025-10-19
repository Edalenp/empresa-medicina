def mostrar_factura(nombre, costos):
    subtotal = sum(costos)
    iva = subtotal * 0.19
    total = subtotal + iva

    print("_______________________________________________________________")
    print("                      SALUD CARE Ltda.")
    print(" Fecha: 18/10/2025")
    print(f" Cliente: {nombre}")
    print()
    print(f"{'Item':<5} {'Descripción':<35} {'Valor':>10}")
    print(f"{'01':<5} Tarifa básica{'':<22} ${costos[0]:>10,.0f}")
    print(f"{'02':<5} Costo edad/género ${'':<20} {costos[1]:>10,.0f}")
    print(f"{'03':<5} Enf. preexistentes ${'':<18} {costos[2]:>10,.0f}")
    print(f"{'04':<5} Costo IMC{'':<26} ${costos[3]:>10,.0f}")
    print("-" * 55)
    print(f"{'Subtotal':>40} ${subtotal:>10,.0f}")
    print(f"{'IVA (19%)':>40} ${iva:>10,.0f}")
    print(f"{'TOTAL':>40} ${total:>10,.0f}")
    print("_______________________________________________________________\n")
