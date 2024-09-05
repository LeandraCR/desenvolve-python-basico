# Solicita a idade do usuário e converte para inteiro
idade = int(input("Digite sua idade: "))

# Solicita ao usuário se ele já jogou pelo menos 3 jogos de tabuleiro
# A resposta é convertida para um valor booleano (True/False)
jogou_3_jogos = input("Você já jogou pelo menos 3 jogos de tabuleiro? (True/False): ")
jogou_3_jogos = jogou_3_jogos == "True"  # Converte a entrada para booleano

# Solicita o número de vezes que o usuário venceu um jogo de tabuleiro e converte para inteiro
vitorias = int(input("Quantas vezes você venceu um jogo de tabuleiro? "))

# Define se o usuário pode ingressar no clube
# Regras: idade entre 16 e 18 anos, já jogou pelo menos 3 jogos de tabuleiro e venceu pelo menos 1 vez
pode_ingressar = idade >= 16 and idade <= 18 and jogou_3_jogos and vitorias >= 1

# Exibe se o usuário pode ingressar no clube (True ou False)
print(pode_ingressar)
