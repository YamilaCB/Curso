print("----------------------------------------------")
print("ingrese valores: ")
numero = int(input("ingrese tipo de calculo (1- multiplicacion, 2-potencia, 3-division: ): "))
v = int (input("ingrese V: "))
switch={
    1: 100*v,
    2: 100**v,
    3: 100/v
    }
val = switch.get (numero, "Numero invalido") 
print(val)
print("----------------------------------------------")