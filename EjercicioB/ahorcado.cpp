//
//
//  Juego del ahorcado
//  Es un Algoritmo sobre el juego del ahorcado en el cual se le pide una palabra oculta y una descripcion al jugador 1
//  y el jugador 2 tiene que encontrar la palabra oculta con la pista y solo puede cometer 7 fallos
//  Created by Julio Alexander Alvarado Morales ,Jonathan Joel Istupe Martinez, Kevin Josue Tecu Piche
//  on 30/08/23.
//

#include <iostream>
#include <string>
#include <cctype>

using namespace std;

int main() {
    string letras[20];
    int contador, fallos, cantidad_espacios, game_over;
    char posibleLetra;
    string palabra, letras_ingresadas, palabra_armada, descripcion;
    string guion = "_ ";
    bool acerto,repetir_juego;
    char verificador, verificador2;
    
    // Interfaz de Bienvenida
    cout << " ______________" << endl;
    cout << "||            ||" << endl;
    cout << "||            ||              ¡Bienvenido al Juego de Ahorcado!" << endl;
    cout << "||            ||" << endl;
    cout << "|______________|        En este juego, debes adivinar la palabra oculta." << endl;
    cout << " \\############\\" << endl;
    cout << "  \\############\\" << endl;
    cout << "   \\    ____    \\  Tienes un número limitado de intentos para adivinar cada letra." << endl;
    cout << "    \\___\\___\\__\\" << endl;
    //Preguntamos si desea jugar
    cout << "¿Te gustaría jugar? (S/N)" << endl;
    cin >> verificador;
    //Verficamos si va jugar o se sale del juego
    if (tolower(verificador) == 's') {
        //Usamos un bucle para verificar si el usuario quiero jugar otra vez con el parametro verificador2
        do{
            //inicializamos
            contador = -1;
            fallos = -1;
            letras_ingresadas = "";
            posibleLetra = ' ';
            std::memset(letras, '\0', sizeof(letras));
            
            do {
                //Obtenemos la palabra oculta y la descripcion
                system("clear");
                cout << "!-----------------------------------------------------------------!" << endl;
                cout << "|                                                                 |" << endl;
                cout << "|        La palabra oculta debe constar de una sola palabra       |" << endl;
                cout << "|        y además, debe tratarse de una palabra real y válida.    |" << endl;
                cout << "|                                                                 |" << endl;
                cout << "!-----------------------------------------------------------------!" << endl;
                cout << "   ,-------," << endl;
                cout << "  /       / |" << endl;
                cout << " /______ /  /" << endl;
                cout << "|___/___/  /" << endl;
                cout << "|__..___|. " << endl;
                cout << "  //" << endl;
                cout << ".//" << endl;
                //Siempre borramos los espacios cada vez que se repita
                cantidad_espacios = 0;
                //Solicitamos la palabra oculta
                cout << "Escriba la palabra oculta" << endl;
                cin >> palabra;
                //Verificamos si la palabra tiene espacios recorriendo la cadena ingresada y si tiene el entero va aumentando dependiendo los espacios
                //Si el entero es mayor a 0 entonces no sale del bucle Repetir
                for (int i = 0; i < palabra.length(); i++) {
                    if (palabra[i] == ' ') {
                        cantidad_espacios++;
                    }
                }
                //Verificamos si el entero cantidad_espacios es mayor a 0, y si es menor es correcto y pasa a escribir la descripcion
                //La palabra oculta
                if (cantidad_espacios > 0) {
                    cout << "Error: Ingresa solo una palabra." << endl;
                } else {
                    cout << "!----------------------------------------------------!" << endl;
                    cout << "|  Por favor, proporciona una breve descripción que  |" << endl;
                    cout << "|  sirva como pista para adivinar la palabra oculta. |" << endl;
                    cout << "!----------------------------------------------------!" << endl;

                    cin >> descripcion;
                }
            }while (cantidad_espacios > 0);
            
            game_over = 0;
            //game_over = 0 : El usuario todavia tiene oportunidades
            //game_over = 1 : El usuario perdio
            //game_over = 2 : El usuario gano
            while (game_over == 0) {
                //Va aumentando cada el contador por cada ciclo que se cumple
                contador ++;
                //Limpiamos parametros
                acerto = false;
                palabra_armada = "";
                //Inicializacion de interfaz de ahorcado
                cout << "            __               ___________________________________" << endl;
                cout << "           (  )              |[] Shell                   |F]||*|" << endl;
                cout << "            ||               |*******************************|*|" << endl;
                cout << "            ||               |         Juego el Ahorcado     | |" << endl;
                cout << "        ___|  |__.._         |                               | |" << endl;
                cout << "       /____________\\        |                               | |" << endl;
                cout << "       \\____________/~~~.    |_______________________________|/|" << endl;
                cout << " " << endl;
                cout << "Descripcion de la palabra oculta:  " << descripcion << endl;
                
                //Aqui se empieza a recorrer la palabra ingresada para ver si la letra ingresada esta dentro de la palabra
                for (int i = 0; i < palabra.length(); i++) {
                    //Verificamos si la letra ingresada por el usuario es igual a la letra de la palabra que estamos recorriendo
                    if (tolower(posibleLetra) == tolower(palabra[i])) {
                        letras[i] = posibleLetra;
                        acerto = true;
                    } else {
                        //La primera ves va colocar a todos los caracteres con gion bajo para despues remplazar el guion
                        if (contador == 0) {
                            letras[i] = letras[i] + guion;
                        }
                    }
                }
                //Va contando los fallos que el usuario tenga
                if (!acerto) {
                    fallos++;
                }
                // va sumando todas las letras ingresadas por el usuario y se le haga mas facil para no repetir ni una
                letras_ingresadas += posibleLetra;
                
                cout << endl;
                cout << "Cual sera ?" << endl;
                //Recorremos la lista de letras para mostrar cada letra o gion guardada en una sola linea
                for (int i = 0; i < palabra.length(); i++) {
                    std::cout << letras[i];
                }
                //aqui volvemos armar lo que llevamos de la palabra para verificar despues si el usuario ya la adivino
                for (int i = 0; i < palabra.length(); i++) {
                    palabra_armada += letras[i];
                }
                
                cout << endl << endl;
                cout << "Letras ingresadas: " << letras_ingresadas << endl;
                cout << endl;
                cout << "Intentos fallidos = " << 7 - fallos << endl;
                //Dependiendo la cantidad de fallos es la opcion del dibujo a presentar
                switch (fallos) {
                    case 0:
                        cout << "  _______" << endl;
                        cout << " |     " << endl;
                        cout << " |" << endl;
                        cout << " |" << endl;
                        cout << " |" << endl;
                        cout << "-|-" << endl;
                        break;
                    case 1:
                        cout << "  _______" << endl;
                        cout << " |     |" << endl;
                        cout << " |" << endl;
                        cout << " |" << endl;
                        cout << " |" << endl;
                        cout << "-|-" << endl;
                        break;
                    case 2:
                        cout << "  _______" << endl;
                        cout << " |     |" << endl;
                        cout << " |     O" << endl;
                        cout << " |" << endl;
                        cout << " |" << endl;
                        cout << "-|-" << endl;
                        break;
                    case 3:
                        cout << "  _______" << endl;
                        cout << " |     |" << endl;
                        cout << " |     O" << endl;
                        cout << " |     |" << endl;
                        cout << " |    " << endl;
                        cout << "-|-" << endl;
                        break;
                    case 4:
                        cout << "  _______" << endl;
                        cout << " |     |" << endl;
                        cout << " |     O" << endl;
                        cout << " |     |\\" << endl;
                        cout << " |     " << endl;
                        cout << "-|-" << endl;
                        break;
                    case 5:
                        cout << "  _______" << endl;
                        cout << " |     |" << endl;
                        cout << " |     O" << endl;
                        cout << " |    /|\\" << endl;
                        cout << " |     " << endl;
                        cout << "-|-" << endl;
                        break;
                    case 6:
                        cout << "  _______" << endl;
                        cout << " |     |" << endl;
                        cout << " |     O" << endl;
                        cout << " |    /|\\" << endl;
                        cout << " |    / " << endl;
                        cout << "-|-" << endl;
                        break;
                    case 7:
                        cout << "  _______" << endl;
                        cout << " |     |" << endl;
                        cout << " |     O" << endl;
                        cout << " |    /|\\" << endl;
                        cout << " |    / \\" << endl;
                        cout << "-|-" << endl;
                        break;
                }
                //Recorremos la palabra_armada para volver minuscula cada letra
                for (int i = 0; i < palabra_armada.length(); i++) {
                    palabra_armada[i] = tolower(palabra_armada[i]);
                }
                //Recorremos la palabra para volver minuscula cada letra
                for (int i = 0; i < palabra.length(); i++) {
                    palabra[i] = tolower(palabra[i]);
                }
                //Verificamos si el usuario ya encontro la palabra con la cadena palabra_armada comparandola con la palabra inicial
                if (palabra_armada == palabra) {
                    cout << "                      __      __" << endl;
                    cout << "                      ( _\\    /_ )" << endl;
                    cout << "                      \\ _\\  /_ /" << endl;
                    cout << "                      \\ _\\/_ /_ _" << endl;
                    cout << "                      |_____/_/ /|          " << endl;
                    cout << "                      (  (_)__)J-)" << endl;
                    cout << "                      (  /`.,   /" << endl;
                    cout << "                      \\/  ;   /" << endl;
                    cout << "                      | === |" << endl;
                    cout << " " << endl;
                    cout << "  ________                               __          " << endl;
                    cout << " /  _____/_____    ____ _____    _______/  |_  ____  " << endl;
                    cout << "/   \\  ___\\__  \\  /    \\\\__  \\  /  ___/\\   __\\/ __ \\ " << endl;
                    cout << "\\    \\_\\  \\/ __ \\|   |  \\/ __ \\_\\___ \\  |  | \\  ___/ " << endl;
                    cout << " \\______  (____  /___|  (____  /____  > |__|  \\___  >" << endl;
                    cout << "        \\/     \\/     \\/     \\/     \\/            \\/ " << endl;
                    cout << "         ¡Ganaste! Adivinaste la palabra: "+palabra << endl;
                    cout << "¿Te gustaría volver a jugar? (S/N)" << endl;
                    cin >> verificador2;
                    //Verifica si el usuario quiere jugar otra vez la variable repetir_juegose coloca true
                    verificador2 = tolower(verificador2);
                    if (verificador2 == 's') {
                        repetir_juego = true;
                    }else{
                        repetir_juego = false;
                    }
                    //cambiamos de valor game_over a 2 porque gano
                    game_over = 2;
                }

                //Si ya lleva 7 intentos fallidos perdio y lo verificamos aqui
                if (fallos == 7) {
                    cout << "  ________                                                  " << endl;
                    cout << " /  _____/_____    _____   ____     _______  __ ___________ " << endl;
                    cout << "/   \\  ___\\__  \\  /     \\_/ __ \\   /  _ \\  \\/ // __ \\_  __ \\" << endl;
                    cout << "\\    \\_\\  \\/ __ \\|  Y Y  \\  ___/  (  <_> )   /\\  ___/|  | \\/" << endl;
                    cout << " \\______  (____  /__|_|  /\\___  >  \\____/ \\_/  \\___  >__|   " << endl;
                    cout << "        \\/     \\/      \\/     \\/                   \\/       " << endl;
                    cout << "                         _|  |_" << endl;
                    cout << "                       _|      |_" << endl;
                    cout << "                      | |_|  |_| | " << endl;
                    cout << "                      | |_|  |_| | " << endl;
                    cout << "                   _  |  _    _  |  " << endl;
                    cout << "                  |_|_|_| |__| |_|_|_|" << endl;
                    cout << "                  |_|_|_| |__| |_|_|_| " << endl;
                    cout << "                      |_|      |_| " << endl;
                    cout << "              Perdiste, intentalo de nuevo" << endl;
                    cout << "¿Te gustaría volver a jugar? (S/N)" << endl;
                    cin >> verificador2;
                    //Verifica si el usuario quiere jugar otra vez la variable repetir_juegose coloca true
                    verificador2 = tolower(verificador2);
                    if (verificador2 == 's') {
                        repetir_juego = true;
                    }else{
                        repetir_juego = false;
                    }
                    //cambiamos de valor game_over a 1 porque perdio
                    game_over = 1;

                }
                //Solo si el usuario tiene todavia oportunidades solicitamos la posible palabra
                if (game_over == 0){
                     cin >> posibleLetra;   
                }

            }
        }while(repetir_juego);
        cout << "¡Esperamos que hayas disfrutado el juego!" << endl;
    } else {
        cout << "¡Gracias por considerarlo! ¡Hasta luego!" << endl;
    }

    return 0;
}
