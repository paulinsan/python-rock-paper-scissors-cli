import random

# Opções disponíveis no jogo
opcoes = ["Pedra ⛰️", "Papel 📄", "Tesoura ✂️"]

# Função para escolher a jogada do jogador
def escolher_opcao():

    # Loop para voltar validação da escolha do jogador
        while True:
    
            try:
                # Tenta converter a entrada para número inteiro    
                jogador = int(input("Você escolhe pedra, papel ou tesoura??? "))
    
                if jogador == 1:
                    return "Pedra ⛰️"
    
    
                elif jogador == 2:
                    return "Papel 📄"
    
    
                elif jogador == 3:
                    return "Tesoura ✂️"
    
    
                else:
                    print("❌ Opção inválida! Por favor, escolha entre 1, 2 ou 3. ")
    
            except ValueError:
                # Executa quando o jogador digita algo que não é número
                print("❌ Opção inválida! Por favor, escolha entre 1, 2 ou 3. ")

# Função para verificar quem venceu
def verificar_vencedor(jogador, computador):

    if jogador == computador:
        return "empate"

    elif jogador == "Pedra ⛰️" and computador == "Tesoura ✂️":
        return "jogador"

    elif jogador == "Papel 📄" and computador == "Pedra ⛰️":
        return "jogador"

    elif jogador == "Tesoura ✂️" and computador == "Papel 📄":
        return "jogador"

    else:
        return "computador"

# Função para mostrar a pontuação atual

def mostrar_placar(placar):

    print(f"""
Rodadas:    {placar["rodadas"]}
Você:       {placar["jogador"]}
Computador: {placar["computador"]}
Empates:    {placar["empates"]}
""")

# Função de validação se o jogador deseja jogar novamente
def jogar_novamente():

    # Continua perguntando até receber S ou N
    while True: 
        resposta = input("Deseja jogar novamente? [S/N]: ").lower()

        # True significa que vai continuar
        if resposta == "s":
            return True
        
        # False significa que vai encerrar
        elif resposta == "n":
            return False

        # Trata respostas diferentes de S ou N
        else:
            print("❌ Opção inválida! Por favor, Digite 'S' para sim ou 'N' para não. ")

# Função para mostrar o resultado final
def mostrar_resultado_final(placar):

    if placar["jogador"] > placar["computador"]:

        print("🏆 Você venceu a partida! 🏆")

    elif placar["jogador"] < placar["computador"]:

        print("😓 Você perdeu a partida! 😓")

    else:

        print("👀 A partida terminou empatada! 👀")

# Pontuação inicial
placar = {
    "jogador": 0,
    "computador": 0,
    "empates": 0,
    "rodadas": 0
}

# Loop principal do jogo
while True:

    # Computador escolhe uma opção aleatória 
    computador = random.choice(opcoes)

    print('''
\n===== PEDRA, PAPEL OU TESOURA??? =====
[1] Pedra ⛰️
[2] Papel 📄
[3] Tesoura ✂️
''')

    # Jogador faz sua escolha através da função
    jogador = escolher_opcao()

    # Mostra as rodadas 
    placar["rodadas"] += 1

    # Mostra as escolhas de ambos
    print(f"Você escolheu: {jogador}")
    print(f"Seu adversário escolheu: {computador}")

    # Verifica quem venceu
    resultado = verificar_vencedor(jogador, computador)

    # Mostra o resultado e atualiza a pontuação
    if resultado == "empate":

        print("👀 Empate! 👀")

        # Marca quantos empates teve na rodada
        placar["empates"] += 1

    elif resultado == "jogador":

        print("🏆 Você venceu! 🏆")

        # Adiciona 1 ponto ao jogador
        placar["jogador"] += 1

    else:

        print("😓 Você perdeu! 😓")

        # Adiciona 1 ponto ao computador
        placar["computador"] += 1

    # Mostra o placar atual
    print("\n===== PLACAR ATUAL =====")
    mostrar_placar(placar)

    # Pergunta se o jogador quer continuar
    if not jogar_novamente():

        # Mostra a pontuação final
        print("\n===== PLACAR FINAL =====")
        mostrar_placar(placar)
        mostrar_resultado_final(placar)
        print("Encerrando o jogo. . . ")
        break