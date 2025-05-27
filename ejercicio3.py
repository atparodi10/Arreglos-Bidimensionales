matriz = [
    [1, 2, 3, 7],
    [4, 5, 6, 8]
]
filas = len(matriz)
columnas = len(matriz[0])
linealizado = []
for col in range(columnas):
    for fila in range(filas):
        linealizado.append(matriz[fila][col])
print("Arreglo original:")
for fila in matriz:
    print(fila)
print("\nArreglo linealizado por columnas:")
print(linealizado)
