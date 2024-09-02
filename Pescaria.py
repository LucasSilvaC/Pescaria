import random

# Códigos ANSI para cores
RED = "\033[91m"
RESET = "\033[0m"

linhas = int(input("Quantas linhas você quer ter no seu jogo? \n"))
colunas = int(input("Quantas colunas você quer ter no seu jogo? \n"))

def gerar_matriz(linhas, colunas):
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # Cria a matriz de acordo com o formato desejado
    matriz = [[f"{letras[i]}{j+1}" for i in range(linhas)] for j in range(colunas)]
    return matriz

def exibir_matriz(matriz, item_correto=None):
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Lista de letras
    # Exibir cabeçalho de números de colunas
    print("   ", end="")  # Espaço inicial para alinhar o cabeçalho
    for i in range(len(matriz[0])):  # len retorna o número de colunas em um objeto
        print(f"{i+1} ", end="")  # Usa os números das colunas no cabeçalho
    print()

    # Exibir linhas com letras
    for i, linha in enumerate(matriz):  # enumerate para arrumar o conjunto de linhas
        print(f"{letras[i]} ", end="")  # Adiciona a letra da linha
        for item in linha:
            if item == item_correto:
                print(f"{RED}{item}{RESET} ", end="")  # Destaca o item em vermelho
            else:
                print(f"{item} ", end="")  # Exibe cada item na linha
        print()  # Quebra de linha

def jogar():
    matriz = gerar_matriz(linhas, colunas)
    
    # Exibir a matriz para o jogador
    print("Tabuleiro de jogo:")
    exibir_matriz(matriz)
    
    elementos = []
    for linha in matriz:
        for pos in linha:  # pos de position
            elementos.append(pos)  # Usado para acrescentar um item final a uma lista
    
    print("Olá! Seja bem-vindo à batalha naval!\n")
    
    tent = int(input("Quantas tentativas você quer ter no seu jogo? \n"))
    qntdpeixe = int(input("Quantos peixes precisam ser descobertos? \n"))
    
    # Escolher as posições dos peixes aleatoriamente
    peixes = random.sample(elementos, qntdpeixe)
    
    print(f"\nTente adivinhar onde os {qntdpeixe} peixes estão escondidos!")
    
    # Usuário
    pontos_user = 0
    while tent > 0:
        print(f"Tentativas restantes: {tent}")
        tent_usuario = input("Digite a coordenada: ").upper()  # Convertendo para maiúsculas
    
        if tent_usuario in peixes:
            print("Parabéns! Você acertou onde está um navio!")
            pontos_user += 1
            peixes.remove(tent_usuario)
            # Exibir a matriz com o item digitado em vermelho
            exibir_matriz(matriz, item_correto=tent_usuario)
            if not peixes:
                print(f"Você encontrou todos os peixes! Total de pontos: {pontos_user}")
                break
        else:
            tent -= 1
            print(f"Você errou! Tentativas restantes: {tent}")
    
        if tent == 0:
            print("Você perdeu! Todas as tentativas foram usadas.")
    
    if tent > 0 and peixes:
        print("Ainda restaram peixes a serem encontrados:", peixes)

    # Máquina
    tent_mac = int(input("\nQuantas tentativas a máquina deve ter? \n"))
    peixes_mac = random.sample(elementos, qntdpeixe)
    
    pontos_mac = 0
    print("\nAgora é a vez da máquina!")
    
    while tent_mac > 0:
        tent_mac_num = random.choice(elementos)
        print(f"A máquina tentou a coordenada: {tent_mac_num}")  # Adicionado para exibir a coordenada
    
        if tent_mac_num in peixes_mac:
            print(f"A máquina acertou onde está um navio! {tent_mac_num}")
            pontos_mac += 1
            peixes_mac.remove(tent_mac_num)
            if not peixes_mac:
                print(f"A máquina encontrou todos os peixes! Total de pontos: {pontos_mac}")
                break
        else:
            tent_mac -= 1
            print(f"A máquina errou! Tentativas restantes: {tent_mac}")
    
        if tent_mac == 0:
            print("A máquina perdeu! Todas as tentativas foram usadas.")
    
    if tent_mac > 0 and peixes_mac:
        print("Ainda restaram peixes a serem encontrados pela máquina:", peixes_mac)

    # Ganhador
    if pontos_mac == pontos_user:
        print("Houve um empate!")

    elif pontos_mac > pontos_user:
        print("A máquina ganhou!")
    else:
        print("Você ganhou!")

def clear():
    print("\n" * 100)  # Simula a limpeza da tela ao imprimir 100 novas linhas

while True:
    clear()
    jogar()
    jogar_novamente = input("Você quer jogar novamente? (sim/nao): ")
    if jogar_novamente.lower() != 'sim':
        print("Obrigado por jogar!")
        break