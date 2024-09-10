# Solicita ao usuário a temperatura em graus Fahrenheit e armazena na variável F
F = int(input("Digite a temperatura em graus Fahrenheit: "))

# Converte a temperatura de Fahrenheit para Celsius usando a fórmula (F - 32) * (5/9)
C = int((F - 32) * (5/9))

# Exibe o resultado da conversão para o usuário, mostrando a temperatura em Celsius
print(f"{F} graus Fahrenheit são {C} graus Celsius.")
