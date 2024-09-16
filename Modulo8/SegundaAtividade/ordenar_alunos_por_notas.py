def ordenar_tuplas(alunos_notas):
    # A função sorted() irá ordenar a lista de tuplas
    # O argumento 'key=lambda x: x[1]' especifica que a ordenação será feita com base no segundo elemento de cada tupla (a nota)
    # 'reverse=True' faz a ordenação ser em ordem decrescente
    return sorted(alunos_notas, key=lambda x: x[1], reverse=True)

# Exemplo de uso da função
alunos_notas = [('Alice', 8.5), ('Bob', 7.2), ('Charlie', 9.0), ('David', 8.8)]

# Chamando a função para ordenar a lista de alunos e suas respectivas notas
resultado = ordenar_tuplas(alunos_notas)

# Exibindo a lista de alunos ordenada por nota em ordem decrescente
print(resultado)
