#resolver los siguentes ejercicios:
#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
este_curso = 1.5
#duracion de crudos
crudo_promedios = 5
este_curso_crudo = 3.5
#calculando porcentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedios / 10
tiempo_vacio_este_curso = 100 - este_curso * 1000 // este_curso_crudo / 10

#diferencias de duracion
print("------------")
diferencias_con_min = 100 - este_curso / otros_cursos_min * 100
diferencias_con_max = 100 - este_curso * 1000 // otros_cursos_max / 10
'''
en este caso si no ejecutaramos la cuenta de esta manera, muestra un resultado decimal muy largo
con esta operacion lo que hacemos es acortar ese numero
con esta operacion en pocas palabras movemos la coma de lugar, por ejemplo:
10,34532 pasaria a ser 103,4532
luego cortamos ese numero con la division doble (//) por lo que quedaria 103,
y por ultimo volvemos a mover esa , un lugar: 10,3
'''
diferencias_con_promedio = 100 - este_curso / otros_cursos_promedio * 100
#mostrando diferencias con otros cursos
print(f"Este curso dura un {diferencias_con_min}% menos que el mas rapido de otros cursos")
print(f"Este curso dura un {diferencias_con_max}% menos que el mas lento de otros cursos")
print(f"Este curso es un {diferencias_con_promedio}% menos que el promedio")
print("------------")
#mostrando tiempo vacio eliminado
print(f"un curso promedio elimina un {tiempo_vacio_promedio}% de material vacio")
print(f"este curso elimina un {tiempo_vacio_este_curso}% de material vacio")
print("------------")
#mostrando diferencias si los cursos duraran 10 horas
print(f"ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // este_curso / 10} horas de otros cursos")
print(f"ver 10 horas de otro curso equivale a ver {este_curso * 100 // otros_cursos_promedio / 10} horas de este cursos")
print("------------")