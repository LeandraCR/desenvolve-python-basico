# Inicializa o produto com 1, pois qualquer número multiplicado por 1 é ele mesmo
produto = 1  

# Cria uma lista vazia para armazenar os valores positivos que serão digitados
valores = []  

# Inicia um loop infinito para continuar pedindo entradas do usuário
while True:
    # Solicita ao usuário que digite um valor inteiro
    valor = int(input("Digite um valor (0 para sair): "))
    
    # Se o valor digitado for 0, o programa encerra o loop
    if valor == 0:
        break  # Interrompe o loop
    
    # Se o valor for maior que 0, ele é adicionado à lista de valores positivos
    if valor > 0:
        valores.append(valor)  # Adiciona o valor positivo à lista

# Usa um loop for para multiplicar todos os valores positivos na lista
for valor in valores:
    produto *= valor  # Atualiza o valor de 'produto' multiplicando pelos valores da lista

# Exibe o resultado final do produto dos valores positivos
print("Produto:", produto)
