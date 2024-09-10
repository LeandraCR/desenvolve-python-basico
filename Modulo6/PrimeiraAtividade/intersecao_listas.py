import random  # Importa a biblioteca random para gerar números aleatórios

# Criando duas listas vazias para armazenar os números
lista1 = []
lista2 = []

# Preenchendo as listas com 20 números aleatórios entre 0 e 50
for i in range(20):  # Repete o loop 20 vezes
    lista1.append(random.randint(0, 50))  # Adiciona um número aleatório na lista1
    lista2.append(random.randint(0, 50))  # Adiciona um número aleatório na lista2

# Criando a lista interseccao para armazenar os números que aparecem nas duas listas
interseccao = []
for num in lista1:  # Percorre todos os números da lista1
    if num in lista2 and num not in interseccao:  # Verifica se o número está em lista2 e não está repetido
        interseccao.append(num)  # Adiciona o número à lista interseccao

# Ordenando a lista de interseção para deixar os números em ordem crescente
interseccao.sort()

# Imprimindo as duas listas e a interseção
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseção (ordenada e sem duplicados):", interseccao)

# Contando e mostrando quantas vezes cada número da interseção aparece em cada lista
print("\nQuantidade de vezes que os números da interseção aparecem em cada lista:")
for num in interseccao:  # Percorre cada número da lista interseccao
    print(f"O número {num} aparece {lista1.count(num)} vez(es) em lista1 e {lista2.count(num)} vez(es) em lista2.")
