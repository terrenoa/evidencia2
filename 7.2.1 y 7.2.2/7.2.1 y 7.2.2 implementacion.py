#Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, 
#guardarlos en una lista y mostrarlos. 

nombre = []
contador = 1

while (contador < 11):
    aux = input(f"Ingrese el {contador}° nombre: ")
    
    if aux in nombre:
        print("El nombre ya ha sido ingresado. Por favor, ingrese un nombre diferente.")
    else:
        nombre.append(aux)
        contador = contador + 1
    
print (nombre)

#Eliminar la tercer y la última persona de la lista del ejercicio 1, luego ordenar la lista y mostrarlo

nombre.pop(2)
nombre.pop(-1)

print(nombre)