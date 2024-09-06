# Função que calcula o fatorial de um número n
def fatorial(n):
    # Inicializa a variável fat com 1, que será usada para calcular o fatorial
    fat = 1
    # Loop que multiplica fat pelos números de 1 até n
    for i in range(1, n + 1):
        fat *= i  # fat = fat * i
    # Retorna o resultado final do fatorial
    return fat

# Programa principal
# Solicita ao usuário que insira um número inteiro
n = int(input("Digite um número inteiro para calcular o fatorial: "))

# Chama a função fatorial com o valor fornecido pelo usuário
resultado = fatorial(n)

# Exibe o resultado do fatorial
print(f"O fatorial de {n} é {resultado}")
