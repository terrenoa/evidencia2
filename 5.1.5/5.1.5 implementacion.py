#Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad. 
#Si el cliente compra más de 12  unidades (y hasta 24 unidades), el costo tiene un descuento del 10%. 
#Si compra más de 24 unidades, el descuento es del 15%. 
#Además posee la promoción a los jubilados. 
#La promoción de jubilados es sumarle un 10% de descuento (si posee otros descuentos, se suma los descuentos). 
#Desarrolle una solución algorítmica para saber cuento debe pagar el cliente

precio_leche = 1000
cant_leche = float(input("Cuantos litros de leche va a llevar? "))
descuento = 1


#DESCUENTO MAYORISTA
if (cant_leche>12 and cant_leche<=24):
    descuento = 0.9
elif (cant_leche>24):
    descuento = 0.85
else:
    descuento = descuento

#DESCUENTO JUBILADO

jubilado=input("Es jubilado? ingrese si o no: ")

if (jubilado == "si"):
    descuento = descuento - 0.1
    print("Felicidades! accede a descuento de jubilado")

precio_final = cant_leche * precio_leche * descuento

print ("Total a pagar: $", precio_final)