'''
Estos son datos que tienen dentro otros datos, por eso se los denomina compuestos

los tipos de datos compuestos son:

lista = ["gonzalo", true, 160]       (es un conjunto de datos, modificables)
print(lista)                         (muestra la lista completa)
print(lista[1])                      (muestra el elemento 2 de la lista, en este caso "true",
                                      porque se cuenta del 0 al 9. en este caso "gonzalo" seria 
                                      el elemento 1, indice 0)  *la lista es una matriz*
                                      
tuple = ()                            (funciona igual que la lista pero el valor se pone entre (), 
                                      y esta a diferencia de la lista, no se puede modificar,
                                      importante recordar que la tuple se define con (), pero se muestra
                                      con [], por ejemplo: print(tupla[2]))

set = {"gonzalo", true, 160}          (el conjunto(set) se crea con{}, similar a la lista pero
                                       sus elementos no se pueden modificar, no permite repetir
                                       valores, ademas debemos acceder estas por medio de un 
                                       bucle y no de un indice, y sus datos son desordenados, se pueden
                                       cambiar de lugar)

dict = {                              (diccionario (dict) similar a la lista, pero para mostrar 
    'nombre': "gonzalo",               el valor se debe acceder por el valor asociado, por ejemplo:
    'vive': true,                      print(dict['nombre']), en cuanto a estructura 'nombre' se le llama
    'altura': 160                      key, y a su valor value, al igual que en la lista)   
}                                      *el ultimo valor del dict no lleva coma*
'''
