
interacao = 10
while(interacao > 0):
    print(interacao)
    interacao-= 1
    
indice = 10
print("programa") 
while(indice >= 2):
    resto = (indice % 2)
    if resto == 0:
        print("O número %d e par" % (indice))
    else:
        print("O numero %d é impar" % (indice))
    indice -= 1
print("Programa finalizado")

soma = 0
numeros_lidos = 0


while (numeros_lidos < 5):
    num_str = input("Digite um numero: ")
    num_lido = float(num_str)
    soma += num_lido
    numeros_lidos += 1

print("A soma é %.2f " % soma)


texto = "Olá 123 _"
indice = 0
while indice < len(texto):
    print(texto[indice])
    indice += 1

    altura = 5
    linha = 0

    while linha < altura:
        espacos = altura - linha - 1
        estrelas = 2 * linha + 1
        print(' ' * espacos + "*" * estrelas)
        linha += 1