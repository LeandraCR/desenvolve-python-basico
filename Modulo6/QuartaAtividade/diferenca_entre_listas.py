# Listas fornecidas para o exemplo
lista1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
lista2 = [1, 1, 2, 4, 5, 6]

# Cria uma cópia de lista1 para preservar a lista original
diferenca = lista1.copy()

# Para cada elemento em lista2, verificamos se ele existe em 'diferenca'
# Se existir, removemos esse elemento da lista 'diferenca'
for elemento in lista2:
    if elemento in diferenca:
        diferenca.remove(elemento)

# Exibe o resultado, ou seja, a diferença entre as listas
print("Diferença entre as listas:", diferenca)
