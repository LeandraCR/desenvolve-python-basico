import csv
from collections import namedtuple
from getpass import getpass
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

# Constantes que definem os caminhos dos arquivos e a variável global para o usuário logado
ARQUIVO_USUARIOS = 'usuarios.csv'
ARQUIVO_PRODUTOS = 'produtos.csv'
USUARIO_LOGADO = None

# Inicializa o console para imprimir com estilo
console = Console()

##################### Funções de usuário #####################

# Função que lê os dados dos usuários de um arquivo CSV
def ler_usuarios(arquivo_csv):
    Usuario = namedtuple('Usuario', ['login', 'senha', 'tipo'])
    usuarios = {}
    try:
        # Abre o arquivo de usuários no modo de leitura
        with open(arquivo_csv, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                login, senha, tipo = row
                usuarios[login] = Usuario(login=login, senha=senha, tipo=tipo)
    except FileNotFoundError:
        # Se o arquivo não existir, ele é criado vazio
        open(arquivo_csv, 'w').close()
    return usuarios

# Função que realiza o login de um usuário
def fazer_login(usuarios):
    global USUARIO_LOGADO
    # Tela de login usando rich
    console.print(Panel('🟢 [bold green]Login[/bold green] 🟢\n\nPor favor, insira suas credenciais.', expand=False))
    login = Prompt.ask("[bold cyan]Login[/bold cyan]")
    senha = getpass("Senha: ")
    
    # Verifica se o login e senha estão corretos
    user = usuarios.get(login)
    if user and user.senha == senha:
        console.print("[bold green]Login bem-sucedido![/bold green]")
        USUARIO_LOGADO = user
    else:
        console.print("[bold red]Usuário ou senha incorretos![/bold red]")

# Função que permite o cadastro de um novo usuário
def cadastrar_usuario(usuarios, arquivo_csv):
    global USUARIO_LOGADO
    console.print(Panel('Cadastro de Novo Usuário', title="Novo Usuário", expand=False))
    
    login = Prompt.ask("[bold cyan]Login[/bold cyan]")
    senha = getpass("Senha: ")

    # Verifica se é o primeiro usuário a ser cadastrado (será admin) ou se um admin está logado
    if len(usuarios) == 0:
        tipo = 'admin'
        console.print("[bold green]Criando primeiro usuário como Administrador.[/bold green]")
    elif USUARIO_LOGADO and USUARIO_LOGADO.tipo == 'admin':
        tipo = Prompt.ask("[bold cyan]Tipo de usuário (admin/cliente)[/bold cyan]", choices=['admin', 'cliente'])
    else:
        tipo = 'cliente'

    # Verifica se o login já existe
    if login in usuarios:
        console.print(f"[bold red]Erro: Usuário '{login}' já existe![/bold red]")
    else:
        # Adiciona o novo usuário no arquivo e no dicionário de usuários
        with open(arquivo_csv, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([login, senha, tipo])
        console.print(f"[bold green]Usuário '{login}' cadastrado com sucesso![/bold green]")
        usuarios[login] = namedtuple('Usuario', ['login', 'senha', 'tipo'])(login, senha, tipo)

# Função para exibir o menu inicial do sistema
def menu_inicial():
    console.print(Panel("[bold green]Sistema de Gestão de Brinquedos[/bold green]\nEscolha uma das opções abaixo:", title="Menu Inicial", expand=False))
    console.print("[bold cyan]1.[/bold cyan] Fazer Login")
    console.print("[bold cyan]2.[/bold cyan] Cadastro")
    console.print("[bold cyan]3.[/bold cyan] Sair")
    
    # Retorna a opção escolhida pelo usuário
    opcao = Prompt.ask("[bold yellow]Digite a opção desejada[/bold yellow]", choices=["1", "2", "3"])
    return opcao

##################### Funções de produto #####################

# Função que lê os dados dos produtos de um arquivo CSV
def ler_produtos(arquivo_csv):
    Produto = namedtuple('Produto', ['nome', 'preco', 'quantidade'])
    produtos = {}
    try:
        # Abre o arquivo de produtos no modo de leitura
        with open(arquivo_csv, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                nome, preco, quantidade = row
                produtos[nome] = Produto(nome=nome, preco=float(preco), quantidade=int(quantidade))
    except FileNotFoundError:
        # Se o arquivo não existir, ele é criado vazio
        open(arquivo_csv, 'w').close()
    return produtos

# Função que permite adicionar um novo produto (apenas administradores)
def adicionar_produto(produtos, arquivo_csv):
    console.print(Panel('Adicionar Novo Produto', title="Novo Produto", expand=False))
    nome = Prompt.ask("[bold cyan]Nome do Produto[/bold cyan]")
    preco = Prompt.ask("[bold cyan]Preço[/bold cyan]", convert=float)
    quantidade = Prompt.ask("[bold cyan]Quantidade em Estoque[/bold cyan]", convert=int)
    
    # Verifica se o produto já existe
    if nome in produtos:
        console.print(f"[bold red]Erro: Produto '{nome}' já existe![/bold red]")
    else:
        # Adiciona o novo produto ao arquivo e ao dicionário de produtos
        with open(arquivo_csv, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nome, preco, quantidade])
        console.print(f"[bold green]Produto '{nome}' adicionado com sucesso![/bold green]")
        produtos[nome] = namedtuple('Produto', ['nome', 'preco', 'quantidade'])(nome, preco, quantidade)

# Função para listar todos os produtos cadastrados
def listar_produtos(produtos):
    console.print(Panel("[bold green]Lista de Produtos[/bold green]", expand=False))
    if produtos:
        for nome, produto in produtos.items():
            console.print(f"[bold white]{nome}[/bold white] - Preço: R$ {produto.preco} - Estoque: {produto.quantidade}")
    else:
        console.print("[bold red]Nenhum produto cadastrado![/bold red]")

##################### Fluxo Principal #####################

# Carrega os usuários e produtos dos arquivos CSV
usuarios = ler_usuarios(ARQUIVO_USUARIOS)
produtos = ler_produtos(ARQUIVO_PRODUTOS)

# Loop principal do sistema
while True:
    opcao = menu_inicial()
    
    if opcao == "1":
        # Se o usuário fizer login com sucesso, mostra as opções de acordo com o tipo de usuário
        fazer_login(usuarios)
        if USUARIO_LOGADO:
            while True:
                # Menu para administradores
                if USUARIO_LOGADO.tipo == 'admin':
                    console.print("[bold cyan]1.[/bold cyan] Adicionar Produto")
                    console.print("[bold cyan]2.[/bold cyan] Listar Produtos")
                    console.print("[bold cyan]3.[/bold cyan] Sair")
                    opcao_admin = Prompt.ask("[bold yellow]Digite a opção desejada[/bold yellow]", choices=["1", "2", "3"])
                    if opcao_admin == "1":
                        adicionar_produto(produtos, ARQUIVO_PRODUTOS)
                    elif opcao_admin == "2":
                        listar_produtos(produtos)
                    elif opcao_admin == "3":
                        break
                # Menu para clientes
                else:
                    console.print("[bold cyan]1.[/bold cyan] Listar Produtos")
                    console.print("[bold cyan]2.[/bold cyan] Sair")
                    opcao_cliente = Prompt.ask("[bold yellow]Digite a opção desejada[/bold yellow]", choices=["1", "2"])
                    if opcao_cliente == "1":
                        listar_produtos(produtos)
                    elif opcao_cliente == "2":
                        break
    elif opcao == "2":
        # Cadastra um novo usuário
        cadastrar_usuario(usuarios, ARQUIVO_USUARIOS)
    elif opcao == "3":
        # Sai do sistema
        break
