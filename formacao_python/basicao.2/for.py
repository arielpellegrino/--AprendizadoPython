#for x in range(20,5, -5):
 #   print()


#texto = "123456789"

#for x in range(0,len(texto)):
    #print(texto[x])

letra = input("Digite uma letra: ")
texto = input("Digite um texto: ")

for i in range(0, len(texto)):
    if letra ==  texto[i]:
        print("Entrei a letra %s na posição %d " % (letra, i))