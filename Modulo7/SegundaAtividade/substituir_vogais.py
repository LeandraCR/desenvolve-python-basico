# Solicita ao usuário que insira uma frase e armazena a entrada na variável 'frase'
frase = input("Digite uma frase: ")

# Define uma string contendo todas as vogais maiúsculas e minúsculas
vogais = "aeiouAEIOU"

# Cria uma variável vazia para armazenar a frase modificada
frase_modificada = ""

# Itera sobre cada caractere da frase original
for letra in frase:
    # Verifica se o caractere atual é uma vogal
    if letra in vogais:
        # Se for uma vogal, adiciona "*" à frase modificada
        frase_modificada += "*"
    else:
        # Se não for uma vogal, mantém o caractere original na frase modificada
        frase_modificada += letra

# Exibe a frase modificada com as vogais substituídas por "*"
print("Frase modificada:", frase_modificada)
