# Solicita que o usuário insira um ano e armazena o valor como inteiro
ano = int(input("Insira um ano: "))

# Verifica se o ano é bissexto
# Um ano é bissexto se for divisível por 4 e não for divisível por 100,
# exceto se for divisível por 400
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Bissexto")  # Exibe "Bissexto" se a condição for verdadeira
else:
    print("Não Bissexto")  # Exibe "Não Bissexto" se a condição for falsa
