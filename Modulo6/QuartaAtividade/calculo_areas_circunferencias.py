import math  # Importa a biblioteca math, que contém a constante pi

# Lista com os raios das circunferências
raios = [1.5, 0.8, 2.3, 5.0]

# Usamos a função map para aplicar uma função a cada elemento da lista raios.
# A função lambda é usada para calcular a área de cada circunferência, usando a fórmula pi * r^2.
# O round() é usado para arredondar o resultado para 2 casas decimais.
areas = list(map(lambda r: round(math.pi * (r ** 2), 2), raios))

# Exibe a lista com as áreas calculadas
print(areas)
