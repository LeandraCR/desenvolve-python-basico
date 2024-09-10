import random  # Importa o módulo random para gerar números aleatórios

# Passo 1: Gerar a lista com 20 números aleatórios
lista = []  # Cria uma lista vazia para armazenar os números
for i in range(20):  # Executa um loop 20 vezes (uma vez para cada número que queremos gerar)
    numero_aleatorio = random.randint(-100, 100)  # Gera um número aleatório entre -100 e 100
    lista.append(numero_aleatorio)  # Adiciona o número gerado à lista

# Passo 2: Mostrar a lista original
print("Lista original:", lista)  # Exibe a lista de números gerados aleatoriamente

# Passo 3: Mostrar a lista ordenada, sem alterar a original
lista_ordenada = sorted(lista)  # Cria uma nova lista com os números em ordem crescente
print("Lista ordenada:", lista_ordenada)  # Exibe a lista ordenada, sem modificar a original

# Passo 4: Encontrar o índice do maior valor
maior_valor = max(lista)  # Acha o maior valor da lista
indice_maior = lista.index(maior_valor)  # Acha o índice (posição) do maior valor na lista original
print("O maior valor é", maior_valor, "e seu índice é", indice_maior)  # Mostra o maior valor e sua posição

# Passo 5: Encontrar o índice do menor valor
menor_valor = min(lista)  # Acha o menor valor da lista
indice_menor = lista.index(menor_valor)  # Acha o índice (posição) do menor valor na lista original
print("O menor valor é", menor_valor, "e seu índice é", indice_menor)  # Mostra o menor valor e sua posição
