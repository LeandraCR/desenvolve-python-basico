# Importa a biblioteca 'os' para trabalhar com caminhos de arquivos
import os

# Solicita uma frase do usuário e armazena na variável 'frase'
frase = input("Digite uma frase: ")

# Define o caminho do arquivo onde a frase será salva
caminho_arquivo = 'frase.txt'

# Abre o arquivo 'frase.txt' em modo de escrita ('w') e salva a frase
arquivo = open(caminho_arquivo, 'w')
arquivo.write(frase)  # Escreve o conteúdo da variável 'frase' no arquivo
arquivo.close()  # Fecha o arquivo após a escrita

# Exibe o caminho completo do arquivo 'frase.txt' salvo no sistema
caminho_completo = os.path.abspath(caminho_arquivo)
print(f"Frase salva em {caminho_completo}")

