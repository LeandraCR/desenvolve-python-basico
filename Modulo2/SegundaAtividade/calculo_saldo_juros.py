# Inicializa o saldo com o valor de 500.0
saldo = 500.0

# Define a taxa de juros como 1.01 (ou seja, 1% ao mês)
juros = 1.01

# Aplica os juros ao saldo por três meses consecutivos
saldo *= juros  # Multiplica o saldo pela taxa de juros no 1º mês
saldo *= juros  # Multiplica o saldo pela taxa de juros no 2º mês
saldo *= juros  # Multiplica o saldo pela taxa de juros no 3º mês

# Exibe o saldo final após 3 meses
print("Após 3 meses meu novo saldo é")
print(saldo)
