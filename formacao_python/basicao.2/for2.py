letra = input("Digite uma letra: ")

if(len(letra) != 1):
    print("Precisa ter um digito")
else:
    texto = input("Digite um texto: ")
    for i in range(0, len(texto)):
        if letra == texto[i]:
            print("Encontrei a letra %s na posição %d " % (letra, i))
            