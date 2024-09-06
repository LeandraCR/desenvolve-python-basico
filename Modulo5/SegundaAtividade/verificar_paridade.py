# Função lambda para verificar paridade.
# Ela recebe um número 'x' e retorna "par" se o número for divisível por 2, 
# ou "ímpar" se não for.
par_ou_impar = lambda x: "par" if x % 2 == 0 else "ímpar"

# Loop infinito para solicitar a entrada de números ao usuário.
while True:
    # Solicita um número ao usuário e converte a entrada para um número inteiro.
    numero = int(input("Digite um número (0 para sair): "))
    
    # Verifica se o número digitado é 0. Caso seja, o loop é encerrado.
    if numero == 0:
        break
    
    # Chama a função lambda e imprime se o número é "par" ou "ímpar".
    print(par_ou_impar(numero))
