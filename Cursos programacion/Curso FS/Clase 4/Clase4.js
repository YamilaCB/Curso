"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var readlineSync = require("readline-Sync");
/*          Estructuras de control
usamos 2 estructuras de control en esta clase, IF donde se crea una condicion y en base a esa
condicion se evalua si es verdadera o falsa.
Y switch donde a la condicion se le da un valor, y se ejecuta una accion dependiendo si el valor
coincide con una de las opciones.
Como crear un comando que repita codigo (loops):
por ejemplo:
while (hayCaminoDelante){
    console.log("Avanzar");
}


while ejecuta una secuencia de instrucciones mientras la condicion sea verdadera
while (condicion){
    (accion)
}


let cantHolas : number = 1            (determina que la variable comienza en 1)
while (cantHolas <= 5){               (indica que mientras sea menor o igual a 5 funciona el loop)
    console.log("hola");              (lo que imprime el codigo)
    cantHolas = cantHolas +1;         (contador que determina que la var se incrementa en 1 en cada loop)
}
*/
var llegadaColectivo;
llegadaColectivo = readlineSync.question("Llego el colectivo? (S/N)");
while (llegadaColectivo == "N") {
    console.log("Todavia no llego");
    llegadaColectivo = readlineSync.question("Llego el colectivo? (S/N)");
}
console.log("Llego el colectivo");
