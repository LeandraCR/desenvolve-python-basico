import string  # Importa o módulo 'string', que contém uma série de constantes relacionadas a caracteres

def checa_panagrama(frase):
    # Cria um conjunto com todas as letras do alfabeto em minúsculas
    alfabeto = set(string.ascii_lowercase)
    
    # Converte a frase para letras minúsculas e cria um conjunto das letras presentes na frase
    letras_frase = set(frase.lower())
    
    # Verifica se todas as letras do alfabeto estão presentes na frase
    return alfabeto.issubset(letras_frase)

# Testando a função com dois exemplos

# Exemplo 1: Frase conhecida por ser um panagrama
frase1 = "The quick brown fox jumps over the lazy dog"
# Exemplo 2: Frase que não contém todas as letras do alfabeto
frase2 = "Python é uma linguagem de programação"

# Verifica se as frases são panagramas e imprime o resultado
print(checa_panagrama(frase1))  # Saída: True (É um panagrama)
print(checa_panagrama(frase2))  # Saída: False (Não é um panagrama)
