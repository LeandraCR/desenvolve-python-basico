# Lista das horas trabalhadas por diferentes funcionários
horas_trabalhadas = [40, 37, 45, 40, 40, 48]

# Valor do pagamento por hora de trabalho regular
ganho_por_hora = 20

# Valor adicional pago por cada hora extra trabalhada (acima de 40 horas)
hora_extra = 25

# Usamos uma compreensão de listas para calcular o pagamento total
# O pagamento é calculado da seguinte forma:
# 1. Para as horas trabalhadas até 40, multiplicamos pelo ganho_por_hora.
# 2. Para as horas extras (acima de 40), multiplicamos a diferença pelo hora_extra.
pagamentos = [ganho_por_hora * min(hora, 40) + hora_extra * max(0, hora - 40) for hora in horas_trabalhadas]

# Exibindo a lista de pagamentos para cada funcionário
print(pagamentos)
