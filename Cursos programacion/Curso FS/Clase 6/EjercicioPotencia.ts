import * as rsl from 'readline-sync'   
function preguntas(){
const base = rsl.question("ingrese base: ")
const exponente = rsl.question("ingrese exponente (debe ser mayor o igual a 0): ")
if (exponente <0){
    console.log("el exponente debe ser mayor o igual a 0");
}
const resultado = calcularPotencia(base, exponente);
console.log("el resutado es: ", resultado)
return;
}

function calcularPotencia (base: number, exponente: number): number{
let resultado = 1;
for (let numero = 0; numero < exponente; numero++){
    resultado *= base;
}
return resultado
}

