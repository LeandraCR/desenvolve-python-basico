# String contendo a frase
frase = "O rato roeu a roupa da Alice"

# Conjunto de vogais que serão verificadas (incluindo maiúsculas e minúsculas)
vogais = "aeiouAEIOU"

# Loop através da string usando a função enumerate, que retorna o índice e a letra
for i, letra in enumerate(frase):
    # Verifica se a letra atual é uma vogal
    if letra in vogais:
        # Imprime a vogal encontrada e seu respectivo índice
        print(f"Vogal '{letra}' encontrada no índice {i}")
