# Inicializa a soma dos valores em 0
soma = 0

# Loop que executa 10 vezes para coletar 10 valores do usuário
for i in range(1, 11):
    # Solicita ao usuário um valor inteiro positivo e armazena na variável 'valor'
    valor = int(input(f"Digite o {i}º valor inteiro positivo: "))
    # Adiciona o valor fornecido à soma acumulada
    soma += valor

# Calcula a média dividindo a soma total pelo número de valores (10)
media = soma / 10

# Imprime a média, formatada para mostrar duas casas decimais
print(f"A média dos valores digitados é: {media:.2f}")
