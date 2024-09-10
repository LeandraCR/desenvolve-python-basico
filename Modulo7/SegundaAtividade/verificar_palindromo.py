import string  # Importa o módulo string, que contém caracteres de pontuação

# Função que verifica se uma frase é um palíndromo
def eh_palindromo(frase):
    # Remove os espaços e pontuações, e converte tudo para minúsculas
    frase_limpa = ''.join(ch.lower() for ch in frase if ch not in string.punctuation and not ch.isspace())
    
    # Compara a frase limpa com sua versão invertida
    return frase_limpa == frase_limpa[::-1]

# Loop que mantém o programa rodando até o usuário digitar "fim"
while True:
    # Pede ao usuário para digitar uma frase
    frase = input("Digite uma frase (digite 'fim' para encerrar): ")
    
    # Verifica se o usuário digitou "fim" para encerrar o programa
    if frase.lower() == 'fim':
        break  # Encerra o loop
    
    # Verifica se a frase é um palíndromo usando a função eh_palindromo
    if eh_palindromo(frase):
        print(f'"{frase}" é palíndromo')  # Se for palíndromo, imprime essa mensagem
    else:
        print(f'"{frase}" não é palíndromo')  # Se não for, imprime essa mensagem
