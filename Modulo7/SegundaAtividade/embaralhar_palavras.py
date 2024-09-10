import random  # Importa a biblioteca random para realizar o embaralhamento das letras

def embaralhar_palavras(frase):
    # Função interna que embaralha as letras internas de uma palavra
    def embaralha_palavra(palavra):
        # Se a palavra tiver mais de 3 caracteres, embaralha as letras internas
        if len(palavra) > 3:
            meio = list(palavra[1:-1])  # Pega todas as letras, exceto a primeira e a última
            random.shuffle(meio)        # Embaralha as letras do meio
            # Retorna a palavra montada com a primeira letra, letras embaralhadas e a última letra
            return palavra[0] + ''.join(meio) + palavra[-1]
        return palavra  # Se a palavra for muito pequena, retorna ela sem alterações
    
    palavras = frase.split()  # Divide a frase em palavras, criando uma lista de palavras
    # Aplica o embaralhamento em cada palavra da lista
    palavras_embaralhadas = [embaralha_palavra(palavra) for palavra in palavras]
    # Junta as palavras embaralhadas em uma nova frase e retorna
    return ' '.join(palavras_embaralhadas)

# Exemplo de uso da função
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)  # Aplica o embaralhamento à frase
print(resultado)  # Exibe o resultado com as palavras embaralhadas
