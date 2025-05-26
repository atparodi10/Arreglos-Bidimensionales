#. Se desea realizar un programa en donde se capture el nombre y tres calificaciones para
#5 estudiantes de la facultad de Ingeniería, y después se pueda procesar dándonos el
#promedio final de cada uno de los alumnos, el resultado se mostrará en pantalla.
import os

os.system('cls')
estudiantes = 5
calificaciones = 3
alumnos = []
for i in range(estudiantes):
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    calif = []
    for j in range(calificaciones):
        calif.append(float(input(f"Ingrese la calificación {j + 1} de {nombre}: ")))
    alumnos.append((nombre, calif))
print("\nResumen de Calificaciones:")
for alumno in alumnos:
    nombre, calif = alumno
    promedio = sum(calif) / len(calif)
    print(f"Nombre: {nombre}, Promedio: {promedio:.2f}")