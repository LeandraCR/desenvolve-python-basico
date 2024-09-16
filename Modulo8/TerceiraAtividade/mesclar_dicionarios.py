# Função que mescla dois dicionários, preservando o maior valor em caso de chaves duplicadas
def mesclar_dicionarios(dic1, dic2):
    # Cria uma cópia do primeiro dicionário para evitar alterar o original
    resultado = dic1.copy()

    # Percorre cada chave e valor no segundo dicionário
    for chave, valor in dic2.items():
        # Se a chave já existir no primeiro dicionário (dentro do resultado)
        if chave in resultado:
            # Atualiza o valor dessa chave com o maior valor entre os dois dicionários
            resultado[chave] = max(resultado[chave], valor)
        else:
            # Se a chave não existir, adiciona a chave e o valor ao dicionário resultado
            resultado[chave] = valor

    # Retorna o dicionário mesclado com os maiores valores
    return resultado

# Exemplo de uso:
dicionario1 = {'a': 1, 'b': 2, 'c': 3}  # Primeiro dicionário de exemplo
dicionario2 = {'b': 4, 'd': 5}  # Segundo dicionário de exemplo
resultado = mesclar_dicionarios(dicionario1, dicionario2)  # Chama a função mesclar_dicionarios
print(resultado)  # Exibe o dicionário mesclado
# Saída esperada: {'a': 1, 'b': 4, 'c': 3, 'd': 5}
