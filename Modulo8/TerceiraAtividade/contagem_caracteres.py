# Função chamada contagem_caracteres que recebe uma string como argumento
def contagem_caracteres(string):
    # Criação de um dicionário vazio que armazenará o resultado
    resultado = {}
    
    # Loop através de cada caractere da string
    for caractere in string:
        # Verifica se o caractere já está no dicionário
        if caractere in resultado:
            # Se o caractere já existe no dicionário, incrementa a contagem
            resultado[caractere] += 1
        else:
            # Caso contrário, adiciona o caractere ao dicionário com valor 1
            resultado[caractere] = 1
    
    # Retorna o dicionário contendo a contagem de cada caractere
    return resultado

# Exemplo de uso da função contagem_caracteres
frase = "python programming"
resultado = contagem_caracteres(frase)

# Exibe o dicionário com a contagem de caracteres da string fornecida
print(resultado)
