# Nome do arquivo sugerido: caracteres_unicos_string.py

frase = "O rato roeu a roupa do Robson"  # Definindo a frase

# Convertendo a frase para minúsculas para evitar diferenciação entre maiúsculas e minúsculas
# e removendo os espaços em branco.
frase_formatada = frase.lower().replace(" ", "")

# Criando um conjunto (set) para obter os caracteres únicos da frase formatada.
caracteres_unicos = set(frase_formatada)

# Ordenando os caracteres únicos em ordem alfabética.
caracteres_ordenados = sorted(caracteres_unicos)

# Exibindo os caracteres únicos, ordenados.
print(caracteres_ordenados)
