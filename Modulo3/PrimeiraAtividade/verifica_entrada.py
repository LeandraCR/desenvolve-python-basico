# Solicita ao usuário que insira a idade de Juliana e converte o valor inserido em um número inteiro
idade_juliana = int(input("Digite a idade de Juliana: "))

# Solicita ao usuário que insira a idade de Cris e converte o valor inserido em um número inteiro
idade_cris = int(input("Digite a idade de Cris: "))

# Verifica se Juliana ou Cris têm mais de 17 anos. Se uma delas for maior de idade, o valor será True
pode_entrar = idade_juliana > 17 or idade_cris > 17

# Exibe se uma delas pode entrar (True) ou não (False)
print(pode_entrar)
