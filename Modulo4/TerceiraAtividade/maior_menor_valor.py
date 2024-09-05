# Inicializa as variáveis para armazenar o maior e menor valor
# Elas começam como None para que possam ser atribuídas na primeira iteração
maior_valor = None
menor_valor = None

# Inicia o loop infinito para ler valores indefinidos
while True:
    # Lê o valor do usuário e converte para um número inteiro
    valor = int(input("Digite um valor (0 para encerrar): "))

    # Verifica se o valor é 0, o que encerra a leitura de dados e quebra o loop
    if valor == 0:
        break

    # Define o maior valor na primeira iteração ou se o valor atual for maior que o anterior
    if maior_valor is None or valor > maior_valor:
        maior_valor = valor
    
    # Define o menor valor na primeira iteração ou se o valor atual for menor que o anterior
    if menor_valor is None or valor < menor_valor:
        menor_valor = valor

# Após o loop, verifica se algum valor válido (não zero) foi digitado
if maior_valor is not None and menor_valor is not None:
    # Exibe o maior valor digitado
    print(f"O maior valor digitado foi: {maior_valor}")
    # Exibe o menor valor digitado
    print(f"O menor valor digitado foi: {menor_valor}")
else:
    # Caso nenhum valor tenha sido digitado antes de 0, exibe essa mensagem
    print("Nenhum valor foi digitado.")
