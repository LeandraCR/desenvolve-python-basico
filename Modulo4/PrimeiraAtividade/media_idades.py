# Solicita ao usuário o número de respondentes e converte a entrada para inteiro
N = int(input("Digite o número de respondentes: "))

# Inicializa a soma das idades
soma_idades = 0

# Inicializa o contador para o loop
contador = 0

# Loop que se repete N vezes, uma para cada respondente
while contador < N:
    # Solicita a idade do respondente atual e converte a entrada para inteiro
    idade = int(input(f"Digite a idade do respondente {contador + 1}: "))
    # Adiciona a idade do respondente à soma total
    soma_idades += idade
    # Incrementa o contador para avançar para o próximo respondente
    contador += 1

# Calcula a média das idades dividindo a soma total pelo número de respondentes
media_idades = soma_idades / N

# Exibe a média das idades, formatada com duas casas decimais
print(f"A média das idades é: {media_idades:.2f}")
