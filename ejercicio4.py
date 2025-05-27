# Sea M una matriz de enteros de “n” filas por “m” columnas, ambas positivas y menores que 10.

import os

print("="*30)
print("Creación de la matriz".center(30, "="))

while True:
    try:
        print("Las filas deben de ser menor a 10 y mayor a 0".center(50, "*"))
        filas = int(input("Ingresa la cantidad de filas de su matriz: "))
        print("\n")
        
        if filas < 1 or filas > 9:
            print("❗Ingresa un rango valido (1-9)")
            print("\n")
        
        else:
            break
        
    except ValueError:
        print("❌ ERROR. Ingrese un dato valido.")
        print("\n")
    
os.system("cls || clear")

print("="*30)
print("Creación de la matriz".center(30, "="))

while True:
    try:
        print("Las columnas deben de ser menor a 10 y mayor a 0".center(50, "*"))
        columnas = int(input("Ingresa la cantidad de columnas de su matriz: "))
        print("\n")
        
        if columnas < 1 or columnas > 9:
            print("❗Ingresa un rango valido (1-9).")
            print("\n")
        
        else:
            break
        
    except ValueError:
        print("❌ ERROR. Ingrese un dato valido.")
    

matriz = []

for i in range(filas):
    datos = []
    for j in range(columnas):
        while True:
            try:
                numeros = int(input(f"Ingrese el valor de la posicion [{i}.{j}]: "))
                
                if numeros < 0:
                    print("❗Ingrese un número entero positivo.")
                
                else:
                    datos.append(numeros)
                    break
            
            except ValueError:
                print("❌ ERROR. Ingrese un dato valido.")
    
    matriz.append(datos)
    
print()
print("Matriz Ingresada:")
for fila in range(filas):
    for columna in range(columnas):
        print(f"{matriz[fila][columna]:4}", end="")
    print()


print()
print("Promedio por Columna:")
for columna in range(columnas):
    suma = 0
    for fila in range(filas):
        suma += matriz[fila][columna]
        promedio = suma / filas
    
    print(f"Promedio de la columna {columna + 1}: {promedio: .2f}")

print()
print("Suma por fila:")
for fila in range(filas):
    suma = 0
    for columna in range(columnas):
        suma += matriz[fila][columna]
    
    print(f"La suma de la fila {fila + 1} es de: {suma}")


mayor = matriz[0][0]
fila_mayor = 0
columna_mayor = 0

print()
print("Número mayor en la matriz:")
for fila in range(filas):
    for columna in range(columnas):
       if matriz[fila][columna] > mayor:
           mayor = matriz[fila][columna]
           fila_mayor = fila
           columna_mayor = columna
           
print(f"El numero mayor de la matriz es: {mayor} en la posición {fila_mayor}.{columna_mayor}")
