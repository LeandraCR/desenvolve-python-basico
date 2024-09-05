# Inicializa a variável x com o valor 1
x = 1 

# Inicia um loop 'while' que continuará enquanto x for diferente de 0
while x != 0:
    # Solicita ao usuário um valor para x e converte para float
    # Se o usuário digitar 0, o loop será interrompido
    x = float(input("Digite um valor para x (digite 0 para sair): "))

    # Verifica se o valor de x é maior que 5
    if x > 5:
        # Imprime a mensagem se a condição for verdadeira
        print("Maior que 5")

# Após o loop ser encerrado (quando x for 0), imprime "Fim"
print("Fim")
