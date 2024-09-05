# Solicita ao usuário a distância da entrega em quilômetros
distancia = float(input("Informe a distância da entrega em quilômetros: "))

# Solicita ao usuário o peso do pacote em quilogramas
peso = float(input("Informe o peso do pacote em quilogramas: "))

# Verifica a distância para determinar o valor do frete com base no peso
if distancia <= 100:
    # Se a distância for menor ou igual a 100 km, o valor do frete é calculado a R$1.00 por quilograma
    valor_frete = peso * 1.00
elif 101 <= distancia <= 300:
    # Se a distância estiver entre 101 e 300 km, o valor do frete é calculado a R$1.50 por quilograma
    valor_frete = peso * 1.50
else:
    # Se a distância for superior a 300 km, o valor do frete é calculado a R$2.00 por quilograma
    valor_frete = peso * 2.00

# Adiciona um custo adicional se o peso do pacote for maior que 10 kg
if peso > 10:
    # Se o peso for superior a 10 kg, acrescenta R$10.00 ao valor do frete
    valor_frete += 10.00

# Exibe o valor final do frete com duas casas decimais
print(f"O valor do frete é: R${valor_frete:.2f}")
