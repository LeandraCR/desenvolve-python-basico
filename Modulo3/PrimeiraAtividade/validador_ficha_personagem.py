# Solicita ao usuário para escolher uma classe de personagem: guerreiro, mago ou arqueiro
classe = input("Escolha a classe do personagem (guerreiro, mago ou arqueiro): ")

# Solicita ao usuário para inserir os pontos de Força, um valor inteiro entre 1 e 20
forca = int(input("Digite os pontos de Força (1 a 20): "))

# Solicita ao usuário para inserir os pontos de Magia, também um valor inteiro entre 1 e 20
magia = int(input("Digite os pontos de Magia (1 a 20): "))

# Verifica se os pontos de Força e Magia estão dentro do intervalo válido (entre 1 e 20)
pontos_validos = (1 <= forca <= 20) and (1 <= magia <= 20)

# Verifica se o personagem é um guerreiro, com Força >= 15 e Magia <= 10, além de ter pontos válidos
guerreiro = pontos_validos and (classe == "guerreiro") and (forca >= 15) and (magia <= 10)

# Verifica se o personagem é um mago, com Força <= 10 e Magia >= 15, além de ter pontos válidos
mago = pontos_validos and (classe == "mago") and (forca <= 10) and (magia >= 15)

# Verifica se o personagem é um arqueiro, com Força e Magia entre 5 e 15, além de ter pontos válidos
arqueiro = pontos_validos and (classe == "arqueiro") and (forca > 5) and (forca <= 15) and (magia > 5) and (magia <= 15)

# Verifica se o personagem criado é válido, sendo guerreiro, mago ou arqueiro
valido = guerreiro or mago or arqueiro

# Exibe se o personagem criado é válido (True ou False)
print(valido)
