#Un hincha de fútbol desea conocer la cantidad de puntos que su
#equipo lleva acumulados en el campeonato, para ello recibe cada semana la
#información de la cantidad total de partidos, desde el inicio del campeonato, que
#el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado
#recibe un punto, por cada partido ganado tres puntos y por los perdidos cero


ganados = int(input("ingrese la cantidad de partidos ganados: "))
peridos = int(input("ingrese la cantidad de partidos perdidos: "))
empatados = int(input("ingrese la cantidad de partidos empatados: "))

puntos= (3 * ganados) + (2 * empatados) + (0 * peridos)

print("Puntos totales: ", puntos)
