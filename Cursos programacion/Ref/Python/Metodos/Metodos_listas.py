'''
list: crea una lista
lista = list["abc", 5, true]

len: devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

append: agrega elementos a la lista
agregando_con_append = lista.append("hola")

insert: agrega un elemento a la lista en un indice especifico
lista.insert(2, "hola")
se coloca primero el indice, luego el nombre de la lista que vamos a agregar

extend: agrega varios elementos a la lista
lista.extend["abc", 5, true]

pop: elimina elementos de la lista
lista.pop(2) elimina el elemento 2 de la lista, recordar que arranca de 0
tambien podemos eliminar especificamente el ultimo elemento usando -1, -2 el anteultimo, etc
lista.pop(-1)

remove: remueve un elemento por su valor
lista.remove("abc")

clear: elimina todos los elementos de la lista
lista.clear

sort: ordena los elementos de la lista de forma ascendente
lista.sort()
en este metodo nos tira una excepcion si hay cadenas de texto, por lo que debemos eliminarlas todas.
Ademas, primero coloca los false y luego true. Para que esto se muestre al reves puede usarse
lista.sort(reverseTrue)
de esta forma quedarian los numeros de forma descendente, luego true y por ultimo false

reverse: invierte los elementos de la lista sin ordenarlos
lista.reverse()

*para mostrar los anteriores metodos se debe usar un print(), en este ejemplo seria print(lista)*
'''