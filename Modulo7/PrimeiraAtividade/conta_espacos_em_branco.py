# Solicita que o usuário insira uma frase
frase = input("Digite a frase: ")

# Conta quantas vezes o caractere de espaço em branco (" ") aparece na frase
espacos_em_branco = frase.count(" ")

# Exibe o resultado na tela, informando quantos espaços em branco foram encontrados
print(f"Espaços em branco: {espacos_em_branco}")
