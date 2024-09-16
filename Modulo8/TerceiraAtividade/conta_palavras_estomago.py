# Abrir o arquivo e ler o conteúdo usando a codificação 'latin-1'
# A codificação 'latin-1' é usada para lidar com possíveis caracteres especiais que não são suportados pelo 'utf-8'
with open("estomago.txt", "r", encoding="latin-1") as file:
    # Lê todo o conteúdo do arquivo e armazena na variável 'texto'
    texto = file.read()

# Importa a biblioteca string para remover pontuações
import string

# Remove pontuações do texto e converte todas as letras para minúsculas
# Isso ajuda a contar palavras como "Casa" e "casa" como a mesma palavra
# O método 'translate' é usado para substituir os caracteres de pontuação por vazio
texto = texto.translate(str.maketrans("", "", string.punctuation)).lower()

# Divide o texto em uma lista de palavras
# O método split() separa o texto em palavras com base nos espaços
palavras = texto.split()

# Importa defaultdict da biblioteca collections para criar um dicionário
# Ele inicializa a contagem de palavras com valor 0 por padrão
from collections import defaultdict
contador_palavras = defaultdict(int)

# Loop através da lista de palavras e incrementa o contador para cada palavra
for palavra in palavras:
    contador_palavras[palavra] += 1

# Ordena o dicionário por frequência de palavras em ordem decrescente
# A função sorted ordena o dicionário pelo valor, que é o número de ocorrências
contador_ordenado = dict(sorted(contador_palavras.items(), key=lambda item: item[1], reverse=True))

# Exibe o dicionário ordenado, palavra por palavra, com sua frequência
# Aqui cada palavra e a frequência são impressas
for palavra, frequencia in contador_ordenado.items():
    print(f"{palavra}: {frequencia}")
