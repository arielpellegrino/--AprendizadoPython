#numero = 1
#if numero ==1 or numero ==0:
    #print("É 1 ou 0")


numero = 11


if numero > 0:
    print("maior que 0")
    if numero > 10:
        print("Numero é maior que 10")
        if numero > 11:
            print("maior que 11")
            
number = 10
if numero > 0:
    print("A")
elif numero <100:
    print("B")
elif numero <= 1000:
    print("C")
else:
    print("X")
    
# Ternário

numero = 10
result = "PAR" if numero % 2 == 0 else "IMPAR"
print(result)
