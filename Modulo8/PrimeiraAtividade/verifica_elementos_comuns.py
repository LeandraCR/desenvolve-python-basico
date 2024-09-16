# Função para verificar se duas listas possuem elementos em comum
def tem_elementos_comuns(lista1, lista2):
    # Converte as duas listas em sets e utiliza a interseção (&) para encontrar elementos em comum
    # A função retorna True se houver elementos em comum, ou False se não houver
    return bool(set(lista1) & set(lista2))

# Teste da função
lista1 = [1, 2, 3, 4]  # Primeira lista de números
lista2 = [3, 4, 5, 6, 7]  # Segunda lista de números
resultado = tem_elementos_comuns(lista1, lista2)  # Chama a função para verificar se há elementos em comum
print(resultado)  # Exibe o resultado, que será True, pois há elementos em comum (3 e 4)
