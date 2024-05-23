# Pedir que el usuario ingrese (input) nombre de personas y mostrarlos hasta que 
# el valor de lo que ingresa sea “fin”

nombres = []
nuevo_nombre = None

while (nuevo_nombre != "fin"):
    nuevo_nombre = input("Ingrese un nombre o fin para terminar: ")
    if (nuevo_nombre == "fin"):
        print (nombres)
        break
    nombres.append(nuevo_nombre)
    print (nombres)


