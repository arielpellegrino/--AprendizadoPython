### NUMEROS
#inteiros INT
idade = 25
numero_negativo = -10
numero_grande = 10000000000

#float "decimais"
altura = 1.80
temperatura = -5.5
pi = 3.14159

### Complex "numeros complexos"
numero_complexo = 3 + 4j
outro_complexo = complex(2,5) # 2 + 5j


### Strings
nome = "Ariel"
frase = "amo python"

###Boolean
verdadeiro = true
false = false

### Tipos de sequência
#list --> Mutaveis
frutas = ["maçã", "banana", "laranja"]
numeros = [1,2,3,4,5]
misto = [1, "texto", true, 3.14]

#tuple --> imutaveis
coordenada = (10, 20)
cores_rgb= (255, 128, 0)
dados_pessoa = ("Ana", 30, "ti")

#range --> Sequência de numeros
numeros = range(5) # 0, 1,2,3,4,5
range_intervalo = range(1, 10, 2) # 1,3,5,7,9



### Tipos de mapeamento
#dict --> Dicionario

pessoa = {
    "nome": "carlos",
    "idade":28,
    "profissao": "desenvolvedor"
}

#set "conjuntos - mutaveis
numeros_unicos = {1,2,3,4,5}
frutas_set = {"maçã", "banana", "pera"}

#frozenset (conjunto imutaveis
conjunto_imutavel = frozenset([1,2,3,4])

###Tipos especiais
#noneType = valor nulo

resultado = None
valor_vazio = None

#bytes - sequeência de bytes

dados_binarios = b"Hello"
bytes_array = bytes([65, 66, 67])
