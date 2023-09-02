
#
#  
#  Juego del ahorcado
#	Es un Algoritmo sobre el juego del ahorcado en el cual se le pide una palabra oculta y una descripcion al jugador 1
# 	y el jugador 2 tiene que encontrar la palabra oculta con la pista y solo puede cometer 7 fallos 
#  Created by Julio Alexander Alvarado Morales ,Jonathan Joel Istupe Martinez, Kevin Josue Tecu Piche
#  on 30/08/23.
#
import os
if __name__ == '__main__':
	letras = [str() for ind0 in range(20)]
	contador = int()
	fallos = int()
	cantidad_espacios = int()
	game_over = int()
	posibleletra = str()
	palabra = str()
	letras_ingresadas = str()
	palabra_armada = str()
	descripcion = str()
	guion = str()
	acerto = bool()
	repetir_juego = bool()
	verificador = str()
	verificador2 = str()
	# Interfaz de Bienvenida
	print(" ______________")
	print("||            ||")
	print("||            ||              ¡Bienvenido al Juego de Ahorcado!")
	print("||            ||")
	print("|______________|        En este juego, debes adivinar la palabra oculta.")
	print(" \\\\############\\\\")
	print("  \\\\############\\\\")
	print("   \\      ____    \\  Tienes un número limitado de intentos para adivinar cada letra.")
	print("    \\_____\\___\\____\\")
	# Preguntamos si desea jugar
	print("¿Te gustaría jugar? (S/N)")
	verificador = input()
	# Verficamos si va jugar o se sale del juego
	if str.lower(verificador)=="s":
		# Usamos un bucle para verificar si el usuario quiero jugar otra vez con el parametro verificador2
		while True:
			# Inicializamos
			guion = " _"
			contador = 0
			fallos = -1
			game_over = 0
			letras_ingresadas = ""
			posibleletra = ""
			while True:
				# Obtenemos la palabra oculta y la descripcion

                # borramos pantallas
				os.system('cls' if os.name == 'nt' else 'clear')
				print("!-----------------------------------------------------------------!")
				print("|                                                                 |")
				print("|        La palabra oculta debe constar de una sola palabra       |")
				print("|        y además, debe tratarse de una palabra real y válida.    |")
				print("|                                                                 |")
				print("!-----------------------------------------------------------------!")
				print("   ,-------,")
				print("  /       / |")
				print(" /______ /  /")
				print("|___/___/  /")
				print("|__..___|. ")
				print("  //")
				print(".//")
				# Siempre borramos los espacios cada vez que se repita
				cantidad_espacios = 0
				# Solicitamos la palabra oculta
				print("Escriba la palabra oculta")
				palabra = input()
				# Verificamos si la palabra tiene espacios recorriendo la cadena ingresada y si tiene el entero va aumentando dependiendo los espacios
				# Si el entero es mayor a 0 entonces no sale del bucle Repetir
				for i in range(1,len(palabra)+1):
					if palabra[i-1:i]==" ":
						cantidad_espacios = cantidad_espacios+1
				# Verificamos si el entero cantidad_espacios es mayor a 0, y si es menor es correcto y pasa a escribir la descripcion 
				# La palabra oculta
				if cantidad_espacios>0:
					print("Error: Ingresa solo una palabra.")
				else:
					print("!----------------------------------------------------!")
					print("|  Por favor, proporciona una breve descripción que  |")
					print("|  sirva como pista para adivinar la palabra oculta. |")
					print("!----------------------------------------------------!")
					descripcion = input()
				if cantidad_espacios==0: break
			#game_over = 0 : El usuario todavia tiene oportunidades
            #game_over = 1 : El usuario perdio
            #game_over = 2 : El usuario gano
			while game_over==0:
				# Va aumentando cada el contador por cada ciclo que se cumple
				contador = contador+1
				# Borramos la consola para simular la funcion de letra encontrada
				os.system('cls' if os.name == 'nt' else 'clear')
				# Limpiamos parametros
				acerto = False
				palabra_armada = ""
				# Inicializacion de interfaz de ahorcado
				print("            __               ___________________________________")
				print("           (  )              |[] Shell                   |F]||*|")
				print("            ||               |*******************************|*|")
				print("            ||               |         Juego el Ahorcado     | |")
				print("        ___|  |__.._         |                               | |")
				print("       /____________\\        |                               | |")
				print("       \\____________/~~~.    |_______________________________|/|")
				print(" ")
				print("Descripcion de la palabra oculta:  "+descripcion)
				# Aqui se empieza a recorrer la palabra ingresada para ver si la letra ingresada esta dentro de la palabra
				for i in range(1,len(palabra)+1):
					# Verificamos si la letra ingresada por el usuario es igual a la letra de la palabra que estamos recorriendo
					if str.lower(posibleletra)==str.lower(palabra[i-1:i]):
						letras[i-1] = posibleletra
						acerto = True
					else:
						# La primera ves va colocar a todos los caracteres con gion bajo para despues remplazar el guion 
						if contador==1:
							letras[i-1] = guion
					# Escribir Minusculas(Subcadena(palabra, i, i)) 
				# Va contando los fallos que el usuario tenga
				if not acerto:
					fallos = fallos+1
				# va sumando todas las letras ingresadas por el usuario y se le haga mas facil para no repetir ni una
				letras_ingresadas = letras_ingresadas+posibleletra+" "
				print("")
				print("Cual sera ?")
				# Recorremos la lista de letras para mostrar cada letra o gion guardada en una sola linea
				for i in range(1,len(palabra)+1):
					print(letras[i-1], end="")
				# aqui volvemos armar lo que llevamos de la palabra para verificar despues si el usuario ya la adivino
				for i in range(1,len(palabra)+1):
					palabra_armada = palabra_armada+letras[i-1]
				print(" ")
				print(" ")
				print("Letras ingresadas: "+letras_ingresadas)
				print(" ")
				print("Intentos fallidos = "+str(7-fallos))
				
                #Dependiendo la cantidad de fallos es la opcion del dibujo a presentar
				if fallos==0:
					print("  _______")
					print(" |     ")
					print(" |")
					print(" |")
					print(" |")
					print("-|-")
				elif fallos==1:
					print("  _______")
					print(" |     |")
					print(" |")
					print(" |")
					print(" |")
					print("-|-")
				elif fallos==2:
					print("  _______")
					print(" |     |")
					print(" |     O")
					print(" |")
					print(" |")
					print("-|-")
				elif fallos==3:
					print("  _______")
					print(" |     |")
					print(" |     O")
					print(" |     |")
					print(" |    ")
					print("-|-")
				elif fallos==4:
					print("  _______")
					print(" |     |")
					print(" |     O")
					print(" |     |\\")
					print(" |     ")
					print("-|-")
				elif fallos==5:
					print("  _______")
					print(" |     |")
					print(" |     O")
					print(" |    /|\\")
					print(" |     ")
					print("-|-")
				elif fallos==6:
					print("  _______")
					print(" |     |")
					print(" |     O")
					print(" |    /|\\")
					print(" |    / ")
					print("-|-")
				elif fallos==7:
					print("  _______")
					print(" |     |")
					print(" |     O")
					print(" |    /|\\")
					print(" |    / \\")
					print("-|-")
				# Verificamos si el usuario ya encontro la palabra con la cadena palabra_armada comparandola con la palabra inicial
				if str.lower(palabra_armada)==str.lower(palabra):
					os.system('cls' if os.name == 'nt' else 'clear')
					print("                      __      __")
					print("                      ( _\\    /_ )")
					print("                      \\ _\\  /_ /")
					print("                      \\ _\\/_ /_ _")
					print("                      |_____/_/ /|          ")
					print("                      (  (_)__)J-)")
					print("                      (  /`.,   /")
					print("                      \\/  ;   /")
					print("                      | === |")
					print(" ")
					print("  ________                               __          ")
					print(" /  _____/_____    ____ _____    _______/  |_  ____  ")
					print("/   \\  ___\\__  \\  /    \\\\__  \\  /  ___/\\   __\\/ __ \\ ")
					print("\\    \\_\\  \\/ __ \\|   |  \\/ __ \\_\\___ \\  |  | \\  ___/ ")
					print(" \\______  (____  /___|  (____  /____  > |__|  \\___  >")
					print("        \\/     \\/     \\/     \\/     \\/            \\/ ")
					print("         ¡Ganaste! Adivinaste la palabra: "+palabra)
					print("¿Te gustaría volver a jugar? (S/N)")
					verificador2 = input()
					#Verifica si el usuario quiere jugar otra vez con la variable repetir_juegos se coloca false
					if str.lower(verificador2)=="s":
						repetir_juego = False
					else:
						repetir_juego = True
					game_over = 2
				# Si ya lleva 7 intentos fallidos perdio y lo verificamos aqui
				if fallos==7:
					os.system('cls' if os.name == 'nt' else 'clear')
					print("  ________                                                  ")
					print(" /  _____/_____    _____   ____     _______  __ ___________ ")
					print("/   \\  ___\\__  \\  /     \\_/ __ \\   /  _ \\  \\/ // __ \\_  __ \\")
					print("\\    \\_\\  \\/ __ \\|  Y Y  \\  ___/  (  <_> )   /\\  ___/|  | \\/")
					print(" \\______  (____  /__|_|  /\\___  >  \\____/ \\_/  \\___  >__|   ")
					print("        \\/     \\/      \\/     \\/                   \\/       ")
					print("                         _|  |_")
					print("                       _|      |_")
					print("                      | |_|  |_| | ")
					print("                      | |_|  |_| | ")
					print("                   _  |  _    _  |  ")
					print("                  |_|_|_| |__| |_|_|_|")
					print("                  |_|_|_| |__| |_|_|_| ")
					print("                      |_|      |_| ")
					print("              Perdiste, intentalo de nuevo")
					print("¿Te gustaría volver a jugar? (S/N)")
					verificador2 = input()
					#Verifica si el usuario quiere jugar otra vez con la variable repetir_juegos se coloca false
					if str.lower(verificador2)=="s":
						repetir_juego = False
					else:
						repetir_juego = True
					game_over = 1
					# Solo si el usuario tiene todavia oportunidades solicitamos la posible palabra
				if game_over==0:
					posibleletra = input()
			if repetir_juego: break
		print("¡Esperamos que hayas disfrutado el juego!")
	else:
		print("¡Gracias por considerarlo! ¡Hasta luego!")