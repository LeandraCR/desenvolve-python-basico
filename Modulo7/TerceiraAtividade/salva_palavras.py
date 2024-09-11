# Define o caminho do arquivo salvo anteriormente
caminho_arquivo = 'frase.txt'

# Abre o arquivo 'frase.txt' em modo de leitura ('r') e lê o conteúdo
arquivo = open(caminho_arquivo, 'r')
frase = arquivo.read()  # Armazena o conteúdo do arquivo na variável 'frase'
arquivo.close()  # Fecha o arquivo após a leitura

# Importa a biblioteca 're' para trabalhar com expressões regulares
import re

# Usa uma expressão regular para extrair apenas palavras (alfabéticas) da frase
palavras = re.findall(r'\b[A-Za-zÀ-ÿ]+\b', frase)

# Abre o arquivo 'palavras.txt' em modo de escrita e salva as palavras extraídas
arquivo_palavras = open('palavras.txt', 'w')
for palavra in palavras:
    arquivo_palavras.write(palavra + '\n')  # Escreve cada palavra em uma nova linha
arquivo_palavras.close()  # Fecha o arquivo após a escrita

# Abre o arquivo 'palavras.txt' em modo de leitura e exibe seu conteúdo
arquivo_palavras = open('palavras.txt', 'r')
conteudo_palavras = arquivo_palavras.read()  # Armazena o conteúdo do arquivo
arquivo_palavras.close()  # Fecha o arquivo após a leitura
print(conteudo_palavras)  # Imprime o conteúdo de 'palavras.txt' no console
