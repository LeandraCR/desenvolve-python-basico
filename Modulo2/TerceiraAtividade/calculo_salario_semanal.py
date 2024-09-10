# Definindo o valor do salário por hora
salario_por_hora = 20  

# Definindo a quantidade de horas trabalhadas na semana
horas_trabalhadas_semana = 40 

# Calculando o salário bruto semanal (salário por hora vezes as horas trabalhadas na semana)
salario_bruto = salario_por_hora * horas_trabalhadas_semana

# Calculando o desconto do INSS (10% do salário bruto)
desconto_inss = salario_bruto * 0.10

# Calculando o desconto do sindicato (5% do salário bruto)
desconto_sindicato = salario_bruto * 0.05

# Calculando o salário líquido semanal (salário bruto menos os descontos do INSS e sindicato)
salario_liquido = salario_bruto - (desconto_inss + desconto_sindicato)

# Exibindo o salário bruto semanal
print(f"Salário semanal bruto: R$ {salario_bruto:.2f}")

# Exibindo o valor descontado semanalmente para o INSS
print(f"Valor descontado por semana INSS: R$ {desconto_inss:.2f}")

# Exibindo o valor descontado semanalmente para o sindicato
print(f"Valor descontado por semana pelo sindicato: R$ {desconto_sindicato:.2f}")

# Exibindo o salário líquido semanal
print(f"Salário semanal líquido: R$ {salario_liquido:.2f}")
