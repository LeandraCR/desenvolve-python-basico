# Passo 1: Solicitar ao usuário que insira pelo menos 4 números inteiros separados por espaços
numeros = input("Digite pelo menos 4 números inteiros, separados por espaço: ")

# Passo 2: Transformar a entrada do usuário (string) em uma lista de inteiros
# O método split() separa os números onde há espaços e o for converte cada número para inteiro
lista = [int(x) for x in numeros.split()]

# Passo 3: Verificar se a lista tem pelo menos 4 elementos
if len(lista) < 4:
    # Se houver menos de 4 elementos, mostrar uma mensagem de erro
    print("A lista precisa ter pelo menos 4 números.")
else:
    # Se a lista tiver 4 ou mais elementos, seguir com as impressões solicitadas

    # Passo 4: Imprimir a lista original completa
    print("Lista original:", lista)

    # Passo 5: Imprimir os 3 primeiros elementos da lista
    # Usamos lista[:3] para pegar os três primeiros elementos
    print("Os 3 primeiros elementos:", lista[:3])

    # Passo 6: Imprimir os 2 últimos elementos da lista
    # Usamos lista[-2:] para pegar os dois últimos elementos
    print("Os 2 últimos elementos:", lista[-2:])

    # Passo 7: Imprimir a lista invertida
    # Usamos lista[::-1] para inverter a lista (do último para o primeiro)
    print("Lista invertida:", lista[::-1])

    # Passo 8: Imprimir os elementos de índice par
    # Usamos lista[0::2] para pegar os elementos nos índices 0, 2, 4, etc.
    print("Elementos de índice par (0, 2, 4...):", lista[0::2])

    # Passo 9: Imprimir os elementos de índice ímpar
    # Usamos lista[1::2] para pegar os elementos nos índices 1, 3, 5, etc.
    print("Elementos de índice ímpar (1, 3, 5...):", lista[1::2])
