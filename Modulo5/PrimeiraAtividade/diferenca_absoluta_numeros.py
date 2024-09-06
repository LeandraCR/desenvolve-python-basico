# Solicita ao usuário que insira o primeiro número decimal e o converte para o tipo float
num1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário que insira o segundo número decimal e o converte para o tipo float
num2 = float(input("Digite o segundo número: "))

# Calcula a diferença absoluta entre os dois números usando a função abs() 
# e arredonda o resultado para duas casas decimais usando a função round()
diferenca = round(abs(num1 - num2), 2)

# Exibe o resultado formatado para o usuário
print(f"A diferença absoluta entre os números é: {diferenca}")
