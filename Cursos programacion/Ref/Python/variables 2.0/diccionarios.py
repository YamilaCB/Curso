'''
diccionario = dict(nombre="gonzalo",apellido="arramon")
en este ejemplo creamos un diccionario usando la funcion dict.
*al igual que las tuplas, listas, etc. No podemos crearlos vacios al menos que usemos la funcion*

crear diccionarios con fromkeys:
diccionario = dict.fromkeys(["nombre","apellido"])
en este caso se crea un diccionario donde todos los elementos estaran vacios y su valor es "none"
hasta que sea reemplazado por algun valor
tambien se puede cambiar el valor por defecto del diccionario de la siguiente forma:
diccionario = dict.fromkeys(["nombre","apellido"], "indefinidos")
en este ejemplo mostrara un diccionarios con "nombre" y "apellido" donde el valor dentro de cada uno sera
"indefinidos"
'''