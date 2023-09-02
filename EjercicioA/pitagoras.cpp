/******************************************************************************

                              Juego del ahorcado.
        Es un Algoritmo sobre el juego del ahorcado en el cual se le pide una palabra oculta 
        y una descripcion al jugador 1 y el jugador 2 tiene que encontrar la palabra oculta 
        con la pista y solo puede cometer 7 fallos
        Created by Julio Alexander Alvarado Morales ,Jonathan Joel Istupe Martinez, Kevin Josue Tecu Piche
        on 30/08/23.
*******************************************************************************/
#include <iostream>

int main() {
    // Bucle para el primer lado (lado1)
    for (int lado1 = 1; lado1 <= 500; lado1++) {
        // Bucle para el segundo lado (lado2)
        for (int lado2 = lado1; lado2 <= 500; lado2++) {
            // Bucle para la hipotenusa
            for (int hipotenusa = lado2; hipotenusa <= 500; hipotenusa++) {
                // Verificar si la condición del teorema de Pitágoras se cumple
                if (lado1 * lado1 + lado2 * lado2 == hipotenusa * hipotenusa) {
                    // Si se cumple, imprimir la tripleta de Pitágoras
                    std::cout << "Triple de Pitágoras: (" << lado1 << ", " << lado2 << ", " << hipotenusa << ")" << std::endl;
                }
            }
        }
    }

    return 0;
}
