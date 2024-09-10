import random  # Importa a biblioteca random para gerar números aleatórios

# Gera uma lista de 20 números aleatórios entre 1 e 100
lista = [random.randint(1, 100) for _ in range(20)]

# Exibe a lista original gerada aleatoriamente
print("Lista original:")
print(lista)

# Loop infinito que continua até o usuário digitar 0
while True:
    # Solicita ao usuário o tamanho para dividir a lista
    tamanho = int(input("Tamanho para divisão (digite 0 para sair): "))

    # Se o usuário digitar 0, o programa encerra
    if tamanho == 0:
        print("Programa encerrado.")  # Mensagem de encerramento
        break  # Sai do loop e termina o programa
    
    # Divide a lista em sublistas do tamanho solicitado pelo usuário
    # A função range percorre a lista em intervalos de 'tamanho'
    sublistas = [lista[i:i + tamanho] for i in range(0, len(lista), tamanho)]
    
    # Exibe o tamanho solicitado e as sublistas geradas
    print(f"Tamanho para divisão: {tamanho}")
    print("Sublistas:", sublistas)
