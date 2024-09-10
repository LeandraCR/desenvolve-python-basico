# Função para calcular o dígito verificador do CPF
# A função recebe a soma e aplica o cálculo de resto da divisão por 11
def calcular_digito_verificador(soma):
    resto = soma % 11  # Calcula o resto da divisão da soma por 11
    if resto < 2:  # Se o resto for menor que 2, o dígito verificador é 0
        return 0
    else:
        return 11 - resto  # Caso contrário, o dígito é 11 menos o resto

# Função principal para validar o CPF
def validar_cpf(cpf):
    # Remove os pontos e o traço do CPF (deixa apenas números)
    cpf = cpf.replace(".", "").replace("-", "")
    
    # Verifica se o CPF tem exatamente 11 dígitos
    if len(cpf) != 11:
        return "CPF Inválido"
    
    # Verifica se todos os dígitos são iguais (CPF inválido, como "111.111.111-11")
    if cpf == cpf[0] * 11:
        return "CPF Inválido"
    
    # Cálculo do primeiro dígito verificador
    soma_1 = 0
    # Para os primeiros 9 dígitos, multiplica pelo peso (10, 9, 8, ..., 2) e soma
    for i in range(9):
        soma_1 += int(cpf[i]) * (10 - i)
    
    # Calcula o primeiro dígito verificador a partir da soma
    digito1 = calcular_digito_verificador(soma_1)
    
    # Cálculo do segundo dígito verificador
    soma_2 = 0
    # Para os primeiros 10 dígitos (incluindo o primeiro dígito verificador), multiplica pelo peso (11, 10, 9, ..., 2)
    for i in range(10):
        soma_2 += int(cpf[i]) * (11 - i)
    
    # Calcula o segundo dígito verificador a partir da soma
    digito2 = calcular_digito_verificador(soma_2)
    
    # Verifica se os dígitos verificadores calculados são iguais aos dígitos fornecidos no CPF
    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
        return "CPF Válido"
    else:
        return "CPF Inválido"

# Teste com um CPF de exemplo (o usuário digita um CPF para testar)
cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")
print(validar_cpf(cpf))  # Imprime se o CPF é válido ou inválido
