import * as readlineSync from 'readline-sync';
    const input = readlineSync.question("Ingrese el numero a evaluar: ")
    const numero = parseFloat(input);
    if (numero === 0){
        console.log("el numero es cero");
    } else if (numero % 2 === 0){
        console.log("El numero es par.")
    } else {
        console.log("El numero es impar")
    }