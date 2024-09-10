# Lista com os meses por extenso
# Cada posição na lista corresponde ao número do mês, ou seja,
# 'Janeiro' está na posição 0, 'Fevereiro' na posição 1, e assim por diante.
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# Solicitar ao usuário que insira a data de nascimento no formato 'dd/mm/aaaa'
data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")

# A função split("/") divide a string de data nas partes 'dia', 'mes', e 'ano'
# com base no caractere separador '/'.
dia, mes, ano = data_nascimento.split("/")

# O mês informado é convertido de string para inteiro para que possamos
# usá-lo como índice na lista de meses. Subtraímos 1 porque os índices
# das listas começam em 0, enquanto os meses do calendário vão de 1 a 12.
mes_extenso = meses[int(mes) - 1]

# Exibir a mensagem formatada com o dia, o nome do mês por extenso, e o ano.
print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")
