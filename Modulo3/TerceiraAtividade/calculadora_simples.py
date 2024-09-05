# Solicita ao usuário o primeiro número e converte para um número decimal (float)
operando1 = float(input("Digite o primeiro operando: "))

# Solicita ao usuário o operador desejado (+, -, *, /, **)
operador = input("Digite o operador (+, -, *, /, **): ")

# Solicita ao usuário o segundo número e converte para um número decimal (float)
operando2 = float(input("Digite o segundo operando: "))

# Verifica qual operador foi fornecido e realiza a operação correspondente
if operador == '+':
    # Realiza a soma se o operador for '+'
    resultado = operando1 + operando2
elif operador == '-':
    # Realiza a subtração se o operador for '-'
    resultado = operando1 - operando2
elif operador == '*':
    # Realiza a multiplicação se o operador for '*'
    resultado = operando1 * operando2
elif operador == '/':
    # Verifica se o segundo operando não é zero antes de realizar a divisão
    if operando2 != 0:
        resultado = operando1 / operando2
    else:
        # Se o segundo operando for zero, exibe uma mensagem de erro
        resultado = "Erro: Divisão por zero"
elif operador == '**':
    # Realiza a exponenciação se o operador for '**'
    resultado = operando1 ** operando2
else:
    # Exibe uma mensagem de erro se o operador fornecido for inválido
    resultado = "Erro: Operador inválido"

# Exibe o resultado da operação (ou a mensagem de erro, se aplicável)
print(f"Resultado: {resultado}")
