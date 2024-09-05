# Solicita ao usuário que insira uma avaliação para o filme, de 1 a 5, e converte o valor de entrada em um número inteiro.
avaliacao = int(input("Insira a avaliação do filme (1 a 5): "))

# Verifica se a avaliação é igual a 5.
if avaliacao == 5:
    # Se for igual a 5, exibe a mensagem "Excelente!"
    print("Excelente!")
# Verifica se a avaliação é igual a 4.
elif avaliacao == 4:
    # Se for igual a 4, exibe a mensagem "Muito Bom!"
    print("Muito Bom!")
# Verifica se a avaliação é igual a 3.
elif avaliacao == 3:
    # Se for igual a 3, exibe a mensagem "Bom!"
    print("Bom!")
# Verifica se a avaliação é igual a 2.
elif avaliacao == 2:
    # Se for igual a 2, exibe a mensagem "Regular."
    print("Regular.")
# Verifica se a avaliação é igual a 1.
elif avaliacao == 1:
    # Se for igual a 1, exibe a mensagem "Ruim."
    print("Ruim.")
# Se a avaliação não estiver entre 1 e 5, exibe uma mensagem de erro.
else:
    # Exibe uma mensagem indicando que a avaliação inserida é inválida.
    print("Avaliação inválida. Insira um número entre 1 e 5.")
