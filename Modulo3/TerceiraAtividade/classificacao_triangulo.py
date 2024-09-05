# Solicita ao usuário o comprimento dos três lados do triângulo
lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

# Verifica se os lados fornecidos podem formar um triângulo
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    # Verifica se todos os lados são iguais
    if lado1 == lado2 == lado3:
        print("O triângulo é Equilátero.")
    # Verifica se dois lados são iguais
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triângulo é Isósceles.")
    else:
        # Se nenhum dos lados for igual, o triângulo é Escaleno
        print("O triângulo é Escaleno.")
else:
    # Caso os lados não formem um triângulo válido
    print("Os lados fornecidos não podem formar um triângulo.")

