# Solicita ao usuário que insira a pontuação do jogador e a armazena na variável 'pontuacao'
pontuacao = int(input("Digite a pontuação do jogador: "))

# Avalia a pontuação e atribui a classificação correspondente à variável 'classificacao'
if pontuacao >= 90:
    classificacao = "Excelente"  # Pontuação igual ou superior a 90 é classificada como "Excelente"
elif pontuacao >= 80:
    classificacao = "Bom"        # Pontuação entre 80 e 89 é classificada como "Bom"
elif pontuacao >= 70:
    classificacao = "Regular"    # Pontuação entre 70 e 79 é classificada como "Regular"
else:
    classificacao = "Insatisfatório"  # Pontuação abaixo de 70 é classificada como "Insatisfatório"

# Exibe a classificação do jogador
print(f"A classificação do jogador é: {classificacao}")
