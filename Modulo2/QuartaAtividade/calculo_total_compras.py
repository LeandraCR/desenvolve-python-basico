# Solicita o nome do produto 1
nome_produto1 = input("Digite o nome do produto 1: ")

# Solicita o preço unitário do produto 1 e converte para float
preco_unitario1 = float(input("Digite o preço unitário do produto 1: "))

# Solicita a quantidade do produto 1 e converte para inteiro
quantidade1 = int(input("Digite a quantidade do produto 1: "))

# Calcula o subtotal do produto 1
subtotal1 = preco_unitario1 * quantidade1

# Solicita o nome do produto 2
nome_produto2 = input("Digite o nome do produto 2: ")

# Solicita o preço unitário do produto 2 e converte para float
preco_unitario2 = float(input("Digite o preço unitário do produto 2: "))

# Solicita a quantidade do produto 2 e converte para inteiro
quantidade2 = int(input("Digite a quantidade do produto 2: "))

# Calcula o subtotal do produto 2
subtotal2 = preco_unitario2 * quantidade2

# Solicita o nome do produto 3
nome_produto3 = input("Digite o nome do produto 3: ")

# Solicita o preço unitário do produto 3 e converte para float
preco_unitario3 = float(input("Digite o preço unitário do produto 3: "))

# Solicita a quantidade do produto 3 e converte para inteiro
quantidade3 = int(input("Digite a quantidade do produto 3: "))

# Calcula o subtotal do produto 3
subtotal3 = preco_unitario3 * quantidade3

# Calcula o total somando os subtotais dos três produtos
total = subtotal1 + subtotal2 + subtotal3

# Exibe o total formatado como valor monetário com duas casas decimais
print(f"Total: R${total:,.2f}")
