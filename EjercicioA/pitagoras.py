# Bucle para el primer lado (lado1)
for lado1 in range(1, 501):
    # Bucle para el segundo lado (lado2)
    for lado2 in range(lado1, 501):
        # Bucle para la hipotenusa
        for hipotenusa in range(lado2, 501):
            # Verificar si la condición del teorema de Pitágoras se cumple
            if lado1 ** 2 + lado2 ** 2 == hipotenusa ** 2:
                # Si se cumple, imprimir la tripleta de Pitágoras
                print(f"Triple de Pitágoras: ({lado1}, {lado2}, {hipotenusa})")

