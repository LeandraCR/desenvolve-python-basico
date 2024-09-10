from collections import Counter  # Importa a classe Counter, que conta a frequência de elementos em uma sequência

# Função que verifica se duas palavras são anagramas
def sao_anagramas(palavra1, palavra2):
    # Compara as frequências de cada caractere nas duas palavras (ignora maiúsculas/minúsculas)
    return Counter(palavra1.lower()) == Counter(palavra2.lower())

# Função para encontrar todos os anagramas da palavra objetivo em uma frase
def encontrar_anagramas(frase, palavra_objetivo):
    # Divide a frase em uma lista de palavras
    palavras = frase.split()
    
    # Lista de palavras que são anagramas da palavra objetivo
    anagramas = [palavra for palavra in palavras if sao_anagramas(palavra, palavra_objetivo)]
    
    # Retorna a lista de anagramas encontrados
    return anagramas

# Entrada da frase pelo usuário
frase = input("Digite uma frase: ")

# Entrada da palavra objetivo pelo usuário
palavra_objetivo = input("Digite a palavra objetivo: ")

# Chama a função encontrar_anagramas e armazena o resultado na variável 'anagramas'
anagramas = encontrar_anagramas(frase, palavra_objetivo)

# Exibe os anagramas encontrados
print(f"Anagramas: {anagramas}")
