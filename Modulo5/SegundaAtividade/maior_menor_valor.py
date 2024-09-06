# Solicita a operação desejada (maior ou menor)
operacao = input("Você deseja encontrar o maior ou o menor valor? (Digite 'maior' ou 'menor'): ")

# Função lambda que recebe uma lista de valores e uma função (max ou min)
# A função lambda irá aplicar a função passada (max ou min) nos valores
calcular = lambda valores, func: func(valores)

# Lista para armazenar os valores digitados pelo usuário
valores = []

# Loop infinito que solicita números do usuário até que o valor 0 seja inserido
while True:
    # Solicita um valor ao usuário e converte para tipo float
    valor = float(input("Digite um valor (ou 0 para finalizar): "))
    
    # Se o valor digitado for 0, o loop é encerrado
    if valor == 0:
        break
    
    # Adiciona o valor à lista de valores
    valores.append(valor)

# Verifica a operação escolhida pelo usuário, permitindo várias formas de digitação
if operacao == "maior" or operacao == "MAIOR" or operacao == "Maior":
    # Se o usuário escolheu "maior", aplica a função max para encontrar o maior valor
    resultado = calcular(valores, max)
elif operacao == "menor" or operacao == "MENOR" or operacao == "Menor":
    # Se o usuário escolheu "menor", aplica a função min para encontrar o menor valor
    resultado = calcular(valores, min)
else:
    # Se o usuário digitou algo inválido, imprime uma mensagem de erro e encerra o programa
    print("Operação inválida!")
    exit()

# Exibe o resultado final, seja o maior ou menor valor, conforme a escolha do usuário
print(f"O {operacao} valor digitado foi: {resultado}")
