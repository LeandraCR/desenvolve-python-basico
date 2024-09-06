import random  # Importa a biblioteca random para gerar números aleatórios

# Gera um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

# Inicia um loop infinito até o usuário acertar o número
while True:
    # Solicita ao usuário que insira um palpite
    palpite = int(input("Adivinhe o número entre 1 e 10: "))

    # Compara o palpite com o número secreto
    if palpite > numero_secreto:
        # Se o palpite for maior que o número secreto, exibe uma mensagem
        print("Muito alto, tente novamente!")
    elif palpite < numero_secreto:
        # Se o palpite for menor que o número secreto, exibe uma mensagem
        print("Muito baixo, tente novamente!")
    else:
        # Se o palpite estiver correto, exibe uma mensagem de sucesso
        print(f"Correto! O número é {numero_secreto}.")
        # Interrompe o loop ao acertar
        break
