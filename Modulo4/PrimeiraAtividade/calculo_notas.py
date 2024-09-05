# Inicia uma variável booleana para controlar o loop
continuar = True

# Enquanto a variável continuar for True, o loop vai se repetir
while continuar:

    # Solicita a primeira nota ao usuário e a converte para float
    n1 = float(input("Digite a primeira nota (ou uma nota inválida para sair): "))
    
    # Verifica se a nota inserida é inválida (menor que 0 ou maior que 100)
    if n1 < 0 or n1 > 100:
        continuar = False  # Se a nota for inválida, define continuar como False para encerrar o loop
        print("Saindo...")  # Informa que está saindo
    else:
        # Solicita a segunda e a terceira notas ao usuário
        n2 = float(input("Digite a segunda nota: "))
        n3 = float(input("Digite a terceira nota: "))

        # Calcula a média das três notas
        m = (n1 + n2 + n3) / 3

        # Verifica a situação do aluno com base na média calculada
        if m >= 60:
            print("Aprovado")  # Se a média for maior ou igual a 60, o aluno está aprovado
        elif m >= 40:
            print("Recuperação")  # Se a média estiver entre 40 e 59, o aluno está de recuperação
        else:
            print("Reprovado")  # Se a média for menor que 40, o aluno está reprovado

        print("Fim")  # Exibe uma mensagem indicando o fim da operação
