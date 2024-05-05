'''
Se denomina variable porque su valor puede cambiar, son modificables a lo largo del codigo.

La variable se declara y se define, por ejemplo:
a = 5  (en este ejemplo declaramos que la variable tiene el nombre de A y se define que su valor es 5)

las variables pueden escribirse en minuscula, en caso de ser mas de una palabra
la 2da comienza con mayus, por ejemplo:
holaMundo = (), holaQueTalComoEstas = ()      (a esto se lo conoce como camelCase)
o podemos separarlo con "_", por ejemplo:
hola_mundo = ()                               (esto se llama snake_case) *RECOMENDADO PARA PYTHON*

las variables tambien pueden ser eliminadas usando el operador del, por ejemplo: del holaMundo

Concatenacion: es cuando unimos dos string, por ejemplo "aaa" + "bbb" = "aaabbb". por ejemplo:
nombre="gonzalo "
saludo="Hola " + nombre + "como estas?"
print(saludo)                                      (este codigo nos muesta "Hola gonzalo como estas?)

tambien podemos concatenar usando fstring, por ejemplo:
nombre="gonzalo "
saludo=f"Hola {nombre} como estas?"                (para crear un fstring se pone la f antes de las "")
print(saludo)                                      (el codigo sigue mostrando el mismo resultado)

tambien podemos usar operadores de pertenencia para buscar algo dentro de una variable, por ejemplo:
saludo=f"Hola {nombre} como estas?"
print("omo" in saludo)                     (este codigo va a mostrar true en la consola, porque "omo"
                                            esta dentro de la palabra "como". en caso de que no 
                                            encuentre coincidencias, el codigo muestra false)
tambien podemos usar 
print("omo" not in saludo)                 (en este caso muestra false porque al poner not in evalua
                                            si "omo" esta en saludo y para mostrar true espera que 
                                            "omo"  no se encuentre en la variable saludo)
'''