/* 
clave --> constante (tiene valor)
claveUsuario --> variable que se crea con el valor que asigna el usuario para comparar
variable intentos = 3;
variable contador=1;
pedir al usuario que ingrese la clave (con readlineSync)
(si usaramos FOR se ejecutan los 3 intento, pero si lo hacemos con WHILE el programa
evalua cada condicion en cada vuelta, y si falla en alguna, el programa se cierra)
mientras contador sea menor o igual a intentos y clave sea distinto de claveUsuario {      (           )
    claveUsuario                                                                           (   WHILE   )
incrementar el contador                                                                    (           )
si intentos es igual a 3 entonces {                                                        (           )
    muestro el msj que agotamos los intentos}                                              (     IF    )
}                                                                                          (           )
*/
import * as rls from "readline-Sync";
const claveReal: string = 'eureka';
let claveUsuario: string = rls.question("Ingrese su clave: ");
let contador: number = 1;
let intentos: number = 2;
while((contador <= intentos) && (claveUsuario != claveReal)){
    claveUsuario = rls.question("Ingrese su clave: ");
    contador++;
}
if (claveReal != claveUsuario){
    console.log("Te has quedado sin intentos");
} else{
    console.log("La clave es correcta")
}

