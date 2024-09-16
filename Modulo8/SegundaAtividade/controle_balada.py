# Lista para armazenar os pares (nome, idade)
pessoas = []

# Coleta de dados de pessoas (nome e idade)
# O loop continua até que o usuário digite 'sair'
while True:
    nome = input("Digite o nome da pessoa (ou 'sair' para terminar): ")  # Solicita o nome da pessoa
    if nome.lower() == 'sair':  # Se o usuário digitar 'sair', o loop é encerrado
        break
    idade = int(input("Digite a idade: "))  # Solicita a idade da pessoa e converte para inteiro
    pessoas.append((nome, idade))  # Adiciona uma tupla (nome, idade) à lista 'pessoas'

# Separando em duas listas: menores de idade e maiores de idade
# Cria uma tupla com os nomes das pessoas que são menores de 18 anos
menores = tuple([pessoa[0] for pessoa in pessoas if pessoa[1] < 18])

# Cria uma tupla com os nomes das pessoas que têm 18 anos ou mais
maiores = tuple([pessoa[0] for pessoa in pessoas if pessoa[1] >= 18])

# Exibe a lista de menores de idade
print("Menores de idade:", menores)

# Exibe a lista de maiores de idade
print("Maiores de idade:", maiores)
