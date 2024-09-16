def resultado_votacao(votos):
    # Dicionário que irá armazenar o total de votos para cada candidato
    total_por_candidato = {}
    
    # Itera sobre cada dicionário de votos, que representa uma sessão eleitoral
    for sessao in votos:
        # Itera sobre os candidatos e seus respectivos votos em cada sessão
        for candidato, votos in sessao.items():
            # Se o candidato já está no dicionário, soma seus votos
            if candidato in total_por_candidato:
                total_por_candidato[candidato] += votos
            # Se o candidato não está no dicionário, adiciona com seus votos iniciais
            else:
                total_por_candidato[candidato] = votos
    
    # Calcula o total de votos somando os votos de todos os candidatos
    total_votos = sum(total_por_candidato.values())
    
    # Dicionário que irá armazenar o resultado final com total e percentual
    resultado = {}
    
    # Itera sobre o total de votos de cada candidato
    for candidato, total in total_por_candidato.items():
        # Calcula o percentual de votos de cada candidato com base no total geral
        percentual = (total / total_votos) * 100
        # Armazena o total de votos e o percentual (arredondado para duas casas decimais) no dicionário de resultado
        resultado[candidato] = (total, round(percentual, 2))
    
    # Retorna o dicionário com o resultado final
    return resultado

# Exemplo de uso:
votos = [
    {'candidato_A': 120, 'candidato_B': 85, 'candidato_C': 90},
    {'candidato_A': 110, 'candidato_B': 95, 'candidato_C': 80},
    {'candidato_A': 130, 'candidato_B': 78, 'candidato_C': 105},
]

# Chama a função para calcular o resultado da votação
resultado = resultado_votacao(votos)

# Exibe o resultado no formato: {'candidato_A': (total, percentual), ...}
print(resultado)  # Saída esperada: {'candidato_A': (360, 40.31), 'candidato_B': (258, 28.89), 'candidato_C': (275, 30.79)}
