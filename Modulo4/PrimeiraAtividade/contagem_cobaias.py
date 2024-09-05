# Solicita ao usuário o número de experimentos a serem contabilizados
N = int(input("Digite o número de experimentos: "))
contagem_sapos = 0  # Inicializa a contagem de sapos
contagem_ratos = 0  # Inicializa a contagem de ratos
contagem_coelhos = 0  # Inicializa a contagem de coelhos
i = 0  # Contador para o loop

# Processa cada experimento um a um
while i < N:
    # Recebe a quantidade e o tipo de cobaia do usuário separadamente
    quantidade = int(input("Digite a quantidade de cobaias: "))
    tipo = input("Digite o tipo de cobaia (C para coelhos, R para ratos, S para sapos): ")

    # Atualiza a contagem conforme o tipo de cobaia
    if tipo == 'S':
        contagem_sapos += quantidade
    elif tipo == 'R':
        contagem_ratos += quantidade
    elif tipo == 'C':
        contagem_coelhos += quantidade
    
    i += 1  # Incrementa o contador do loop

# Calcula o total de cobaias
total_cobaias = contagem_sapos + contagem_ratos + contagem_coelhos

# Calcula o percentual de cada tipo de cobaia sobre o total
percentual_sapos = (contagem_sapos / total_cobaias) * 100 if total_cobaias > 0 else 0
percentual_ratos = (contagem_ratos / total_cobaias) * 100 if total_cobaias > 0 else 0
percentual_coelhos = (contagem_coelhos / total_cobaias) * 100 if total_cobaias > 0 else 0

# Imprime os resultados no console
print("Total de cobaias:", total_cobaias)
print("Total de sapos:", contagem_sapos, f"({percentual_sapos:.2f}%)")
print("Total de ratos:", contagem_ratos, f"({percentual_ratos:.2f}%)")
print("Total de coelhos:", contagem_coelhos, f"({percentual_coelhos:.2f}%)")
