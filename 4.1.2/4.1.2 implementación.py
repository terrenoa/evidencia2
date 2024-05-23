precio_metro = float(input("ingrese el precio por metro cuadrado: $ "))
ancho = float(input("ingrese el ancho de la pared en metros: "))
largo = float(input("ingrese largo de la pared en metros: "))

metros_totales = ancho * largo
presupuesto = metros_totales * precio_metro

print('el presupuesto de la obra es: $', presupuesto)