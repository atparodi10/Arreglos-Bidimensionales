def main():
    vendedores = 3
    zonas = 4
    ventas = []

    print("Ingrese la cantidad de computadoras vendidas por cada vendedor en cada zona")

    # El usuariio ingresa los datos de la cantidad de computadoras que vendió cada vendedor en cada zona
    for v in range(vendedores):
        ventas_vendedor = []
        for z in range(zonas):
            while True:
                try:
                    cantidad = int(input(f"Computadoras vendidas por el vendedor {v + 1} en la zona {z + 1}: "))
                    if cantidad < 0:
                        print("Por favor ingrese un número no negativo.")
                        continue
                    ventas_vendedor.append(cantidad)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor ingrese un número entero.")
        ventas.append(ventas_vendedor)

    #Para identificar la zona con más computadoras vendidas
    zonas_totales = [sum(ventas[v][z] for v in range(vendedores)) for z in range(zonas)]
    zona_maxima = max(zonas_totales)
    zona_index = zonas_totales.index(zona_maxima)

    print(f"\nLa zona en la que más computadoras se vendió es la zona {zona_index + 1} con {zona_maxima} computadoras vendidas.")

    #Para identificar el vendedor que menos computadoras vendió
    vendedores_totales = [sum(ventas[v]) for v in range(vendedores)]
    vendedor_minimo = min(vendedores_totales)
    vendedor_index = vendedores_totales.index(vendedor_minimo)

    print(f"El vendedor que menos computadoras vendió es el vendedor {vendedor_index + 1} con {vendedor_minimo} computadoras vendidas.")

    #Cantidad total de computadoras vendidas en todas las zonas por todos los vendedores
    total_ventas = sum(vendedores_totales)
    print(f"La cantidad total de computadoras vendidas por todos los vendedores en todas las zonas es {total_ventas}.")

if __name__ == "__main__":
    main()