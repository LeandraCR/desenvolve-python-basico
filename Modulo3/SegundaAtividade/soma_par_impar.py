# Solicita ao usuário que insira o primeiro número e converte a entrada para um número inteiro
numero1 = int(input("Digite o primeiro número: "))

# Solicita ao usuário que insira o segundo número e converte a entrada para um número inteiro
numero2 = int(input("Digite o segundo número: "))

# Calcula a soma dos dois números inseridos
soma = numero1 + numero2

# Verifica se a soma é um número par ou ímpar usando o operador de módulo (%) para verificar o resto da divisão por 2
if soma % 2 == 0:
    # Se o resto for 0, a soma é par, e esta mensagem será exibida
    print(f"A soma de {numero1} e {numero2} é {soma}, que é um número par.")
else:
    # Se o resto não for 0, a soma é ímpar, e esta mensagem será exibida
    print(f"A soma de {numero1} e {numero2} é {soma}, que é um número ímpar.")
