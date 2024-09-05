# Definindo os valores de entrada
salario_por_hora = 20.0
horas_trabalhadas = 40

# Calculando o salário bruto semanal
salario_bruto = salario_por_hora * horas_trabalhadas

# Calculando o salário líquido diretamente (descontos de 10% do INSS e 5% do sindicato)
salario_liquido = salario_bruto - (salario_bruto * 0.10 + salario_bruto * 0.05)

# Exibindo os resultados
print(f"Salário semanal bruto: R${salario_bruto:.2f}")
print(f"Salário semanal líquido: R${salario_liquido:.2f}")
