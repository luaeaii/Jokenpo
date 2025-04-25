# Trabalho Jokenpô - Luana Vendramini, Geovanna Karolyne Javé Soto, Clara Amazonas Pereira da Costa
import random #Importa jogadas aleatórias
while True:
# Mostra o menu de escolha de modo de jogo.
    print("Selecione o modo de jogo que deseja")
    print("======Joken Po======")
    print("1. Humano V.S Humano")
    print("2. Humano V.S Computador")
    print("3. Computador V.S Computador")
    print("4. Sair")
    print("=====================") 

    # Usuário escolhe o modo de jogo.
    modoJogo = int(input("Qual você deseja jogar? "))

    # Verifica o modo de jogo escolhido pelo usuário, no caso 1 (Humano V.S Humano).
    if modoJogo == 1:
        print("======Humano V.S Humano======")
        print("1. Pedra")
        print("2. Papel")
        print("3. Tesoura")
        print("==============================")

        # Usuários podem adicionar seus nomes.
        nome1 = input("Qual seu nome, jogador 1?: ")
        nome2 = input("Qual seu nome, jogador 2? ")
    
        # Contagem de pontos e rounds.
        ponto1 = 0
        ponto2 = 0
        rodada = 1
    
        # Loop das partidas enquanto quiserem jogar.
        while True:
            print("Rodada número " + str(rodada) + ". O jogo vai começar!")

            # Pega a jogada dos jogadores.
            jogador1 = input(nome1 + ", escolha sua jogada! Pedra = 1 , Papel = 2, Tesoura = 3 : ").strip()
            jogador2 = input(nome2 + ", escolha sua jogada! (Tente não olhar a jogada do adversário) Pedra = 1 , Papel = 2, Tesoura = 3 : ").strip()

            # Verifica se ambas as jogadas foram iguais (empate).
            if jogador1 == jogador2:
                print("Parece que houve um empate, ninguém ganha ponto :c")
                rodada += 1

            # Verifica se o jogador 1 ganhou, com todas as combinações que existem dentro do jogo.
            elif (jogador1 == "1" and jogador2 == "3") or (jogador1 == "2" and jogador2 == "1") or (jogador1 == "3" and jogador2 == "2"):
                print("======================")
                print(nome1 + " venceu esse round!")
                ponto1 += 1 # Dá 1 ponto o jogador 1.
                rodada += 1

                #Exibe o placar.
                print("=======Placar=========")
                print(nome1 + ": " + str(ponto1))
                print(nome2 + ": " + str(ponto2))
                print("=======================")

            # Verifica se o jogador 2 ganhou.
            elif (jogador2 == "1" and jogador1 == "3") or (jogador2 == "2" and jogador1 == "1") or (jogador2 == "3" and jogador1 == "2"):
                print("======================")
                print(nome2 + " venceu esse round!")
                ponto2 += 1 # Dá 1 ponto o jogador 2.
                rodada += 1

                #Exibe o placar.
                print("=======Placar=========")
                print(nome1 + ": " + str(ponto1))
                print(nome2 + ": " + str(ponto2))
                print("=======================")

            # Se alguém digitar errado ou qualquer outra coisa ele invalida o round e retorna.
            else:
                print("Parece que houve um erro ou alguma jogada foi inválida, tente de novo!")
                continue # Retorna ao jogo.

            continuar = input("Desejam continuar o jogo? (Sim/Não): ").strip().lower()

            # Verifica se não querem mais jogar.
            if continuar != "sim": 
                print("======= Placar Final =======")
                print(nome1 + ": " + str(ponto1))
                print(nome2 + ": " + str(ponto2))
                print("============================")
                print("Esse jogo foi feito por Luana Vendramini, Geovanna Karolyne Javé Soto, Clara Amazonas Pereira da Costa.")
                break # Sai do while

    # Verifica o modo de jogo escolhido pelo usuário, no caso 2 (Humano V.S Computador).
    elif modoJogo == 2:
        placar_humano = 0
        placar_computador = 0

        while True:
            # Menu de opções
            print("====== Bem-vindo ao Jokenpô - Humano V.S Computador ======")
            print("Escolha sua jogada:")
            print("1 - Pedra")
            print("2 - Papel")
            print("3 - Tesoura")
            print("==============================")
            # Recebe a jogada do jogador
            jogada_humano = input("Digite o número da sua jogada: ").strip()

            # Verifica se a jogada é válida (1, 2 ou 3)
            if jogada_humano in ["1", "2", "3"]:
                # Converte para número inteiro
                jogada_humano = int(jogada_humano)
                # Computador escolhe aleatoriamente (1, 2 ou 3)
                jogada_computador = random.randint(1, 3)

                # Mostra a jogada do humano em texto
                if jogada_humano == 1:
                    print("\nVocê escolheu: Pedra")
                elif jogada_humano == 2:
                    print("\nVocê escolheu: Papel")
                else:
                    print("\nVocê escolheu: Tesoura")

                # Mostra a jogada do computador em texto
                if jogada_computador == 1:
                    print("O computador escolheu: Pedra")
                elif jogada_computador == 2:
                    print("O computador escolheu: Papel")
                else:
                    print("O computador escolheu: Tesoura")

                # Verifica quem ganhou
                if jogada_humano == jogada_computador:
                    print("\nEmpate!")
                elif (jogada_humano == 1 and jogada_computador == 3) or \
                    (jogada_humano == 2 and jogada_computador == 1) or \
                    (jogada_humano == 3 and jogada_computador == 2):
                    print("\nVocê venceu!")
                    placar_humano += 1 # Aumenta o placar do jogador
                else:
                    print("\nO computador venceu!")
                    placar_computador += 1 # Aumenta o placar do computador

                # Mostra o placar atual
                print(f"\n======= Placar atual - Você: {placar_humano} x Computador: {placar_computador} =======")

                # Pergunta se quer continuar
                continuar = input("\nDeseja jogar novamente? (Sim/Não): ").strip().lower()
                if continuar != "sim":
                    break # Sai do loop
            else:
                # Mensagem de erro para jogada inválida
                print("\nJogada inválida! Digite 1, 2 ou 3.")

        # Placar final e mensagem de agradecimento
        print("\n======= Resultado Final =======")
        print(f"Você: {placar_humano} vitórias")
        print(f"Computador: {placar_computador} vitórias")
        print("==============================")
        print("Trabalho feito por: Luana Vendramini, Geovanna Karolyne Javé Soto, Clara Amazonas Pereira da Costa")


    # Verifica o modo de jogo escolhido pelo usuário, no caso 3 (Computador V.S Computador).
    elif modoJogo == 3:
        
    # Inserir dentro do menu principal -> cp1_vitorias, cp2_vitorias e rodada ficam fora do loop, se forem colocadas pra dentro do while o valor sempre volta a ser 0

        cp1_vitorias = 0
        cp2_vitorias = 0
        rodada = 1

        while True:
            print("---------------------------------------------------")
            print(f"\nRodada: {rodada}")
            print(f"CPU1 Vitorias: {cp1_vitorias}")
            print(f"CPU2 Vitorias: {cp2_vitorias}")
            
            # Random sorteia um numero entre 1 e 3 e depois o if e else tranforma o numero correspondente em uma jogada

            cp1_jogada = random.randint(1, 3)

            if cp1_jogada == 1:
                cp1_jogada = "Pedra"
            elif cp1_jogada == 2:
                cp1_jogada = "Papel"
            else:
                cp1_jogada = "Tesoura"

            cp2_jogada = random.randint(1, 3)

            if cp2_jogada == 1:
                cp2_jogada = "Pedra"
            elif cp2_jogada == 2:
                cp2_jogada = "Papel"
            else:
                cp2_jogada = "Tesoura"


            print(f"\nCPU1 Jogada: {cp1_jogada}")
            print(f"CPU2 Jogada: {cp2_jogada}")
            print("\n---------------------------------------------------")

            # Aqui estão as condições de vitoria da RODADA

            if cp1_jogada == "Papel" and cp2_jogada == "Pedra":
                print("CPU1 Venceu!")
                cp1_vitorias += 1
            elif cp1_jogada == "Pedra" and cp2_jogada == "Tesoura":
                print("CPU1 Venceu!")
                cp1_vitorias += 1
            elif cp1_jogada == "Tesoura" and cp2_jogada == "Papel":
                print("CPU1 Venceu!")
                cp1_vitorias += 1
            elif cp1_jogada == cp2_jogada:
                print("Empate!")
            else:
                print("CPU2 Venceu!")
                cp2_vitorias += 1

            # Aqui estão as condições de vitoria do JOGO (melhor de 3)

            if cp1_vitorias == 2:
                print("---------------------------------------------------")
                print(f"CPU1 Vitorias: {cp1_vitorias}")
                print(f"CPU2 Vitorias: {cp2_vitorias}")
                print("CPU1 Venceu o Jogo!")
                print("---------------------------------------------------")
                break
            elif cp2_vitorias == 2:
                print("---------------------------------------------------")
                print("--- Resultado Final ---")
                print(f"CPU1 Vitorias: {cp1_vitorias}")
                print(f"CPU2 Vitorias: {cp2_vitorias}")
                print("\nCPU2 Venceu o Jogo!")
                print("---------------------------------------------------")
                print("Obrigada por assistir")
                print("Trabalho feito por: Luana Vendramini, Clara Amazonas e Geovanna Karolyne")
                break

            rodada += 1
    elif modoJogo == 4:
        print("===========================")
        print("Obrigada por testar nosso jogo!")
        print("===========================")
        break