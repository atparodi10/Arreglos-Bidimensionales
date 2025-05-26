#1. La Abarrotera ABSA tiene 4 sucursales en las cuales se realizaron diferentes ventas en los
#meses de Julio a diciembre del año 2022, se le ha solicitado a usted realizar un programa en
#donde pueda capturar la siguiente tabla de datos:

ventas = [
    [50000, 60000, 65000, 62000, 78000, 95000],  # ABSA 1
    [89000, 90000, 98000, 80000, 85000, 90000],  # ABSA 2
    [65000, 72000, 85000, 72000, 83000, 98000],  # ABSA 3
    [92000, 88000, 90000, 76000, 82000, 93000]   # ABSA 4
]
# 2. Se desea saber el total de ventas de cada sucursal y el promedio de ventas de cada mes.
nom_tiendas = ["Sucursal 1", "Sucursal 2", "Sucursal 3", "Sucursal 4"]
meses = ["Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
venta_total = []

print(ventas)
for i in range(len(ventas)):
    suma_total = 0
    for j in range(len(ventas[i])):
        suma_total += ventas[i][j]
    print(f"Total de ventas de {nom_tiendas[i]}: {suma_total}")

#venta de todas las tiendas

venta_total = sum(sum(sucursal) for sucursal in ventas)
print(f"Total de ventas de todas las sucursales: {venta_total}")

#tienda que mas vendio
max_venta = max(ventas, key=lambda x: sum(x))
max_venta_index = ventas.index(max_venta)
print(f"La tienda que más vendió es {nom_tiendas[max_venta_index]} con un total de {sum(max_venta)} en ventas.")
#tienda que menos vendio    
min_venta = min(ventas, key=lambda x: sum(x))
min_venta_index = ventas.index(min_venta)
print(f"La tienda que menos vendió es {nom_tiendas[min_venta_index]} con un total de {sum(min_venta)} en ventas.") 