# Leitura dos valores de N e M a partir do input do usuário
# N é o número de linhas e M é o número de colunas do tabuleiro
N = int(input("Digite o número de linhas (N): "))
M = int(input("Digite o número de colunas (M): "))

# Primeira linha com o cabeçalho das colunas
# O 'end' evita a quebra de linha após o espaço inicial
print(' ', end=' ')  # Imprime o espaço antes dos números das colunas
for coluna in range(1, M + 1):  # Itera sobre o número de colunas
    print(coluna, end=' ')  # Imprime os números das colunas
print()  # Quebra de linha para começar a próxima linha

# Loop para imprimir as linhas do tabuleiro com o cabeçalho das linhas
for linha in range(1, N + 1):  # Itera sobre o número de linhas
    print(linha, end=' ')  # Imprime o número da linha
    for _ in range(M):  # Itera sobre o número de colunas para imprimir as células jogáveis
        print('/', end=' ')  # Imprime a barra que representa a célula jogável
    print()  # Quebra de linha após imprimir todas as células da linha
