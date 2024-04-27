print("------------------------------------------")
print("               EJERCICIO 3")
print("------------------------------------------")
correctas = float (input ("Ingrese el numero de respuestas correctas: "))
incorrectas = float (input ("ingrese el numero de respuestas incorrectas: "))
blanco = float (input ("ingrese el numero de respuestas en blanco: "))
rcorrectas = correctas * 3
rincorrectas = incorrectas * -1
rblanco = blanco * 0
puntaje = rcorrectas + rincorrectas + rblanco 
print("El puntaje final es: ", puntaje)
print("------------------------------------------")