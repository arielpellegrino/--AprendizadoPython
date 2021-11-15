import random


print("***********************************")
print("Bem vindo ao jogos de adivinhação")
print("***********************************")

#Declaração de numeros
numero_secreto = round(random.randrange(1, 101, 1))
total_de_tentativas = 3

print (numero_secreto)


for rodada in range (1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas)) # O .format se chama String interpolation
    chute_Str = input("Digite o seu numero: ")
    print("Você digitou", chute_Str)
    chute = int(chute_Str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um numero entre 1 e 100")
        continue


    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou! Seu chhute foi maior do que o numero secreto.")
        elif (menor):
            print("Você errou! Seu chute foi menor do que o numero secreto.")


print("##### Fim do jogo. #####")
