'''
son funciones que usamos aplicadas a un objeto
ejemplos:
cadena1 = "hola"
cadena2 = "como estas"
el metodo es: dato.metodo()

Dir: devuelve todas las cosas que podemos hacer con un objeto (tiene que estar dentro de un print)
print (dir (cadena1))
*esto es una funcion*

Upper: convierte todo a mayusculas
para que sea considerado un metodo se ejecuta de la siguiente manera, por ejemplo:
resultado = cadena1.upper()
en este caso todo lo que esta dentro de cadena1 se transfoma a mayusculas

Lower: igual que el anterior metodo, pero convierte todo a minusculas

Capitalize: convierte la primer letra en mayuscula, pero antes convierte todo a minuscula, como si fuera
un lower, por ejemplo: si lo usamos en esta string "Hola Como Estas" se transforma en
"Hola como estas"

Find: busca una cadena dentro de otra cadena, por ejemplo:
busqueda_find = cadena1.find ("hola")
este ejemplo nos va a devolver en consola el numero 0, porque find nos devuelve la primera posicion donde
se encuentra el string que buscamos, es decir, si hay mas de un "hola" nos devuelve el valor del primero.
Y devielve-1 cuando no encuentra un valor
otra funcion similar es:
busqueda_index = cadena1.index ()
esta funcion hace lo mismo, pero en caso de no encontrar resultado tira un error (excepcion), esto es 
importante para aprender a hacer que los programas no se traben cuando tienen errores

isnumeric: devuelve true o false dependiendo si el dato es o no numerico, por ejemplo
es_numerico = cadena1.isnumeric()
print (es_numerico)
en este caso devuelve false porque dentro de cadena1 no hay numeros

isalpha: al igual que el anterior, devuelve true o false si es alfanumerico 
es_alphanumerico = cadena1.isalpha()
print (es_alphanumerico)
en este caso devuelve true
*los espacios son caracteres especiales, por ende, si estan en lo que analizamos, devuelve un error*

count: similar a find, pero en vez de decirnos si se encontro o no una coincidencia, nos dice
cuantas veces se encuentran coincidencias, por ejemplo:
cantidad_coincidencias = cadena1.count("a")
print (cantidad_coincidencias)
en este ejemplo devuelve 1, porque la letra "a" esta una vez dentro del string "hola"

len: cuenta cuantos caracteres tiene una cadena, por ejemplo:
contar_caracteres = len(cadena1)
print(contar_caracteres)
en este caso devuelve 4, porque cadena1 tiene el string "hola" con 4 caracteres
*se escribe len(cadena1) porque es una funcion, no un metodo*

startswith: sirve para verificar si una cadena empieza con otra cadena dada, por ejemplo
empieza_con = cadena1.startswith("h")
print (empieza_con)
en este caso devuelve true porque "hola" empieza con h

endswith: sirve para verificar si una cadena termina con otra cadena dada, por ejemplo
termina_con = cadena1.endswith("h")
print (termina_con)
en este caso devuelve false porque "hola" no termina con h

replace: reemplaza una parte de la cadena dada, por otra dada, por ejemplo:
cadena_nueva = cadena1.replace("la", "lu")
print (cadena_nueva)
en este caso el resultado sera "holu"

split: devuelve una matriz (lista), separa cadenas con la cadena que le pasemos, por ejemplo:
cadena1 = "hola,como,estas"
cadena_separada = cadena1.split(",")
print(cadena_separada)
este codigo devuelve una lista en la que cada lista tiene el nombre de las palabras que estan separadas 
por "," la lista quedaria ['hola', 'como', 'estas']

'''