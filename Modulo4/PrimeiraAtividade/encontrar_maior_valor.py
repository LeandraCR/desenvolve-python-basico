# Solicita ao usuário que insira o valor de 'n', que representa quantas vezes será solicitado o valor de 'x'.
n = int(input("Digite o valor de n: "))

# Inicializa a variável 'maior' com 0, que será usada para armazenar o maior valor inserido.
maior = 0

# Loop que será executado enquanto 'n' for maior que 0.
while n > 0:

    # Solicita ao usuário que insira o valor de 'x'.
    x = int(input("Digite o valor de x: "))
    
    # Verifica se o valor de 'x' é maior que o valor armazenado em 'maior'.
    # Se for maior, 'maior' recebe o valor de 'x'.
    if x > maior:
        maior = x
    
    # Diminui o valor de 'n' em 1 a cada iteração.
    n -= 1

# Exibe o maior valor inserido pelo usuário.
print("O maior valor é:", maior)
