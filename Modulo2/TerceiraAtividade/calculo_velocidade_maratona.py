# Define a distância de uma maratona em quilômetros
distancia_km = 42.195

# Define o tempo disponível para completar a maratona em horas
tempo_horas = 3

# Converte a distância de quilômetros para metros
distancia_metros = distancia_km * 1000

# Converte o tempo de horas para segundos
tempo_segundos = tempo_horas * 3600

# Calcula a velocidade média necessária para completar a maratona
velocidade_media = distancia_metros / tempo_segundos

# Exibe a velocidade média necessária para completar a maratona no tempo determinado
print(f"A velocidade média necessária para completar a maratona em {tempo_horas} horas é de {velocidade_media:.2f} metros por segundo.")
