'''
la estructura else if (elif) permite poner una 2da (o las deseadas) condicion a la estructura if
antes de pasar al else, por ejemplo:

if condicion:         (si da true se ejecuta, el programa termina)
    accion
elif condicion:       (si if dio false, se ejecuta, si da true el programa termina)
     accion
else:                 (si tanto if como los elif dieron false, se ejecuta y el programa termina)
    accion
    
tambien podemos utilizar if anidados donde se deben cumplir 2 condiciones para que el resultado sea true

if condicion:            (si el if principal y el anidado dan true, se ejecutan y el programa termina)
    if condicion:
        accion
    elif condicion:      (si el if principal da true, el anidado da false, se ejecuta elif y si este es
         accion:         true, el programa termina)
    else:                (si no se cumple ninguna de las condiciones anteriores, se ejecuta else
         accion           y el programa termina)
    
'''