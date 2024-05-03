"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var readlineSync = require("readline-sync");
var input = readlineSync.question("Ingrese el numero a evaluar: ");
var numero = parseFloat(input);
if (numero === 0) {
    console.log("el numero es cero");
}
else if (numero % 2 === 0) {
    console.log("El numero es par.");
}
else {
    console.log("El numero es impar");
}
