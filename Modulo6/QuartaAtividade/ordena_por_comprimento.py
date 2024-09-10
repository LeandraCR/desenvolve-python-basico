# Função chamada ordena_por_comprimento que ordena uma lista de nomes pelo comprimento das strings
def ordena_por_comprimento(nomes):
    # A função sorted é usada para ordenar a lista 'nomes'
    # O parâmetro key define que o critério de ordenação será o comprimento das strings (len(nome))
    return sorted(nomes, key=lambda nome: len(nome))

# Lista de nomes fornecida
nomes = ["Joao", "Maria", "Jose", "Gabriela", "Sol", "Luna", "Bento", "Enzo", "Fernanda"]

# Chama a função ordena_por_comprimento e armazena o resultado na variável 'resultado'
resultado = ordena_por_comprimento(nomes)

# Imprime o resultado, que será a lista de nomes ordenada pelo comprimento das strings
print(resultado)
