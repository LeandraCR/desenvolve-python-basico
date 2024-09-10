# Definindo o valor do salário por hora
salario_por_hora = 20.0

# Definindo o número de horas trabalhadas na semana
horas_trabalhadas = 40

# Calculando o salário bruto (antes dos descontos)
salario_bruto = salario_por_hora * horas_trabalhadas

# Calculando o salário líquido após os descontos
# Desconto de 10% (imposto) + 5% (outros descontos)
salario_liquido = salario_bruto - (salario_bruto * 0.10 + salario_bruto * 0.05)

# Exibindo o salário bruto formatado com duas casas decimais
print(f"Salário semanal bruto: R${salario_bruto:.2f}")

# Exibindo o salário líquido formatado com duas casas decimais
print(f"Salário semanal líquido: R${salario_liquido:.2f}")
