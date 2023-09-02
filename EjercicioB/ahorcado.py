import os

letras = [""] * 20
contador = 0
fallos = -1
cantidad_espacios = 1  # Inicializado para que entre al primer bucle
game_over = 0
posibleLetra = ''
palabra = ''
letras_ingresadas = ''
palabra_armada = ''
descripcion = ''
guion = " _"
acerto = False
verificador = ''

print(" ______________")
print("||            ||")
print("||            ||              ¡Bienvenido al Juego de Ahorcado!")
print("||            ||")
print("|______________|        En este juego, debes adivinar la palabra oculta.")
print(" \\############\\")
print("  \\############\\")
print("   \\      ____    \\  Tienes un número limitado de intentos para adivinar cada letra.")
print("    \\_____\\___\\____\\")
print("¿Te gustaría jugar? (S/N)")
verificador = input().lower()

if verificador == 's':
    guion = " _"
    contador = 0
    fallos = -1
    
    while cantidad_espacios > 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        cantidad_espacios = 0
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
        
        print("Escriba la palabra oculta")
        palabra = input()
        
        for i in range(len(palabra)):
            if palabra[i] == ' ':
                cantidad_espacios += 1
        
        if cantidad_espacios > 0:
            print("Error: Ingresa solo una palabra.")
        else:
            print("!----------------------------------------------------!")
            print("|  Por favor, proporciona una breve descripción que  |")
            print("|  sirva como pista para adivinar la palabra oculta. |")
            print("!----------------------------------------------------!")
            descripcion = input()
    
    while game_over == 0:
        contador += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        acerto = False
        palabra_armada = ""
        print("            __               ___________________________________")
        print("           (  )              |[] Shell                   |F]||*|")
        print("            ||               |*******************************|*|")
        print("            ||               |         Juego el Ahorcado     | |")
        print("        ___|  |__.._         |                               | |")
        print("       /____________\        |                               | |")
        print("       \____________/~~~.    |_______________________________|/|")
        print(" ")
        print("Descripcion de la palabra oculta:  " + descripcion)
        
        for i in range(len(palabra)):
            if posibleLetra.lower() == palabra[i].lower():
                letras[i] = posibleLetra
                acerto = True
            else:
                if contador == 1:
                    letras[i] = guion
        
        if not acerto:
            fallos += 1
        
        letras_ingresadas += posibleLetra + " "
        print("")
        print("Cual sera ?")
        
        for i in range(len(palabra)):
            print(letras[i], end='')
        print("\n")
        
        for i in range(len(palabra)):
            palabra_armada += letras[i]
        
        print("")
        print("Letras ingresadas: " + letras_ingresadas)
        print(" ")
        print("Intentos fallidos =", 7 - fallos)

        if fallos == 0:
            print("  _______")
            print(" |     ")
            print(" |")
            print(" |")
            print(" |")
            print("-|-")
        elif fallos == 1:
            print("  _______")
            print(" |     |")
            print(" |")
            print(" |")
            print(" |")
            print("-|-")
        elif fallos == 2:
            print("  _______")
            print(" |     |")
            print(" |     O")
            print(" |")
            print(" |")
            print("-|-")
        elif fallos == 3:
            print("  _______")
            print(" |     |")
            print(" |     O")
            print(" |     |")
            print(" |")
            print("-|-")
        elif fallos == 4:
            print("  _______")
            print(" |     |")
            print(" |     O")
            print(" |    /|\ ")
            print(" |")
            print("-|-")
        elif fallos == 5:
            print("  _______")
            print(" |     |")
            print(" |     O")
            print(" |    /|\ ")
            print(" |")
            print("-|-")
        elif fallos == 6:
            print("  _______")
            print(" |     |")
            print(" |     O")
            print(" |    /|\ ")
            print(" |    / ")
            print("-|-")
        elif fallos == 7:
            print("  _______")
            print(" |     |")
            print(" |     O")
            print(" |    /|\ ")
            print(" |    / \ ")
            print("-|-")
        else:
            print("Haz d")
        if palabra_armada.lower() == palabra.lower():
            print("¡Ganaste! Adivinaste la palabra:", palabra)
            game_over = 2
        
        if fallos == 7:
            print("Perdiste, intentalo de nuevo")
            game_over = 1
        
        posibleLetra = input()
    
    print("¡Esperamos que hayas disfrutado el juego!")
else:
    print("¡Gracias por considerarlo! ¡Hasta luego!")
