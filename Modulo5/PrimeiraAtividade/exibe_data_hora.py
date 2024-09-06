# Importa a classe datetime da biblioteca datetime
from datetime import datetime

# Obtém a data e hora atuais no formato de objeto datetime
data_hora_atual = datetime.now()

# Formata a data para o formato 'dia/mês/ano'
data_formatada = data_hora_atual.strftime("%d/%m/%Y")

# Formata a hora para o formato 'hora:minutos'
hora_formatada = data_hora_atual.strftime("%H:%M")

# Exibe a data formatada no console
print(f"Data: {data_formatada}")

# Exibe a hora formatada no console
print(f"Hora: {hora_formatada}")
