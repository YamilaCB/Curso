import * as readlineSync from "readline-Sync";

/*          Estructuras de control
usamos 2 estructuras de control en esta clase, IF donde se crea una condicion y en base a esa 
condicion se evalua si es verdadera o falsa.
Y switch donde a la condicion se le da un valor, y se ejecuta una accion dependiendo si el valor
coincide con una de las opciones.
Como crear un comando que repita codigo (loops):
por ejemplo:

while ejecuta una secuencia de instrucciones mientras la condicion sea verdadera
while (condicion){
    (accion)
}


while (hayCaminoDelante){
    console.log("Avanzar");
}

let cantHolas : number = 1            (determina que la variable comienza en 1)
while (cantHolas <= 5){               (indica que mientras sea menor o igual a 5 funciona el loop)
    console.log("hola");              (lo que imprime el codigo)
    cantHolas = cantHolas +1;         (contador que determina que la var se incrementa en 1 en cada loop)
}

let llegadaColectivo : string
llegadaColectivo = readlineSync.question("Llego el colectivo? (S/N)");
while (llegadaColectivo == "N"){
    console.log("Todavia no llego");
    llegadaColectivo = readlineSync.question("Llego el colectivo? (S/N)");
}
console.log("Llego el colectivo")



ESTRUCTURA FOR
for (variable : numero = inicial; condicion; contador){
    (impresion)
}


for (let rueda : number =1; rueda<4; rueda++){
    console.log("Inflar rueda")
}


let suma, nota, promedio : number                           (declara las variables y su tipo)
suma = 0;                                                   (establece un valor a una variable)
for (contador=1; contador < 11; contador++){                (crea el contador y como va a funcionar)
    nota = readlineSync.question("Ingrese la nota: ");      (imprime una pregunta al usuario)
    suma += nota;                                           (suma y asigna en el mismo operador)
}
promedio= suma/10                                           (almacena un valor en una variable)
console.log("El promedio del alumno es: " + promedio);      (imprime un msj mostrando una variable)

*/