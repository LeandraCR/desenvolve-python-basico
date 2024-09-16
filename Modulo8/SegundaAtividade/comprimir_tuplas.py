from collections import defaultdict  # Importa defaultdict da biblioteca collections

# Função para comprimir a lista de tuplas, somando os números associados a palavras idênticas
def comprimir_tuplas(tuplas):
    # Criar um dicionário que vai armazenar a soma dos números para cada palavra
    # defaultdict(int) inicializa o valor como 0 automaticamente
    resultado = defaultdict(int)
    
    # Iterar sobre a lista de tuplas
    for palavra, numero in tuplas:
        # Adiciona o número ao valor atual da palavra no dicionário
        resultado[palavra] += numero
    
    # Converte o dicionário de volta para uma lista de tuplas
    return list(resultado.items())

# Exemplo de uso da função
tuplas_originais = [('maçã', 3), ('banana', 2), ('maçã', 5), ('laranja', 1), ('banana', 3)]

# Chama a função com a lista de tuplas originais e armazena o resultado
resultado = comprimir_tuplas(tuplas_originais)

# Imprime o resultado, que é uma lista de tuplas onde as palavras foram agrupadas e os números somados
print(resultado)
