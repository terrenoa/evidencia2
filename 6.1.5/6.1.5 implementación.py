#Un profesor de matemática necesita generar la tabla de multiplicar de un número entero comprendido 
#entre 1 y 10. Por ejemplo para el 3 debería aparecer como salida:
#3x1=3
#3x2=6
#3x3=9
#…. y así hasta 10

#5.1 Resuelva este problema utilizando un mientras y de modo que por la salida se emita la tabla tal como se propone.
#5.2 Resuelva este problema utilizando un para y de modo que por la salida se emita la tabla tal como se propone.

multiplicador = int(input("la tabla de que numero quiere generar? "))

contador = 0

print ("CICLO WHILE")
while contador <= 10:
    print(f"{contador} x {multiplicador} = ",contador*multiplicador)
    contador = contador + 1

print("")
print("CICLO FOR")
for i in range(11):
    print(f"{i} x {multiplicador} = ",i*multiplicador)
    i = i + 1

