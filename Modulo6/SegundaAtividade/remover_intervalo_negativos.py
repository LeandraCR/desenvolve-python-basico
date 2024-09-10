import random  # Importa o módulo random para gerar números aleatórios

# Cria uma lista com 20 elementos, cada um sendo um número aleatório entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]
print("Lista original:", lista)  # Exibe a lista original gerada

# Cria uma lista com os índices de todos os números negativos da lista
negativos = [i for i, num in enumerate(lista) if num < 0]

# Se houver números negativos, continue o processo
if negativos:
    # Remove o intervalo de números negativos com base no menor e maior índice encontrado
    del lista[min(negativos):max(negativos) + 1]

# Exibe a lista após a exclusão do intervalo de números negativos
print("Lista após a exclusão:", lista)
