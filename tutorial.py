def calcular_margen():
    print("Calculadora de margen de ganancia\n")

    try:
        costo = float(input("Ingresá el costo del producto: $"))
        precio_venta = float(input("Ingresá el precio de venta: $"))

        if precio_venta < costo:
            print("⚠️ Atención: estás vendiendo por debajo del costo.")
        
        ganancia = precio_venta - costo
        margen = (ganancia / costo) * 100

        print(f"\nGanancia: ${ganancia:.2f}")
        print(f"Margen de ganancia: {margen:.2f}%")

    except ValueError:
        print("⚠️ Error: ingresá solo números válidos.")

# Ejecutar la función
calcular_margen()

