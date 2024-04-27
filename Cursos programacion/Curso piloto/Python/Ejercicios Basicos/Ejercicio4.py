print("------------------------------------------")
print("               EJERCICIO 4")
print("------------------------------------------")
ganados = float (input ("Ingrese el numero de partidos ganados: "))
perdidos = float (input ("ingrese el numero de partidos perdidos: "))
empatados = float (input ("ingrese el numero de partidos empatados: "))
pganados = ganados * 3
pperdidos = perdidos * 0
pempatados = empatados * 1
puntaje = pganados + pperdidos + pempatados 
print("El puntaje final es: ", puntaje)
print("------------------------------------------")