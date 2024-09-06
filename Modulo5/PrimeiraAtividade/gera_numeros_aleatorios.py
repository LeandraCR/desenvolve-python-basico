import random  # Importa a biblioteca random, usada para gerar números aleatórios
import math    # Importa a biblioteca math, usada para funções matemáticas, como a raiz quadrada

# Solicita ao usuário a quantidade de números aleatórios que deseja gerar (valor de n)
n = int(input("Digite a quantidade de números aleatórios que deseja gerar: "))

# Gera uma lista com n valores inteiros aleatórios entre 0 e 100
valores = [random.randint(0, 100) for _ in range(n)]

# Calcula a soma de todos os valores gerados
soma_valores = sum(valores)

# Calcula a raiz quadrada da soma dos valores
raiz_quadrada = math.sqrt(soma_valores)

# Exibe os números gerados, a soma dos valores e a raiz quadrada da soma
print(f"Os valores gerados foram: {valores}")
print(f"A soma dos valores é: {soma_valores}")
print(f"A raiz quadrada da soma é: {raiz_quadrada}")
