# Solicita ao usuário que insira um valor inteiro em reais
valor = int(input("Digite um valor inteiro em reais: "))

# Calcula a quantidade de notas de 100 e atualiza o valor restante
notas100 = valor // 100
valor = valor % 100

# Calcula a quantidade de notas de 50 e atualiza o valor restante
notas50 = valor // 50
valor = valor % 50

# Calcula a quantidade de notas de 20 e atualiza o valor restante
notas20 = valor // 20
valor = valor % 20

# Calcula a quantidade de notas de 10 e atualiza o valor restante
notas10 = valor // 10
valor = valor % 10

# Calcula a quantidade de notas de 5 e atualiza o valor restante
notas5 = valor // 5
valor = valor % 5

# Calcula a quantidade de notas de 2 e atualiza o valor restante
notas2 = valor // 2
valor = valor % 2

# Calcula a quantidade de notas de 1 (moedas ou notas de 1 real)
notas1 = valor // 1

# Exibe a quantidade de notas de cada valor
print(f"{notas100} nota(s) de R$ 100")
print(f"{notas50} nota(s) de R$ 50")
print(f"{notas20} nota(s) de R$ 20")
print(f"{notas10} nota(s) de R$ 10")
print(f"{notas5} nota(s) de R$ 5")
print(f"{notas2} nota(s) de R$ 2")
print(f"{notas1} nota(s) de R$ 1")

