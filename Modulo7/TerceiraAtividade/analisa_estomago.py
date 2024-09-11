# Abrir o arquivo "estomago.txt" em modo de leitura e especificar o encoding UTF-8 para evitar erros com acentuação
with open("estomago.txt", "r") as arquivo:
    linhas = arquivo.readlines()

# 1. Imprimir o texto das primeiras 25 linhas
print("Texto das primeiras 25 linhas:")

# Loop que percorre as primeiras 25 linhas ou menos, se o arquivo tiver menos de 25 linhas
for i in range(min(25, len(linhas))):
    # Usamos .strip() para remover espaços extras no início e fim das linhas
    print(linhas[i].strip())

# 2. Contar o número de linhas do arquivo
numero_linhas = len(linhas)
print("\nNúmero de linhas do arquivo:", numero_linhas)

# 3. Encontrar a linha com o maior número de caracteres
# A função max() recebe a lista de linhas e usa a função len como critério de comparação
linha_maior = max(linhas, key=len)
print("\nLinha com maior número de caracteres:", linha_maior.strip())

# 4. Contar quantas vezes "Nonato" e "Íria" aparecem no texto
# Para "Nonato", convertemos todas as linhas para minúsculas com lower() para considerar variações de maiúsculas/minúsculas
menções_nonato = sum(1 for linha in linhas if "nonato" in linha.lower())

# Para "Íria", dividimos a linha em palavras com .split() para evitar contar "iria" como parte de outras palavras
menções_iria = sum(1 for linha in linhas if "íria" in linha.lower().split())

# Exibir o número de menções aos nomes "Nonato" e "Íria"
print("\nNúmero de menções ao nome 'Nonato':", menções_nonato)
print("Número de menções ao nome 'Íria':", menções_iria)
