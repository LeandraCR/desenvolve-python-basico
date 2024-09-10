# Lista de alunos
alunos = ["Maria", "Jose", "Carla", "Sol"]

# Lista de notas correspondentes aos alunos
notas = [35, 50, 20, 80]

# Lista de aprovados usando compreensão de lista
# Percorre os índices das notas e adiciona à lista 'aprovados' apenas os alunos com nota >= 60
aprovados = [alunos[i] for i in range(len(notas)) if notas[i] >= 60]

# Imprime a lista de alunos aprovados
print(aprovados)
