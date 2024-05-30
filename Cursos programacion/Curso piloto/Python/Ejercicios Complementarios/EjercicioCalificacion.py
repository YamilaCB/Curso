nombre = str(input("Ingrese nombre del alumno (vacio para cortar): "))
while (nombre != ""):
    practica = int(input("Nota practica: "))
    problemas = int(input("Nota problemas: "))
    teorica = int(input("Nota teorica: "))
    if (practica <= 10 and practica >= 0) and (problemas <= 10 and problemas >= 0) and (teorica <= 10 and teorica >= 0):
        nota_final = (practica * 0.1) + (problemas * 0.5) + (teorica * 0.4)
        print(f"La nota final de {nombre} es: {nota_final: .2f}")
    else:
        print("Error en las notas ingresadas")
nombre= input("Ingrese nombre del alumno (vacio para cortar): ")