import emoji  # type: ignore # Importa a biblioteca emoji, que permite trabalhar com emojis no Python.

# Dicionário com alguns exemplos de emojis e suas descrições.
# Cada chave é o código textual do emoji, e o valor é a função emoji.emojize(),
# que converte esse código textual em um emoji visual.
emoji_dict = {
    ":grinning_face:": emoji.emojize(":grinning_face:"),  # Rosto sorridente 😀
    ":thumbs_up:": emoji.emojize(":thumbs_up:"),  # Polegar para cima 👍
    ":red_heart:": emoji.emojize(":red_heart:"),  # Coração vermelho ❤️
    ":fire:": emoji.emojize(":fire:"),  # Fogo 🔥
    ":clapping_hands:": emoji.emojize(":clapping_hands:"),  # Mãos batendo palmas 👏
}

# Exibe a lista de emojis disponíveis para o usuário.
print("Lista de emojis disponíveis:")
# Itera sobre o dicionário emoji_dict, imprimindo o código textual (ex: :grinning_face:)
# e o símbolo do emoji correspondente (ex: 😀).
for code, symbol in emoji_dict.items():
    print(f"{code}: {symbol}")

# Solicita ao usuário que insira uma frase com emojis codificados, por exemplo,
# utilizando os códigos de emojis exibidos anteriormente, como ":grinning_face:".
frase_codificada = input("Digite uma frase codificada com emojis (exemplo: Eu estou :grinning_face: hoje): ")

# Decodifica a frase que o usuário digitou, substituindo os códigos de emojis
# pelos emojis visuais correspondentes usando a função emoji.emojize().
frase_emojizada = emoji.emojize(frase_codificada)

# Exibe a frase original, agora com os emojis convertidos.
print("\nFrase com emojis:")
print(frase_emojizada)
