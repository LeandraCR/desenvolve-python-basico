# Definindo a função soma_quadrados, que recebe dois números como parâmetros
# e retorna a soma de seus quadrados
def soma_quadrados(num1, num2):
    # Calcula o quadrado de cada número e retorna a soma deles
    return num1**2 + num2**2

# Programa principal
# Solicita ao usuário que insira o primeiro número
n1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário que insira o segundo número
n2 = float(input("Digite o segundo número: "))

# Chama a função soma_quadrados passando os dois números digitados
resultado = soma_quadrados(n1, n2)

# Exibe o resultado da soma dos quadrados dos números
print(f"A soma dos quadrados de {n1} e {n2} é: {resultado}")
