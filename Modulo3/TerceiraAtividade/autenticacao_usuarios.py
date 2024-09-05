# Define um dicionário contendo padrões de íris para diferentes usuários.
usuarios = {
    "usuario1": (123, 456, 789),
    "usuario2": (321, 654, 987),
    "usuario3": (111, 222, 333),
    "usuario4": (444, 555, 666)
}

# Define a margem de erro permitida para comparação dos valores.
margem_erro = 10

# Solicita ao usuário que insira os valores de leitura do padrão de íris.
print("Insira os valores da nova leitura de padrão de íris:")
valor1 = int(input("Valor 1: "))
valor2 = int(input("Valor 2: "))
valor3 = int(input("Valor 3: "))

# Inicializa a variável de autenticação como False.
autenticado = False

# Verifica se a leitura de padrão de íris corresponde a algum dos padrões armazenados.
# O processo é repetido para cada usuário.
# Se o padrão corresponder dentro da margem de erro, a autenticação é bem-sucedida e o loop termina.
usuario, padrao = "usuario1", usuarios["usuario1"]
if (abs(valor1 - padrao[0]) <= margem_erro and
    abs(valor2 - padrao[1]) <= margem_erro and
    abs(valor3 - padrao[2]) <= margem_erro):
    print(f"Autenticação bem-sucedida! Usuário: {usuario}")
    autenticado = True

usuario, padrao = "usuario2", usuarios["usuario2"]
if (abs(valor1 - padrao[0]) <= margem_erro and
    abs(valor2 - padrao[1]) <= margem_erro and
    abs(valor3 - padrao[2]) <= margem_erro):
    print(f"Autenticação bem-sucedida! Usuário: {usuario}")
    autenticado = True

usuario, padrao = "usuario3", usuarios["usuario3"]
if (abs(valor1 - padrao[0]) <= margem_erro and
    abs(valor2 - padrao[1]) <= margem_erro and
    abs(valor3 - padrao[2]) <= margem_erro):
    print(f"Autenticação bem-sucedida! Usuário: {usuario}")
    autenticado = True

usuario, padrao = "usuario4", usuarios["usuario4"]
if (abs(valor1 - padrao[0]) <= margem_erro and
    abs(valor2 - padrao[1]) <= margem_erro and
    abs(valor3 - padrao[2]) <= margem_erro):
    print(f"Autenticação bem-sucedida! Usuário: {usuario}")
    autenticado = True

# Se nenhum dos padrões corresponder, imprime uma mensagem de falha na autenticação.
if not autenticado:
    print("Falha na autenticação. Nenhum padrão correspondente encontrado.")
