print("***********************************")
print("Bem vindo ao jogos de adivinhação")
print("***********************************")

#Declaração de numeros
numero_secreto = 42
total_de_tentativas = 3
rodada = 1


while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas)) # O .format se chama String interpolation
    chute_Str = input("Digite o seu numero: ")
    print("Você digitou", chute_Str)
    chute = int(chute_Str)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
    else:
        if (maior):
            print("Você errou! Seu chhute foi maior do que o numero secreto.")
        elif (menor):
            print("Você errou! Seu chute foi menor do que o numero secreto.")

    rodada = rodada + 1


print("##### Fim do jogo. #####")
