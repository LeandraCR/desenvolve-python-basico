import csv  # Importa a biblioteca CSV

# Lista para armazenar as músicas extraídas
musicas = []

# Abre o arquivo CSV e define a codificação
with open('musicas.csv', encoding='latin1') as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv)  # Cria um leitor CSV que trabalha com dicionários
    # Itera por cada linha do arquivo CSV
    for linha in leitor_csv:
        # Extrai as informações das colunas desejadas
        track_name = linha['track_name']
        artist_name = linha['artist(s)_name']
        released_year = linha['released_year']
        streams = linha['streams']
        
        # Armazena as informações relevantes em uma lista
        musicas.append([track_name, artist_name, released_year, streams])

# Exibe as 10 primeiras músicas extraídas
for musica in musicas[:10]:
    print(musica)  # Imprime as informações das músicas
