# Receber duas listas de números do usuário, separadas por espaços
# A função split() vai separar os números onde há espaços e criar uma lista
lista1 = input("Digite os números da primeira lista, separados por espaço: ").split()
lista2 = input("Digite os números da segunda lista, separados por espaço: ").split()

# Converter os valores da lista de strings para inteiros
# A função int() transforma cada valor em número, e a lista de compreensão faz isso para cada número
lista1 = [int(num) for num in lista1]
lista2 = [int(num) for num in lista2]

# Criar uma nova lista onde vamos guardar os números intercalados
lista_intercalada = []

# Descobrir qual das listas tem o menor tamanho
# A função min() retorna o menor valor entre len(lista1) e len(lista2), que são os tamanhos das listas
tamanho_menor_lista = min(len(lista1), len(lista2))

# Para cada índice de 0 até o tamanho da menor lista, adicionar alternadamente os elementos das duas listas
for i in range(tamanho_menor_lista):
    # Adiciona o i-ésimo elemento da primeira lista
    lista_intercalada.append(lista1[i])
    # Adiciona o i-ésimo elemento da segunda lista
    lista_intercalada.append(lista2[i])

# Se a primeira lista for maior, adiciona os elementos que sobraram dela
if len(lista1) > len(lista2):
    lista_intercalada.extend(lista1[tamanho_menor_lista:])
# Se a segunda lista for maior, adiciona os elementos que sobraram dela
else:
    lista_intercalada.extend(lista2[tamanho_menor_lista:])

# Exibe a lista intercalada final
print("Lista intercalada:", lista_intercalada)
