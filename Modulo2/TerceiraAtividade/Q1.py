salario_por_hora = 20  
horas_trabalhadas_semana = 40 

salario_bruto = salario_por_hora * horas_trabalhadas_semana
desconto_inss = salario_bruto * 0.10
desconto_sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (desconto_inss + desconto_sindicato)

print(f"Salário semanal bruto: R$ {salario_bruto:.2f}")
print(f"Valor descontado por semana INSS: R$ {desconto_inss:.2f}")
print(f"Valor descontado por semana pelo sindicato: R$ {desconto_sindicato:.2f}")
print(f"Salário semanal líquido: R$ {salario_liquido:.2f}")

# Definindo as variáveis
salario_por_hora = 20
horas_trabalhadas_semana = 40

# Calculando o salário semanal bruto
salario_bruto = salario_por_hora * horas_trabalhadas_semana

# Calculando o salário semanal líquido em uma única expressão composta
salario_liquido = salario_bruto - (salario_bruto * 0.10 + salario_bruto * 0.05)

# Exibindo os resultados
salario_bruto, salario_liquido

