# Solicita uma frase do usuário
frase = input("Digite uma frase: ")

# Variáveis para armazenar as vogais e os índices
vogais = "aeiou"  # Definindo quais letras serão consideradas como vogais
contador_vogais = 0  # Inicializa o contador de vogais como zero
indices_vogais = []  # Lista vazia para armazenar os índices das vogais encontradas

# Percorre cada caractere da frase
for indice, letra in enumerate(frase):  # Usando enumerate para obter tanto o índice quanto a letra
    if letra.lower() in vogais:  # Verifica se a letra é uma vogal (independente de maiúscula ou minúscula)
        contador_vogais += 1  # Incrementa o contador de vogais
        indices_vogais.append(indice)  # Adiciona o índice da vogal encontrada à lista

# Exibe a quantidade de vogais e os índices onde elas aparecem
print(f"{contador_vogais} vogais")  # Exibe a quantidade total de vogais encontradas
print(f"Índices {indices_vogais}")  # Exibe a lista de índices onde as vogais aparecem na frase
