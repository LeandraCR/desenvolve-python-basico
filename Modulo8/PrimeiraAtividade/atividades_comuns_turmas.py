# Definindo as turmas e suas atividades em conjuntos
turmas = [
    {'ações comunitárias', 'futebol', 'música', 'rugby'},  # Atividades da turma 1
    {'ações comunitárias', 'música', 'rugby', 'teatro'},    # Atividades da turma 2
    {'música', 'rugby', 'teatro', 'vôlei'},                 # Atividades da turma 3
    {'música', 'vôlei', 'rugby'},                           # Atividades da turma 4
    {'ações comunitárias', 'futebol', 'rugby', 'teatro', 'vôlei'},  # Atividades da turma 5
    {'ações comunitárias', 'futebol', 'rugby'},             # Atividades da turma 6
    {'ações comunitárias', 'rugby', 'teatro', 'vôlei'},     # Atividades da turma 7
    {'ações comunitárias', 'rugby', 'teatro', 'vôlei'},     # Atividades da turma 8
    {'ações comunitárias', 'rugby', 'vôlei'}               # Atividades da turma 9
]

# Começando com o conjunto de atividades da primeira turma
atividades_comuns = set(turmas[0])  # Inicializa as atividades comuns com as atividades da turma 1

# Itera sobre as demais turmas para encontrar as atividades em comum
for turma in turmas[1:]:
    atividades_comuns &= turma  # Interseção: mantém apenas atividades que estão presentes em todas as turmas

# Exibindo as atividades comuns a todas as turmas
print("Atividades comuns a todas as turmas:", atividades_comuns)
