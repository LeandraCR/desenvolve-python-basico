# Definindo uma função chamada testa_equilatero que recebe uma lista de três lados de um triângulo
def testa_equilatero(lados):
    # Verifica se todos os três lados são iguais. Se sim, retorna True (verdadeiro), caso contrário, retorna False
    return lados[0] == lados[1] == lados[2]

# Lista de triângulos representada por listas contendo três valores, cada um correspondendo ao tamanho dos lados
triangulos = [[2, 2, 2], [3, 4, 5], [3, 2, 2], [4, 4, 4]]

# Aplicando a função testa_equilatero a cada triângulo na lista triangulos usando a função filter
# A função filter retorna apenas os triângulos equiláteros, ou seja, aqueles que passaram no teste
triangulos_equilateros = list(filter(testa_equilatero, triangulos))

# Exibe os triângulos equiláteros, mostrando apenas aqueles onde os três lados são iguais
print(triangulos_equilateros)
