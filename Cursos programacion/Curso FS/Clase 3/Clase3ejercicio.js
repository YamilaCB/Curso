"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var readlineSync = require("readline-sync");
var numero = readlineSync.question("Ingrese el numero a evaluar: ");
if (numero == 0) {
    console.log("el numero es cero");
}
else if (numero % 2 == 0) {
    console.log("El numero es par.");
}
else {
    console.log("El numero es impar");
}
