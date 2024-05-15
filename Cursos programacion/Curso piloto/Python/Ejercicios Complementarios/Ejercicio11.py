#Escribir un algoritmo que nos devuelva si un año es o no bisiesto

anio=int(input("Ingrese el año: "))
print("--------------------")
if (anio %400==0) or (anio % 4 == 0) and (anio % 100 != 0):
    print("El año es bisiesto")
else:
    print("el año no es bisiesto ")
print("--------------------")