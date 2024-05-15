'''
diccionario = {
    "nombre" = "gonzalo",
    "apellido" = "arramon",
    "edad" = 27
}

key: nos devuelve un objeto dict_item, tambien sirve para iterar los keys
claves = diccionario.keys()
print(claves)
en este ejemplo devuelve "nombre", "apellido", "edad"
 
get: nos devuelve el valor de los datos del diccionario, por ejemplo:
get = diccionario.get("nombre")
print(get)
este ejemplo muestra en consola "gonzalo"
*get al contrario de key no lanza una excepcion si no encuentra coincidencias*

clear: elimina todos los elementos del diccionario
diccionario.clear()

pop: elimina un elemento del diccionario
diccionario.pop("nombre", "apellido")
print(diccionario)
mostraria solo la edad

items: nos muestra un elemento dict_item iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)
nos permite recorrer los elementos para acceder a cada uno de ellos

'''