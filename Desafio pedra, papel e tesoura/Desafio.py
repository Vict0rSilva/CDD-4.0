placar_jogador1 = 0
placar_jogador2 = 0

while placar_jogador1 < 3 and placar_jogador2 < 3:
    print("Escolha: pedra, papel ou tesoura")
    jogador1_escolha = input("Jogador 1: ").lower()
    jogador2_escolha = input("Jogador 2: ").lower()

    if jogador1_escolha not in ["pedra", "papel", "tesoura"] or jogador2_escolha not in ["pedra", "papel", "tesoura"]:
        print("Escolha inválida. escolha entre pedra, papel ou tesoura.")
        continue

    if jogador1_escolha == jogador2_escolha:
            print("Empate nesta rodada!")
    elif ((jogador1_escolha == "pedra" and jogador2_escolha == "tesoura") or (jogador1_escolha == "papel" and jogador2_escolha == "pedra") or (jogador1_escolha == "tesoura" and jogador2_escolha == "papel")):
        print("Jogador 1 venceu esta rodada!")
        placar_jogador1 += 1
    else:
        print("Jogador 2 venceu esta rodada!")
        placar_jogador2 += 1

    print(f"Placar: Jogador 1 ({placar_jogador1}) - Jogador 2 ({placar_jogador2})\n")

if placar_jogador1 > placar_jogador2:
    print("Jogador 1 venceu o jogo!")
else:
    print("Jogador 2 venceu o jogo!")
