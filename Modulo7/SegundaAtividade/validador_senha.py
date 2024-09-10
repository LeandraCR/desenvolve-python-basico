import re  # Importa o módulo 're' para utilizar expressões regulares

def validador_senha(senha):
    # Verificar se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False
    
    # Verificar se a senha contém pelo menos uma letra maiúscula (A-Z)
    if not re.search(r'[A-Z]', senha):
        return False

    # Verificar se a senha contém pelo menos uma letra minúscula (a-z)
    if not re.search(r'[a-z]', senha):
        return False

    # Verificar se a senha contém pelo menos um número (0-9)
    if not re.search(r'\d', senha):
        return False

    # Verificar se a senha contém pelo menos um caractere especial (@, #, $, etc.)
    if not re.search(r'[@#$%^&+=]', senha):
        return False

    # Se a senha passou por todas as verificações, ela é válida
    return True

# Exemplo de uso para testar a função:
senha1 = "Senha123@"  # Senha que atende a todos os critérios
senha2 = "senhafraca"  # Senha que não contém letra maiúscula, número ou caractere especial
senha3 = "Senha_fraca"  # Senha que não contém número

# Imprime o resultado da função para cada senha
print(validador_senha(senha1))  # Saída esperada: True
print(validador_senha(senha2))  # Saída esperada: False
print(validador_senha(senha3))  # Saída esperada: False
