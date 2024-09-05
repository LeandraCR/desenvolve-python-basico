# Inicializa o resultado com zero
resultado = 0

# Define a operação inicial como adição
operacao = "+"

# Variável para controlar se o loop deve continuar
fim = False

# Inicia o loop enquanto a variável 'fim' for False
while not fim:
    # Pede a entrada do usuário (número, operador ou 'Fim')
    entrada = input("Digite um número ou operador (+, -) ou 'Fim' para sair: ")

    # Verifica se a entrada é "Fim" para encerrar o loop
    if entrada == "Fim":
        fim = True  # Define 'fim' como True para parar o loop
    # Verifica se a entrada é um operador (+ ou -)
    elif entrada in ["+", "-"]:
        operacao = entrada  # Armazena a operação
    # Caso contrário, assume que a entrada é um número
    else:
        numero = int(entrada)  # Converte a entrada para um número inteiro
        # Aplica a operação armazenada ao número atual
        if operacao == "+":
            resultado += numero  # Soma o número ao resultado
        elif operacao == "-":
            resultado -= numero  # Subtrai o número do resultado

# Exibe o resultado final após a palavra "Fim" ser digitada
print(f"Resultado: {resultado}")
