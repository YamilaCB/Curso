frase = input("Escriba una frase y calculo cuanto tardarias si tuvieras que decirlo: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print("------------------------------")
print(f"Dijiste {cantidad_de_palabras} palabras, y tardarias en decirlo {cantidad_de_palabras/2} segundos en decirlo")
print("------------------------------")
print(f"hablando un 30% mas lento lo dirias en {cantidad_de_palabras *100 // 2*1.3/100} segundo")
print("------------------------------")