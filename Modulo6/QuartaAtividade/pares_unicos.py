# Função para encontrar pares únicos cuja soma seja igual a um valor determinado
def pares_unicos(numeros, soma_objetivo):
    # Lista para armazenar os pares que satisfazem a condição
    pares = []
    
    # Loop para percorrer todos os números da lista
    for i in range(len(numeros)):
        # Loop interno para comparar cada número com os números seguintes
        for j in range(i + 1, len(numeros)):
            # Verifica se a soma dos dois números é igual à soma objetivo
            if numeros[i] + numeros[j] == soma_objetivo:
                # Adiciona o par (numeros[i], numeros[j]) à lista de pares
                pares.append((numeros[i], numeros[j]))
    
    # Retorna a lista de pares que satisfazem a condição
    return pares

# Exemplo de uso:
# Lista de números para testar
nums = [3, 4, 5, 6, 7]
# Valor da soma objetivo
soma = 10
# Chama a função e armazena o resultado
resultado = pares_unicos(nums, soma)
# Exibe o resultado (pares cuja soma é igual à soma objetivo)
print(resultado)  # Saída esperada: [(3, 7), (4, 6)]
