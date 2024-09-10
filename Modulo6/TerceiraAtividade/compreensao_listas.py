# Gera uma lista com os números pares entre 20 e 50
pares = [x for x in range(20, 51) if x % 2 == 0]
print(pares)  # Exibe a lista de números pares

# Gera uma lista com os quadrados dos números da lista fornecida
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Lista de números fornecida
quadrados = [x**2 for x in lista]  # Calcula o quadrado de cada número da lista
print(quadrados)  # Exibe a lista de quadrados

# Gera uma lista com números entre 1 e 100 que são divisíveis por 7
div7 = [x for x in range(1, 101) if x % 7 == 0]  
print(div7)  # Exibe a lista de números divisíveis por 7

# Gera uma lista que indica "par" ou "impar" para valores no intervalo de 0 a 29, com passo de 3
par_impar = ['par' if x % 2 == 0 else 'impar' for x in range(0, 30, 3)]  
print(par_impar)  # Exibe a lista indicando paridade ("par" ou "impar")
