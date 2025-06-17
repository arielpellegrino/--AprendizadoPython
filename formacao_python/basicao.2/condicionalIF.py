



if (True):
    print("Dentro do IF")
    
print("Fora do IF")

if(False):
    print("Este codigo nao vai ser executado")
    
if(True):
    pass

valor1 = 10
valor2 = 10
sao_iguais = (valor1 == valor2)

if(sao_iguais):
    print("São iguais", sao_iguais)
else:
    print(sao_iguais)
    
nome = "Ariel"
if "A" in nome:
    print("possui letra a")
    
name = input("Digite seu nome: ")
possui_vogal = ("a" in name) or ("e" in nome)

if possui_vogal:
    print("Possui!")