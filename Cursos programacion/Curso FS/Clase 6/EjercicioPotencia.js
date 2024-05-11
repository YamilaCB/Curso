"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var rsl = require("readline-sync");
var base = rsl.question("ingrese base: ");
var exponente = rsl.question("ingrese exponente (debe ser mayor o igual a 0): ");
if (exponente < 0) {
    console.log("el exponente debe ser mayor o igual a 0");
}
else {
    var resultado_1 = calcularPotencia;
    console.log(resultado_1);
}
function calcularPotencia(base, exponente) {
    var resultado = 1;
    for (var numero = 0; numero < exponente; numero++) {
        resultado *= base;
    }
    return resultado;
}
var resultado = calcularPotencia(base, exponente);
console.log("el resutado es: ", resultado);
