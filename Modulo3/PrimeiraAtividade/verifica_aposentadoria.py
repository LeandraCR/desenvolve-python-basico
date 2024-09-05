# Solicita ao usuário que insira seu gênero
genero = input("Digite seu gênero ('M' para masculino, 'F' para feminino): ")

# Solicita ao usuário que insira sua idade e converte para inteiro
idade = int(input("Digite sua idade: "))

# Solicita ao usuário que insira seu tempo de serviço e converte para inteiro
tempo_servico = int(input("Digite seu tempo de serviço (em anos): "))

# Calcula se a pessoa pode se aposentar com base nas seguintes condições:
# 1. Gênero feminino e idade igual ou maior a 60
# 2. Gênero masculino e idade igual ou maior a 65
# 3. Tempo de serviço igual ou superior a 30 anos
# 4. Idade igual ou maior a 60 e tempo de serviço igual ou superior a 25 anos
pode_aposentar = (
    (genero == "F" and idade >= 60) or   # Condição para mulheres
    (genero == "M" and idade >= 65) or   # Condição para homens
    (tempo_servico >= 30) or             # Condição pelo tempo de serviço
    (idade >= 60 and tempo_servico >= 25)  # Condição combinada de idade e tempo de serviço
)

# Exibe se a pessoa pode se aposentar (True) ou não (False)
print(pode_aposentar)
