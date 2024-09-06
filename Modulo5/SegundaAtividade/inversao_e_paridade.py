# Função para inverter o valor
# Recebe um número inteiro e retorna o número com os dígitos invertidos
def inverteValor(num):
    # Converte o número para string, inverte a string e converte de volta para inteiro
    invertido = int(str(num)[::-1])
    return invertido

# Função para verificar se o número original e o invertido têm a mesma paridade
# Ou seja, se ambos são pares ou ambos são ímpares
def verificaInverso(original, invertido):
    # Verifica se ambos os números são pares ou ambos são ímpares
    if (original % 2 == 0 and invertido % 2 == 0) or (original % 2 != 0 and invertido % 2 != 0):
        return True  # Retorna True se ambos forem pares ou ambos forem ímpares
    return False  # Retorna False caso contrário

# Programa principal
# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Chama a função para inverter o número digitado
num_invertido = inverteValor(numero)

# Exibe o número invertido
print(f"O número invertido é: {num_invertido}")

# Chama a função para verificar se o número original e o invertido têm a mesma paridade
resultado = verificaInverso(numero, num_invertido)

# Exibe o resultado da verificação
if resultado:
    print("O número original e o invertido são ambos pares ou ambos ímpares.")
else:
    print("O número original e o invertido têm paridade diferente.")
