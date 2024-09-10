def avalia_tabuleiro(tabuleiro):
    # Verifica cada linha do tabuleiro
    for linha in tabuleiro:
        # Se todos os elementos da linha forem iguais e não forem vazios, retorna o vencedor ('X' ou 'O')
        if linha[0] == linha[1] == linha[2] and linha[0] != ' ':
            return linha[0]  # Retorna 'X' ou 'O', quem venceu
    
    # Verifica cada coluna do tabuleiro
    for col in range(3):
        # Se todos os elementos da coluna forem iguais e não forem vazios, retorna o vencedor ('X' ou 'O')
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] and tabuleiro[0][col] != ' ':
            return tabuleiro[0][col]  # Retorna 'X' ou 'O', quem venceu
    
    # Verifica a diagonal principal (de cima à esquerda para baixo à direita)
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != ' ':
        return tabuleiro[0][0]  # Retorna 'X' ou 'O', quem venceu na diagonal principal
    
    # Verifica a diagonal secundária (de cima à direita para baixo à esquerda)
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != ' ':
        return tabuleiro[0][2]  # Retorna 'X' ou 'O', quem venceu na diagonal secundária
    
    # Se ninguém venceu (não encontrou três iguais seguidos), retorna "Empate"
    return "Empate"

# Testando o exemplo 1
tabuleiro1 = [
    ['x', 'o', 'x'],
    [' ', 'x', 'o'],
    ['o', ' ', 'o']
]
# O resultado esperado é "Empate", pois não há três iguais seguidos
print(avalia_tabuleiro(tabuleiro1))  # Esperado: "Empate"

# Testando o exemplo 2
tabuleiro2 = [
    ['o', 'x', 'o'],
    ['x', 'o', 'x'],
    ['x', ' ', 'o']
]
# O resultado esperado é "o", pois 'O' venceu na diagonal
print(avalia_tabuleiro(tabuleiro2))  # Esperado: "o"
