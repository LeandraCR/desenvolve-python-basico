import random  # Importa a biblioteca random, que permite gerar números aleatórios

# Passo 1: Gerar um número aleatório entre 5 e 20 e armazenar na variável 'num_elementos'
num_elementos = random.randint(5, 20)

# Passo 2: Criar uma lista vazia chamada 'elementos' para armazenar os números
elementos = []

# Usar um loop para gerar 'num_elementos' números aleatórios entre 1 e 10
for i in range(num_elementos):  
    numero = random.randint(1, 10)  # Gera um número aleatório entre 1 e 10
    elementos.append(numero)  # Adiciona o número gerado à lista 'elementos'

# Passo 3: Calcular a soma dos elementos da lista usando a função 'sum()'
soma_elementos = sum(elementos)

# Passo 4: Calcular a média dividindo a soma pelo número de elementos
media_elementos = soma_elementos / num_elementos

# Passo 5: Imprimir a lista, a soma dos valores e a média dos valores
print("A lista de elementos é:", elementos)  # Mostra a lista
print("A soma dos valores da lista é:", soma_elementos)  # Mostra a soma dos elementos
print("A média dos valores da lista é:", round(media_elementos, 2))  # Mostra a média, arredondada para 2 casas decimais
