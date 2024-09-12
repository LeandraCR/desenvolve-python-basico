import csv  # Importa a biblioteca CSV

# Lista para armazenar as músicas
musicas = []

# Abre o arquivo CSV com codificação correta
with open('spotify-2023.csv', encoding='latin1') as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv)  # Lê o arquivo como um dicionário
    # Itera por cada linha do arquivo
    for linha in leitor_csv:
        track_name = linha['track_name']  # Nome da música
        artist_name = linha['artist(s)_name']  # Nome do(s) artista(s)
        released_year = int(linha['released_year'])  # Ano de lançamento
        streams = linha['streams']  # Número de streams
        
        # Filtra músicas lançadas entre 2010 e 2022
        if 2010 <= released_year <= 2022:
            # Armazena as músicas que atendem ao critério
            musicas.append([track_name, artist_name, released_year, streams])

# Exibe as 10 primeiras músicas filtradas
for musica in musicas[:10]:
    print(musica)  # Imprime as informações das músicas
