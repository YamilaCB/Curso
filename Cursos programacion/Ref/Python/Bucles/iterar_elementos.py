'''
Se utilizan los bucles para repetir de forma controlada la ejecucion de un codigo
*iterar: es recorrer un dato por medio de sus elementos*


bucle for para recorrer una lista:
animales = ["gato", "perro", "loro", "cocodrilo"]
for animal in animales:
    print (animales)
este buclea va a imprimir en pantalla todos los elementos de la lista hasta que llegue al 
ultimo, ahi el bucle termina
En este ejemplo animal es una variable que se crea para recorrer el bucle

para recorrer una lista de numeros:
for numero in numeros:
    resultado = numero * 10
    print(resultado)

para recorrer 2 listas al mismo tiempo se puede hacer de la siguiente forma:
for numero, animal in zip(animales, numeros):
    print(numero)
    print(animal)
se accede al valor de la primer lista, luego al primer valor de la segunda, y asi hasta terminar el bucle

forma de recorrer una lista por su indice:
for num in enumerate(numeros)
    print(num)
esto devuelve 2 valores, donde el primero es el indice y el 2do es el valor

*si usamos else y no ponemos un break, siempre se va a mostrar al final del bucle*
*funciona igual para tuplas y conjuntos*
'''