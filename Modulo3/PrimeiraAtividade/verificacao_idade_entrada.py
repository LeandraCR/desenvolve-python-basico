# Solicita a idade de Juliana ao usuário e converte a entrada para inteiro
idade_juliana = int(input("Digite a idade de Juliana: "))

# Solicita a idade de Cris ao usuário e converte a entrada para inteiro
idade_cris = int(input("Digite a idade de Cris: "))

# Verifica se tanto Juliana quanto Cris têm mais de 17 anos
pode_entrar = idade_juliana > 17 and idade_cris > 17

# Exibe o resultado da verificação, True se ambas as idades forem maiores que 17, senão False
print(pode_entrar)
