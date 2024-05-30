def calcular_probabilidad(dados):
    probabilidad = (1/6 ** dados)
    return probabilidad
dados = int(input("Ingrese la cantidad de dados: "))

probabilidad_6= calcular_probabilidad(dados)
print(f"la probabilidad de salir el numero 6 en {dados} es de {probabilidad_6: .2f}")