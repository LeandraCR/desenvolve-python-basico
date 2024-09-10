# Solicita uma frase ao usuário e converte todas as letras para minúsculas
frase = input("Digite uma frase: ").lower()

# Define uma string com todas as vogais
vogais = 'aeiou'

# Compreensão de lista para gerar uma lista com as vogais da frase
# A lista só inclui as letras que estão presentes na variável 'vogais'
# sorted() é usado para ordenar as vogais em ordem alfabética
lista_vogais = sorted([letra for letra in frase if letra in vogais])

# Compreensão de lista para gerar uma lista de consoantes
# A função isalpha() garante que a letra é uma letra do alfabeto (ignora espaços e caracteres especiais)
# Só inclui letras que não estão nas vogais, ou seja, são consoantes
lista_consoantes = [letra for letra in frase if letra.isalpha() and letra not in vogais]

# Exibe a lista de vogais ordenadas alfabeticamente
print("Vogais ordenadas alfabeticamente:", lista_vogais)

# Exibe a lista de consoantes, removendo os espaços
print("Consoantes sem espaços:", lista_consoantes)
