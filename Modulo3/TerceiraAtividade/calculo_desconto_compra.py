# Solicita ao usuário o valor total da compra e converte para float
valor_total_compra = float(input("Digite o valor total da compra: R$ "))

# Inicializa a variável desconto com 0
desconto = 0

# Verifica a faixa de valor total da compra e define o desconto correspondente
if valor_total_compra < 50:
    desconto = 0
elif valor_total_compra >= 100:
    desconto = 20
else:
    desconto = 10

# Calcula o valor final com desconto aplicado
valor_com_desconto = valor_total_compra - (valor_total_compra * desconto / 100)

# Exibe o desconto aplicado e o valor final com desconto
print(f"Desconto aplicado: {desconto}%")
print(f"Valor final com desconto: R$ {valor_com_desconto:.2f}")
