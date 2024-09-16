# Função que calcula a área e o perímetro de um terreno retangular
# A função recebe uma tupla (largura, comprimento) e retorna a área e o perímetro

def calcula_area_perimetro(dimensoes):
    # Desempacota a tupla dimensoes nas variáveis largura e comprimento
    largura, comprimento = dimensoes
    
    # Calcula a área do terreno: largura * comprimento
    area = largura * comprimento
    
    # Calcula o perímetro do terreno: 2 * (largura + comprimento)
    perimetro = 2 * (largura + comprimento)
    
    # Retorna a área e o perímetro como uma tupla (area, perimetro)
    return area, perimetro

# Exemplo de uso da função

# Atribui valores para largura e comprimento
largura = 5
comprimento = 7

# Chama a função calcula_area_perimetro passando uma tupla (largura, comprimento)
retorno = calcula_area_perimetro((largura, comprimento))

# Imprime o retorno da função e o tipo do retorno (que será uma tupla)
print(retorno, type(retorno))
