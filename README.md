# Descripción del código

Este programa en Python permite al usuario crear y analizar una matriz de números enteros con dimensiones personalizables dentro de un rango limitado (entre 1 y 9 tanto para filas como columnas). El objetivo principal es permitir la práctica de estructuras de control, listas anidadas (matrices), validación de datos y operaciones básicas con matrices.

# Funcionalidades

El programa realiza las siguientes tareas:

    1) Solicita al usuario el tamaño de la matriz:

        a) Se validan los datos para asegurarse de que el número de filas y columnas esté entre 1 y 9.

    2) Solicita los elementos de la matriz:

        a) Solo se aceptan números enteros positivos. Cada elemento se ingresa individualmente por posición [fila][columna].

    3) Muestra la matriz ingresada:

        a) Se imprime en formato tabular para facilitar la visualización.

    4) Calcula y muestra el promedio por columna:

        a) Se recorre cada columna para sumar sus valores y luego calcular su promedio.

    5) Calcula y muestra la suma por fila:

        a) Se recorren las filas y se suman sus elementos individualmente.

    6) Determina el número mayor de toda la matriz:

        a) Se identifica el valor más alto y su ubicación (índice de fila y columna).

# Conceptos Clave Utilizados

    1) Listas anidadas: La matriz es una lista de listas.

    2) Bucles anidados: Para recorrer filas y columnas de la matriz.

    3) Validación de entradas: Manejo de errores con try-except y validación de rangos.

    4) Formateo de impresión: Uso de print() con formato para una visualización clara.


