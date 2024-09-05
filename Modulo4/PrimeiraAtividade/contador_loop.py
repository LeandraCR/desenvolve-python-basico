# Recebe um número inteiro do usuário e armazena na variável 'n'
n = int(input("Digite um número: "))

# Inicializa a variável 'cont' com 0
cont = 0

# Inicia um loop que continuará enquanto 'cont' for menor ou igual a 'n'
while n >= cont:
    # Incrementa 'cont' em 1 a cada iteração do loop
    cont += 1

    # Imprime o valor atual de 'cont'
    print(cont)

# Após o término do loop, imprime "Fim"
print("Fim")
