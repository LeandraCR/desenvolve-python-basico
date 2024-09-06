import math  # Importa a biblioteca math para usar a constante pi

# Função para calcular o perímetro de um triângulo
# Recebe três inteiros correspondentes aos lados do triângulo
def calcula_perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3  # Retorna a soma dos três lados

# Função para calcular o perímetro de um círculo
# Recebe o raio do círculo como parâmetro
def calcula_perimetro_circulo(raio):
    return 2 * math.pi * raio  # Retorna o perímetro com base na fórmula 2 * pi * raio

# Função para calcular o perímetro de um retângulo ou quadrado
# Recebe um lado obrigatório (lado1) e um opcional (lado2)
def calcula_perimetro_retangulo(lado1, lado2=None):
    if lado2 is None:
        # Se lado2 não for informado, assume que é um quadrado
        return 4 * lado1  # Perímetro de um quadrado é 4 vezes o valor do lado
    else:
        # Se lado2 for informado, calcula o perímetro do retângulo
        return 2 * lado1 + 2 * lado2  # Fórmula para o perímetro de um retângulo

# Função para exibir o menu e processar a escolha do usuário
def exibir_menu():
    while True:  # Loop infinito para manter o menu ativo até o usuário escolher sair
        print("\nEscolha uma opção:")  # Exibe as opções disponíveis
        print("1 - Calcular perímetro do triângulo")
        print("2 - Calcular perímetro do círculo")
        print("3 - Calcular perímetro do retângulo ou quadrado")
        print("4 - Sair")

        opcao = input("Digite a opção desejada: ")  # Recebe a escolha do usuário

        # Processa a escolha do usuário com base na opção selecionada
        if opcao == '1':
            # Se a escolha for 1, pede os lados do triângulo
            lado1 = int(input("Digite o primeiro lado do triângulo: "))
            lado2 = int(input("Digite o segundo lado do triângulo: "))
            lado3 = int(input("Digite o terceiro lado do triângulo: "))
            # Calcula e exibe o perímetro do triângulo
            print(f"O perímetro do triângulo é: {calcula_perimetro_triangulo(lado1, lado2, lado3)}")

        elif opcao == '2':
            # Se a escolha for 2, pede o raio do círculo
            raio = int(input("Digite o raio do círculo: "))
            # Calcula e exibe o perímetro do círculo
            print(f"O perímetro do círculo é: {calcula_perimetro_circulo(raio)}")

        elif opcao == '3':
            # Se a escolha for 3, pede os lados do retângulo ou quadrado
            lado1 = int(input("Digite o primeiro lado: "))
            lado2 = input("Digite o segundo lado (pressione Enter se for um quadrado): ")

            if lado2 == '':
                # Se não houver segundo lado, assume que é um quadrado
                print(f"O perímetro do quadrado é: {calcula_perimetro_retangulo(lado1)}")
            else:
                # Se houver segundo lado, calcula o perímetro do retângulo
                print(f"O perímetro do retângulo é: {calcula_perimetro_retangulo(lado1, int(lado2))}")

        elif opcao == '4':
            # Se a escolha for 4, encerra o programa
            print("Saindo do programa...")
            break  # Sai do loop, terminando o programa

        else:
            # Caso o usuário digite uma opção inválida
            print("Opção inválida! Tente novamente.")

# Executa o menu quando o programa é rodado
exibir_menu()
