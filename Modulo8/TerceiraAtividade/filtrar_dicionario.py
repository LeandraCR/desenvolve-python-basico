# Função filtrar_dicionario
# Esta função recebe um dicionário e uma lista de chaves como parâmetros
# Ela retorna um novo dicionário contendo apenas as chaves presentes na lista.

def filtrar_dicionario(dicionario, chaves):
    # Compreensão de dicionário:
    # Para cada chave na lista 'chaves', verificamos se ela existe no dicionário original 'dicionario'.
    # Se a chave estiver presente, ela é adicionada ao novo dicionário com seu valor correspondente.
    return {chave: dicionario[chave] for chave in chaves if chave in dicionario}

# Exemplo de uso:
dados = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
chaves_filtradas = ['a', 'c', 'e']

# Chama a função filtrar_dicionario passando os dados e as chaves_filtradas como argumentos.
resultado = filtrar_dicionario(dados, chaves_filtradas)

# Exibe o resultado esperado: {'a': 1, 'c': 3, 'e': 5}
print(resultado)
