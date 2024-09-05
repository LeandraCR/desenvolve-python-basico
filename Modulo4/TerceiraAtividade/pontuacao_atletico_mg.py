# Solicita ao usuário o número total de jogos do Atlético MG no campeonato
numero_de_jogos = int(input("Digite o número de jogos do Atlético MG no campeonato: "))

# Inicializa as variáveis para contar vitórias, empates e derrotas
vitorias = 0
empates = 0
derrotas = 0

# Inicializa a variável que armazenará a pontuação total do time
pontuacao_total = 0

# Loop que percorre cada jogo do campeonato
for i in range(numero_de_jogos):
    # Solicita a quantidade de gols marcados pelo Atlético MG
    gols_atletico = int(input(f"Digite a quantidade de gols do Atlético MG no jogo {i+1}: "))
    # Solicita a quantidade de gols marcados pelo time adversário
    gols_oponente = int(input(f"Digite a quantidade de gols do time oponente no jogo {i+1}: "))
    
    # Condicional que compara os gols e atualiza contadores e pontuação
    if gols_atletico > gols_oponente:
        vitorias += 1
        pontuacao_total += 3
    elif gols_atletico == gols_oponente:
        empates += 1
        pontuacao_total += 1
    else:
        derrotas += 1

# Após o término do loop, imprime a pontuação total e o detalhamento de resultados
print(f"Vitórias: {vitorias}")
print(f"Empates: {empates}")
print(f"Derrotas: {derrotas}")
print(f"Pontuação: {pontuacao_total}")
