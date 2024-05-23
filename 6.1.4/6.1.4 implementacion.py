#En una escuela, luego de tomar un determinado examen, es necesario calcular el promedio de notas 
#(las notas van de 0 a 10) de los alumnos de un curso. 
#Se necesita saber si el rendimiento ha sido elevado (el promedio es mayor a 8), 
#aceptable (el promedio está comprendido entre 6 y 8) o bajo (promedio es inferior a 6). 
#Desarrollar un algoritmo que resuelva este problema. Para tener en cuenta: 
#las autoridades del colegio saben cuántos estudiantes del curso han rendido el examen.

cant_alumnos = int (input("ingrese la cantidad de alumnos que rindieron el examen: "))
notas = []

for i in range(cant_alumnos):
    notas.append(int(input(f"ingrese la nota del alumno {i}: ")))

promedio = sum(notas)/cant_alumnos

if (promedio>=8):
    print("el promedio es: ", promedio)
    print("el promedio es elevado")
elif (promedio>6 and promedio<8):
    print("el promedio es: ", promedio)
    print("el promedio es aceptable")
else: 
    print("el promedio es: ", promedio)
    print("el promedio es bajo")
