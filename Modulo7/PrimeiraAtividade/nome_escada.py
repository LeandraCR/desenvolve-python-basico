# Solicita o nome do usuário e armazena na variável 'nome'
nome = input("Digite seu nome: ")

# Loop para iterar sobre o comprimento do nome
# O range começa em 1 e vai até o tamanho do nome, inclusive
for i in range(1, len(nome) + 1):
    # Imprime uma parte do nome, do índice 0 até o índice 'i'
    # A cada iteração, imprime mais uma letra do nome
    print(nome[:i])
