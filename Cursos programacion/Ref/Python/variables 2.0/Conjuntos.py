'''
conjunto = set(["dato1","dato2"])
print(conjunto)

en este ejemplo creamos un set, recordemos que los sets son datos que nos e pueden modificar
la forma de poner datos que se puedan cambiar dentro de otros que no se pueden cambiar es la siguiente:

conjunto1 = frozenset (["dato1", "dato2"])
conjunto2 = {conjunto1, "dato3"}
print(conjunto2)
de esta manera hay un dato dentro de otros datos, utilizando la palabra reservada frozenset

teoria de conjuntos:
por un lado tenemos un conjunto (A), y por otro lado un subconjunto(B), donde el subconjunto de
toma datos del conjunto A para crear un nuevo conjunto, podemos verificar si un conjunto es
un subconjunto de otro de la siguiente forma:
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,5}
resultado = conjunto2.issubset(conjunto1)
print(resultado)
en este ejemplo el print va a devolver true porque devuelve valores booleanos, y es verdad que
conjunto2 es un subconjunto de conjunto1. Pero si lo hicieramos al reves devuelve false
otra forma es:
resultado = conjunto1 <= conjunto2
print(resultado)

en cambio, cuando tomamos como refencia principal un subconjunto (B), al conjunto con mas datos (A)
se le llama superconjunto de
y la forma de verificarlo es:
resultado = conjunto2.issuperset(conjunto1)             (en consola devuelve false)
resultado = conjunto1 > conjunto2                       *no se usa el =*
print(resultado)


para verificar si hay algun dato en comun entre los dos conjuntos se hace de la siguiente forma:
resultado = conjunto2.isdisjoint(conjunto1)
en este ejemplo da false porque cuando hay elementos iguales es el valor que devuelve
si se repitieran elementos entre conjuntos devuelve true
'''