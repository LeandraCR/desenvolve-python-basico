import csv  # Importa a biblioteca para trabalhar com arquivos CSV

# Abrir o arquivo CSV com a codificação correta
with open('spotify-2023.csv', encoding='latin1') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)  # Cria um leitor CSV
    # Lê e imprime as cinco primeiras linhas do arquivo
    for i in range(5):
        print(next(leitor_csv))  # Imprime cada linha do arquivo CSV
