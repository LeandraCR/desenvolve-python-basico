# Função que recebe um número de celular e o formata conforme as regras estabelecidas
def formatar_numero(numero):
    # Verifica se o número tem exatamente 8 dígitos
    if len(numero) == 8:
        numero = '9' + numero  # Adiciona o dígito '9' na frente do número

    # Verifica se o número já tem 9 dígitos e o primeiro dígito é '9'
    elif len(numero) == 9 and numero[0] == '9':
        pass  # Se já estiver correto, não faz nada

    # Adiciona um separador '-' entre os primeiros 5 dígitos e os últimos 4
    numero_formatado = numero[:5] + '-' + numero[5:]

    # Retorna o número formatado
    return numero_formatado

# Solicita ao usuário que insira um número de celular
numero = input("Digite o número: ")

# Chama a função de formatação e armazena o resultado
numero_completo = formatar_numero(numero)

# Exibe o número formatado para o usuário
print(f"Número completo: {numero_completo}")
