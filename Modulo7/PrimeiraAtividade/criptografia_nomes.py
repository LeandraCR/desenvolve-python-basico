import random  # Importa o módulo random para gerar números aleatórios

def encrypt(nomes):
    # Gera a chave de criptografia aleatória entre 1 e 10
    chave = random.randint(1, 10)
    
    # Função para criptografar uma string
    def criptografar_nome(nome):
        criptografado = ""  # String vazia para armazenar o nome criptografado
        for char in nome:
            # Converte o caractere para sua posição Unicode
            codigo_unicode = ord(char)
            # Aplica a chave de criptografia, garantindo que o valor permaneça no intervalo de caracteres visíveis (33 a 126)
            novo_unicode = ((codigo_unicode - 33 + chave) % (126 - 33 + 1)) + 33
            # Converte de volta para o caractere e adiciona ao nome criptografado
            criptografado += chr(novo_unicode)
        return criptografado

    # Aplica a criptografia para cada nome na lista
    nomes_cript = [criptografar_nome(nome) for nome in nomes]
    
    # Retorna a lista de nomes criptografados e a chave usada na criptografia
    return nomes_cript, chave

# Exemplo de uso
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]  # Lista de nomes que serão criptografados
nomes_cript, chave_aleatoria = encrypt(nomes)  # Chama a função encrypt e armazena os resultados

# Exibe a chave de criptografia gerada e os nomes criptografados
print(f"Chave aleatória: {chave_aleatoria}")
print(f"Nomes criptografados: {nomes_cript}")
