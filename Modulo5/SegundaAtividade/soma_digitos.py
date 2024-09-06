# Função que calcula a soma dos dígitos de um número
def soma_digitos(numero):
    soma = 0  # Variável que armazenará a soma dos dígitos
    while numero > 0:  # Continua enquanto o número tiver dígitos
        soma += numero % 10  # Obtém o último dígito do número e o adiciona à soma
        numero = numero // 10  # Remove o último dígito do número (divisão inteira por 10)
    return soma  # Retorna o valor da soma dos dígitos

# Programa principal que solicita um número ao usuário
numero = int(input("Digite um número inteiro: "))  # Lê o número inserido pelo usuário e converte para inteiro
resultado = soma_digitos(numero)  # Chama a função soma_digitos passando o número digitado como argumento
print(f"A soma dos dígitos de {numero} é {resultado}.")  # Exibe o resultado da soma dos dígitos
