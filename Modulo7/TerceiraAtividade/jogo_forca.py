import random  # Importa o módulo random para escolher uma palavra aleatória

# Função para ler o arquivo de palavras
def carregar_palavras():
    # Abre o arquivo 'gabarito_forca.txt' no modo leitura
    with open("gabarito_forca.txt", "r") as arquivo:
        palavras = arquivo.readlines()  # Lê todas as linhas do arquivo
    return [palavra.strip() for palavra in palavras]  # Retorna uma lista de palavras sem quebras de linha

# Função para carregar os estágios do enforcado
def carregar_enforcado():
    # Abre o arquivo 'gabarito_enforcado.txt' no modo leitura
    with open("gabarito_enforcado.txt", "r") as arquivo:
        # Divide os estágios do enforcamento pelo separador '\n\n' (dupla quebra de linha)
        estagios = arquivo.read().split("\n\n")
    return estagios  # Retorna uma lista com cada estágio do enforcamento

# Função para imprimir o estágio do enforcamento
def imprime_enforcado(erros, estagios):
    print(estagios[erros])  # Exibe o estágio correspondente ao número de erros

# Função principal do jogo
def jogar_forca():
    palavras = carregar_palavras()  # Carrega a lista de palavras do arquivo
    estagios = carregar_enforcado()  # Carrega os estágios do enforcamento
    
    palavra = random.choice(palavras).lower()  # Escolhe uma palavra aleatória da lista e converte para minúsculas
    letras_descobertas = ["_"] * len(palavra)  # Inicializa a palavra com underscores ('_')
    letras_erradas = []  # Lista para armazenar letras erradas
    tentativas = 6  # Limite máximo de tentativas/erros
    erros = 0  # Contador de erros
    
    # Mensagem inicial do jogo
    print("Bem-vindo ao jogo da Forca!")
    print("A palavra tem", len(palavra), "letras.")  # Exibe o número de letras da palavra
    print(" ".join(letras_descobertas))  # Exibe os underscores da palavra
    
    # Enquanto o jogador não errou 6 vezes e ainda há letras para descobrir
    while erros < tentativas and "_" in letras_descobertas:
        print("\nLetras erradas até agora: ", " ".join(letras_erradas))  # Exibe as letras erradas
        chute = input("Adivinhe uma letra: ").lower()  # Solicita ao jogador uma letra

        # Verifica se a letra já foi adivinhada (correta ou errada)
        if chute in letras_erradas or chute in letras_descobertas:
            print("Você já tentou essa letra.")
        elif chute in palavra:  # Se a letra estiver na palavra
            # Atualiza os underscores com a letra correta
            for i in range(len(palavra)):
                if palavra[i] == chute:
                    letras_descobertas[i] = chute
            print("Boa! A letra", chute, "está na palavra.")
        else:
            # Se a letra não estiver na palavra, adiciona aos erros  
            erros += 1
            letras_erradas.append(chute)
            print("Errou! A letra", chute, "não está na palavra.")
            imprime_enforcado(erros, estagios)  # Exibe o estágio do enforcamento
        
        # Mostra o progresso atual do jogador (letras acertadas e underscores restantes)
        print(" ".join(letras_descobertas))

    # Se o jogador descobriu todas as letras
    if "_" not in letras_descobertas:
        print("\nParabéns! Você venceu. A palavra era:", palavra)
    else:
        # Se o jogador foi enforcado (errou 6 vezes)
        print("\nVocê foi enforcado! A palavra era:", palavra)

# Inicia o jogo
jogar_forca()
