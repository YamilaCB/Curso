import * as rsl from 'readline-sync'   

const base = rsl.question("ingrese base: ")
const exponente = rsl.question("ingrese exponente (debe ser mayor o igual a 0): ")
if (exponente <0){
    console.log("el exponente debe ser mayor o igual a 0")}
else {
    const resultado= calcularPotencia
        console.log(resultado)
    }

function calcularPotencia (base: number, exponente: number): number{
let resultado = 1;
for (let numero = 0; numero < exponente; numero++){
    resultado *= base;
}
return resultado
}
const resultado = calcularPotencia(base, exponente);
console.log("el resutado es: ", resultado)