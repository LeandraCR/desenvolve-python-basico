# Definindo as listas A e B
# A lista A contém todos os elementos, enquanto a lista B contém todos os elementos menos um
A = [1, 4, 5, 7, 9]
B = [4, 5, 7, 9]

# Percorre todos os elementos da lista A
for elem in A:
    # Verifica se o elemento atual (elem) de A não está presente na lista B
    if elem not in B:
        # Caso o elemento não esteja presente em B, imprime qual elemento está faltando
        print(f"O elemento {elem} está faltando na segunda lista")
        # Interrompe o loop após encontrar o elemento faltante
        break
