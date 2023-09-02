//
//  
//  Juego del ahorcado
//	Es un Algoritmo sobre el juego del ahorcado en el cual se le pide una palabra oculta y una descripcion al jugador 1
// 	y el jugador 2 tiene que encontrar la palabra oculta con la pista y solo puede cometer 7 fallos 
//  Created by Julio Alexander Alvarado Morales ,Jonathan Joel Istupe Martinez, Kevin Josue Tecu Piche
//  on 30/08/23.
//
Algoritmo JuegoAhorcado
    Dimension letras[20]
    Definir contador, fallos, cantidad_espacios,game_over Como Entero
    Definir posibleLetra Como Caracter
    Definir palabra, letras_ingresadas,palabra_armada,descripcion Como Cadena
    Definir guion Como Cadena
	Definir acerto,repetir_juego Como Logico
	Definir verificador,verificador2 Como Caracter
	
	// Interfaz de Bienvenida
	Borrar Pantalla
	Escribir " ______________"
	Escribir "||            ||"
	Escribir "||            ||              ¡Bienvenido al Juego de Ahorcado!"
	Escribir "||            ||"
	Escribir "|______________|        En este juego, debes adivinar la palabra oculta."
	Escribir " \\############\\"
	Escribir "  \\############\\"
	Escribir "   \      ____    \  Tienes un número limitado de intentos para adivinar cada letra."
	Escribir "    \_____\___\____\"
	
	//Preguntamos si desea jugar
	Escribir "¿Te gustaría jugar? (S/N)"
	Leer verificador
	
	//Verficamos si va jugar o se sale del juego
	Si Minusculas(verificador) = "s" Entonces
		//Usamos un bucle para verificar si el usuario quiero jugar otra vez con el parametro verificador2
		Repetir
			//Inicializamos
			guion = " _"
			contador = 0
			fallos = -1
			game_over = 0
			letras_ingresadas = ""
			posibleLetra = ""
			Repetir
				//Obtenemos la palabra oculta y la descripcion
				Borrar Pantalla
				Escribir "!-----------------------------------------------------------------!"
				Escribir "|                                                                 |"
				Escribir "|        La palabra oculta debe constar de una sola palabra       |"
				Escribir "|        y además, debe tratarse de una palabra real y válida.    |"
				Escribir "|                                                                 |"
				Escribir "!-----------------------------------------------------------------!"
				Escribir "   ,-------,"
				Escribir "  /       / |"
				Escribir " /______ /  /"
				Escribir "|___/___/  /"
				Escribir "|__..___|. "
				Escribir "  //"
				Escribir ".//"
				//Siempre borramos los espacios cada vez que se repita
				cantidad_espacios = 0
				
				//Solicitamos la palabra oculta
				Escribir "Escriba la palabra oculta"
				Leer palabra
				
				//Verificamos si la palabra tiene espacios recorriendo la cadena ingresada y si tiene el entero va aumentando dependiendo los espacios
				//Si el entero es mayor a 0 entonces no sale del bucle Repetir
				Para i = 1 Hasta Longitud(palabra)
					Si SubCadena(palabra, i, i) = " " Entonces
						cantidad_espacios = cantidad_espacios + 1
					Fin Si
				Fin Para
				
				//Verificamos si el entero cantidad_espacios es mayor a 0, y si es menor es correcto y pasa a escribir la descripcion 
				//La palabra oculta
				Si cantidad_espacios > 0 Entonces
					Escribir "Error: Ingresa solo una palabra."
				Sino
					Escribir "!----------------------------------------------------!"
					Escribir "|  Por favor, proporciona una breve descripción que  |"
					Escribir "|  sirva como pista para adivinar la palabra oculta. |"
					Escribir "!----------------------------------------------------!"
					Leer descripcion
				Fin Si
				
			Hasta Que cantidad_espacios = 0
			
			Mientras game_over = 0  Hacer
				//Va aumentando cada el contador por cada ciclo que se cumple
				contador <- contador + 1
				//Borramos la consola para simular la funcion de letra encontrada
				Borrar Pantalla
				//Limpiamos parametros
				acerto = Falso
				palabra_armada = ""
				//Inicializacion de interfaz de ahorcado
				Escribir "            __               ___________________________________"
				Escribir "           (  )              |[] Shell                   |F]||*|"
				Escribir "            ||               |*******************************|*|"
				Escribir "            ||               |         Juego el Ahorcado     | |"
				Escribir "        ___|  |__.._         |                               | |"
				Escribir "       /____________\        |                               | |"
				Escribir "       \____________/~~~.    |_______________________________|/|"
				Escribir " "
				Escribir "Descripcion de la palabra oculta:  "+descripcion
				
				//Aqui se empieza a recorrer la palabra ingresada para ver si la letra ingresada esta dentro de la palabra
				Para i <- 1 Hasta Longitud(palabra)
					//Verificamos si la letra ingresada por el usuario es igual a la letra de la palabra que estamos recorriendo
					Si Minusculas(posibleLetra) = Minusculas(Subcadena(palabra, i, i)) Entonces
						letras[i] = posibleLetra
						acerto = Verdadero
					SiNo
						//La primera ves va colocar a todos los caracteres con gion bajo para despues remplazar el guion 
						Si contador == 1  Entonces
							letras[i] = guion
						Fin Si
					Fin Si		
				Fin Para
				
				//Va contando los fallos que el usuario tenga
				Si !acerto Entonces
					fallos <- fallos + 1
				Fin Si
				
				// va sumando todas las letras ingresadas por el usuario y se le haga mas facil para no repetir ni una
				letras_ingresadas <- Concatenar(letras_ingresadas, Concatenar(posibleLetra, " "))
				
				
				Escribir ""
				Escribir "Cual sera ?"
				//Recorremos la lista de letras para mostrar cada letra o gion guardada en una sola linea
				Para i <- 1 Hasta Longitud(palabra)
					Escribir Sin Saltar letras[i]
				Fin Para
				
				//aqui volvemos armar lo que llevamos de la palabra para verificar despues si el usuario ya la adivino
				Para i <- 1 Hasta Longitud(palabra)
					palabra_armada = palabra_armada + letras[i]
				FinPara
				
				//
				Escribir " "
				Escribir " "
				Escribir "Letras ingresadas: " + letras_ingresadas	
				Escribir " "
				Escribir "Intentos fallidos = " + ConvertirATexto(7 - fallos)
				
				//Dependiendo la cantidad de fallos es la opcion del dibujo a presentar
				Segun fallos Hacer
					0:
						Escribir "  _______"
						Escribir " |     "
						Escribir " |"
						Escribir " |"
						Escribir " |"
						Escribir "-|-"
					1:
						Escribir "  _______"
						Escribir " |     |"
						Escribir " |"
						Escribir " |"
						Escribir " |"
						Escribir "-|-"
					2:
						Escribir "  _______"
						Escribir " |     |"
						Escribir " |     O"
						Escribir " |"
						Escribir " |"
						Escribir "-|-"
					3:
						Escribir "  _______"
						Escribir " |     |"
						Escribir " |     O"
						Escribir " |     |"
						Escribir " |    "
						Escribir "-|-"
					4:
						Escribir "  _______"
						Escribir " |     |"
						Escribir " |     O"
						Escribir " |     |\"
						Escribir " |     "
						Escribir "-|-"
					5:
						Escribir "  _______"
						Escribir " |     |"
						Escribir " |     O"
						Escribir " |    /|\"
						Escribir " |     "
						Escribir "-|-"
					6:					
						Escribir "  _______"
						Escribir " |     |"
						Escribir " |     O"
						Escribir " |    /|\"
						Escribir " |    / "
						Escribir "-|-"
					7:
						Escribir "  _______"
						Escribir " |     |"
						Escribir " |     O"
						Escribir " |    /|\"
						Escribir " |    / \"
						Escribir "-|-"
				Fin Segun
				
				//Verificamos si el usuario ya encontro la palabra con la cadena palabra_armada comparandola con la palabra inicial
				Si Minusculas(palabra_armada) = Minusculas(palabra) Entonces
					Borrar Pantalla
					Escribir "                      __      __"
					Escribir "                      ( _\    /_ )"
					Escribir "                      \ _\  /_ /"
					Escribir "                      \ _\/_ /_ _"
					Escribir "                      |_____/_/ /|          "
					Escribir "                      (  (_)__)J-)"
					Escribir "                      (  /`.,   /"
					Escribir "                      \/  ;   /"
					Escribir "                      | === |"
					Escribir " "
					Escribir "  ________                               __          "
					Escribir " /  _____/_____    ____ _____    _______/  |_  ____  "
					Escribir "/   \  ___\__  \  /    \\__  \  /  ___/\   __\/ __ \ "
					Escribir "\    \_\  \/ __ \|   |  \/ __ \_\___ \  |  | \  ___/ "
					Escribir " \______  (____  /___|  (____  /____  > |__|  \___  >"
					Escribir "        \/     \/     \/     \/     \/            \/ "
					Escribir "         ¡Ganaste! Adivinaste la palabra: " + palabra
					Escribir "¿Te gustaría volver a jugar? (S/N)"
					Leer verificador2					
					Si Minusculas(verificador2) = "s"  Entonces
						repetir_juego <- Falso
					SiNo
						repetir_juego <- Verdadero
					Fin Si
					game_over <- 2
				Fin Si
				
				//Si ya lleva 7 intentos fallidos perdio y lo verificamos aqui
				Si fallos = 7 Entonces
					Borrar Pantalla
					Escribir "  ________                                                  "
					Escribir " /  _____/_____    _____   ____     _______  __ ___________ "
					Escribir "/   \  ___\__  \  /     \_/ __ \   /  _ \  \/ // __ \_  __ \"
					Escribir "\    \_\  \/ __ \|  Y Y  \  ___/  (  <_> )   /\  ___/|  | \/"
					Escribir " \______  (____  /__|_|  /\___  >  \____/ \_/  \___  >__|   "
					Escribir "        \/     \/      \/     \/                   \/       "
					Escribir "                         _|  |_"
					Escribir "                       _|      |_"
					Escribir "                      | |_|  |_| | "
					Escribir "                      | |_|  |_| | "
					Escribir "                   _  |  _    _  |  "
					Escribir "                  |_|_|_| |__| |_|_|_|"
					Escribir "                  |_|_|_| |__| |_|_|_| "
					Escribir "                      |_|      |_| "
					Escribir "              Perdiste, intentalo de nuevo"
					Escribir "¿Te gustaría volver a jugar? (S/N)"
					Leer verificador2					
					Si Minusculas(verificador2) = "s"  Entonces
						repetir_juego <- Falso
					SiNo
						repetir_juego <- Verdadero
					Fin Si
					game_over = 1
				FinSi
				
				//Solo cuando no a perdido pedira leer letra
				Si game_over = 0 Entonces
					Leer posibleLetra
				Fin Si
				
			Fin Mientras
			
		Hasta Que repetir_juego
		
		Escribir "¡Esperamos que hayas disfrutado el juego!"
	Sino
		//Sale del programa
		Escribir "¡Gracias por considerarlo! ¡Hasta luego!"
    Fin Si
	
FinAlgoritmo
