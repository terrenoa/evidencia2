#Mostrar sólo los números pares desde 0 hasta el número ingresado (input). 
#Nota: para saber si un número es par hacer i % 2 == 0)

num=int(input("Ingrese un numero: "))
i=0
while (i<=num):
    if (i%2 ==0):
        print(i)
    i = i+1