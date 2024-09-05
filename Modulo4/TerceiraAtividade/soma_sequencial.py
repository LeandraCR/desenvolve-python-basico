# Solicita ao usuário um número inteiro positivo
n = int(input("Digite um número: "))

# Inicializa a variável soma para armazenar a soma dos números
soma = 0

# Loop para calcular a soma dos números de 1 até n
for i in range(1, n + 1):
    soma += i  # Adiciona o valor atual de i à variável soma

# Exibe o resultado da soma
print(f"A soma dos números de 1 a {n} é {soma}")
