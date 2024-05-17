const arreglo = [4, 7, 9, 3, 1, 45, 67, 23, 29, 78, 11, 16];
let numeroMasGrande = arreglo[0];

for (let i = 1; i < arreglo.length; i++) {
    if (arreglo[i] > numeroMasGrande) {
        numeroMasGrande = arreglo[i];
    }
}

function esParOImpar(numero: number): string {
    if (numero % 2 === 0){
        return "par";    
    } else {
        return "impar";
    }
}

console.log("El número más grande del arreglo es: ", numeroMasGrande);
console.log(`El número es ${esParOImpar(numeroMasGrande)}`);

