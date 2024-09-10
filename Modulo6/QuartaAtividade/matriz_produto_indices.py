# Solicita ao usuário que insira o valor de n
n = int(input("Digite o valor de n: "))

# Cria uma lista vazia que irá armazenar as linhas da matriz
matriz = []

# Loop para preencher as linhas da matriz
for i in range(n):
    # Cria uma nova linha (lista) para armazenar os valores
    linha = []
    # Loop para preencher os valores de cada linha
    for j in range(n):
        # Adiciona o produto dos índices i e j na lista 'linha'
        linha.append(i * j)
    # Adiciona a linha completa à matriz
    matriz.append(linha)

# Exibe a matriz na tela, linha por linha
for linha in matriz:
    print(linha)
