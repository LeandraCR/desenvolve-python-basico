# Solicita o comprimento do terreno em metros e converte para inteiro
comprimento = int(input("Digite o comprimento do terreno (em metros): "))

# Solicita a largura do terreno em metros e converte para inteiro
largura = int(input("Digite a largura do terreno (em metros): "))

# Solicita o preço por metro quadrado em reais e converte para float
preco_m2 = float(input("Digite o preço do metro quadrado (em R$): "))

# Calcula a área do terreno em metros quadrados
area_m2 = comprimento * largura

# Calcula o preço total do terreno, multiplicando o preço por metro quadrado pela área
preco_total = preco_m2 * area_m2

# Exibe a área do terreno em metros quadrados e o preço total em reais, formatado com duas casas decimais
print(f"O terreno possui {area_m2}m² e custa R${preco_total:,.2f}")
