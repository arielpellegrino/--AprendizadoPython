# 🐍 Roadmap Python: Júnior para Pleno em 6 Meses

## 📋 Objetivo
Evoluir de desenvolvedor Python júnior para pleno em 6 meses através de estudo estruturado e prática consistente.

---

# Roadmap Completo de Python - Do Básico ao Avançado

## 📚 Nível 1: Fundamentos Básicos

### 1.1 Sintaxe Básica e Variáveis
**Conceito**: Python usa indentação para definir blocos de código e não precisa de ponto e vírgula.

```python
# Variáveis e tipos básicos
nome = "João"
idade = 25
altura = 1.75
ativo = True

print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}m")
```

### 1.2 Tipos de Dados Primitivos
**Conceito**: Python tem tipos dinâmicos - int, float, str, bool.

```python
# Verificando tipos
numero = 42
print(type(numero))  # <class 'int'>

# Conversão de tipos
idade_str = "25"
idade_int = int(idade_str)
print(f"Idade como inteiro: {idade_int}")
```

### 1.3 Operadores
**Conceito**: Operadores aritméticos, de comparação e lógicos.

```python
# Operadores aritméticos
a, b = 10, 3
print(f"Soma: {a + b}")
print(f"Divisão inteira: {a // b}")
print(f"Módulo: {a % b}")
print(f"Potência: {a ** b}")

# Operadores de comparação e lógicos
x, y = 5, 10
resultado = (x < y) and (x > 0)
print(f"Resultado lógico: {resultado}")
```

### 1.4 Entrada e Saída de Dados
**Conceito**: Interação com o usuário através de input() e print().

```python
# Entrada de dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Saída formatada
print(f"Olá {nome}, você tem {idade} anos!")
print("Você nasceu em aproximadamente", 2024 - idade)
```

## 📋 Nível 2: Estruturas de Controle

### 2.1 Condicionais (if, elif, else)
**Conceito**: Controle de fluxo baseado em condições.

```python
nota = 85

if nota >= 90:
    conceito = "A"
elif nota >= 80:
    conceito = "B"
elif nota >= 70:
    conceito = "C"
else:
    conceito = "D"

print(f"Nota: {nota}, Conceito: {conceito}")
```

### 2.2 Loops - for
**Conceito**: Iteração sobre sequências ou intervalos.

```python
# Loop com range
for i in range(5):
    print(f"Número: {i}")

# Loop com lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(f"Fruta: {fruta}")

# Loop com enumerate
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")
```

### 2.3 Loops - while
**Conceito**: Repetição baseada em condição.

```python
# Contador simples
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

# Loop com validação
senha = ""
while senha != "123456":
    senha = input("Digite a senha: ")
    if senha != "123456":
        print("Senha incorreta!")

print("Acesso liberado!")
```

### 2.4 Controle de Loop (break, continue, pass)
**Conceito**: Palavras-chave para controlar a execução de loops.

```python
# break - sair do loop
for i in range(10):
    if i == 5:
        break
    print(i)

# continue - pular iteração
for i in range(5):
    if i == 2:
        continue
    print(i)

# pass - placeholder
for i in range(3):
    if i == 1:
        pass  # TODO: implementar lógica aqui
    else:
        print(i)
```

## 🗂️ Nível 3: Estruturas de Dados

### 3.1 Listas
**Conceito**: Coleção ordenada e mutável de elementos.

```python
# Criação e manipulação de listas
numeros = [1, 2, 3, 4, 5]
numeros.append(6)
numeros.insert(0, 0)
print(numeros)  # [0, 1, 2, 3, 4, 5, 6]

# Slicing
print(numeros[1:4])  # [1, 2, 3]
print(numeros[::-1])  # Lista invertida

# List comprehension
pares = [x for x in numeros if x % 2 == 0]
print(f"Números pares: {pares}")
```

### 3.2 Tuplas
**Conceito**: Coleção ordenada e imutável de elementos.

```python
# Criação de tuplas
coordenadas = (10, 20)
pessoa = ("João", 25, "Desenvolvedor")

# Desempacotamento
nome, idade, profissao = pessoa
print(f"{nome} tem {idade} anos e é {profissao}")

# Tuplas nomeadas
from collections import namedtuple
Pessoa = namedtuple('Pessoa', ['nome', 'idade', 'profissao'])
p = Pessoa("Maria", 30, "Designer")
print(f"{p.nome} - {p.idade} anos")
```

### 3.3 Dicionários
**Conceito**: Coleção de pares chave-valor, não ordenada e mutável.

```python
# Criação e manipulação
pessoa = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}

# Acesso e modificação
pessoa["profissao"] = "Desenvolvedor"
pessoa["idade"] = 26

# Métodos úteis
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

# Dictionary comprehension
quadrados = {x: x**2 for x in range(5)}
print(quadrados)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### 3.4 Conjuntos (Sets)
**Conceito**: Coleção de elementos únicos, não ordenada.

```python
# Criação de sets
frutas = {"maçã", "banana", "laranja", "maçã"}  # Remove duplicatas
print(frutas)  # {'banana', 'laranja', 'maçã'}

# Operações de conjunto
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"União: {set1 | set2}")
print(f"Interseção: {set1 & set2}")
print(f"Diferença: {set1 - set2}")
print(f"Diferença simétrica: {set1 ^ set2}")
```

## 🔧 Nível 4: Funções

### 4.1 Definição e Chamada de Funções
**Conceito**: Blocos de código reutilizáveis que executam tarefas específicas.

```python
# Função simples
def saudacao(nome):
    return f"Olá, {nome}!"

# Função com múltiplos parâmetros
def calcular_area_retangulo(largura, altura):
    return largura * altura

# Chamadas
print(saudacao("Maria"))
area = calcular_area_retangulo(5, 3)
print(f"Área: {area}")
```

### 4.2 Parâmetros e Argumentos
**Conceito**: Diferentes formas de passar dados para funções.

```python
# Parâmetros padrão
def criar_perfil(nome, idade=18, cidade="São Paulo"):
    return f"{nome}, {idade} anos, {cidade}"

# Argumentos posicionais e nomeados
print(criar_perfil("João"))
print(criar_perfil("Maria", cidade="Rio de Janeiro", idade=25))

# *args e **kwargs
def funcao_flexivel(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

funcao_flexivel(1, 2, 3, nome="João", idade=25)
```

### 4.3 Escopo de Variáveis
**Conceito**: Visibilidade e acesso de variáveis em diferentes contextos.

```python
# Variável global
contador_global = 0

def incrementar():
    global contador_global
    contador_global += 1
    
    # Variável local
    contador_local = 10
    return contador_local

# Exemplo de escopo
def externa():
    x = 10
    
    def interna():
        nonlocal x
        x += 5
        return x
    
    return interna()

print(externa())  # 15
```

### 4.4 Funções Lambda
**Conceito**: Funções anônimas de uma linha.

```python
# Lambda básica
quadrado = lambda x: x ** 2
print(quadrado(5))  # 25

# Lambda com múltiplos argumentos
soma = lambda x, y: x + y
print(soma(3, 7))  # 10

# Uso com map, filter, sorted
numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x**2, numeros))
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(f"Quadrados: {quadrados}")
print(f"Pares: {pares}")
```

## 📦 Nível 5: Módulos e Pacotes

### 5.1 Importação de Módulos
**Conceito**: Reutilização de código através de módulos.

```python
# Importações básicas
import math
from datetime import datetime
from random import randint, choice

# Usando módulos
print(math.pi)
print(math.sqrt(16))

agora = datetime.now()
print(f"Agora: {agora}")

numero_aleatorio = randint(1, 100)
fruta_aleatoria = choice(["maçã", "banana", "laranja"])
print(f"Número: {numero_aleatorio}, Fruta: {fruta_aleatoria}")
```

### 5.2 Criação de Módulos Próprios
**Conceito**: Organização do código em arquivos separados.

```python
# arquivo: calculadora.py
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

PI = 3.14159

# arquivo: main.py
# from calculadora import somar, PI
# import calculadora as calc

# resultado = somar(5, 3)
# area_circulo = PI * calc.multiplicar(raio, raio)
```

### 5.3 Pacotes
**Conceito**: Organização de módulos em diretórios.

```python
# Estrutura de diretórios:
# meu_projeto/
#   __init__.py
#   matematica/
#     __init__.py
#     operacoes.py
#     geometria.py

# Importação de pacotes
# from meu_projeto.matematica.operacoes import somar
# from meu_projeto.matematica import geometria

# Exemplo de __init__.py
# __all__ = ['somar', 'subtrair']
# from .operacoes import somar, subtrair
```

## 🛠️ Nível 6: Programação Orientada a Objetos

### 6.1 Classes e Objetos
**Conceito**: Criação de tipos personalizados de dados.

```python
class Pessoa:
    # Atributo de classe
    especie = "Homo sapiens"
    
    def __init__(self, nome, idade):
        # Atributos de instância
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        return f"Olá, eu sou {self.nome} e tenho {self.idade} anos"
    
    def fazer_aniversario(self):
        self.idade += 1
        return f"{self.nome} agora tem {self.idade} anos"

# Criando objetos
pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)

print(pessoa1.apresentar())
print(pessoa1.fazer_aniversario())
```

### 6.2 Herança
**Conceito**: Criação de classes baseadas em outras classes.

```python
class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
    
    def fazer_som(self):
        return "Som genérico de animal"

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, "Canis lupus")
        self.raca = raca
    
    def fazer_som(self):  # Sobrescrita de método
        return "Au au!"
    
    def buscar_objeto(self):
        return f"{self.nome} foi buscar o objeto!"

# Uso
rex = Cachorro("Rex", "Labrador")
print(rex.fazer_som())
print(rex.buscar_objeto())
print(f"Espécie: {rex.especie}")
```

### 6.3 Encapsulamento
**Conceito**: Controle de acesso aos atributos e métodos.

```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial  # Atributo "protegido"
        self.__numero_conta = self._gerar_numero_conta()  # Atributo "privado"
    
    def _gerar_numero_conta(self):
        import random
        return random.randint(10000, 99999)
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return f"Depósito de R${valor} realizado"
        return "Valor inválido"
    
    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            return f"Saque de R${valor} realizado"
        return "Saldo insuficiente ou valor inválido"
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero_conta(self):
        return self.__numero_conta

# Uso
conta = ContaBancaria("João", 1000)
print(conta.depositar(500))
print(f"Saldo: R${conta.saldo}")
print(f"Número da conta: {conta.numero_conta}")
```

### 6.4 Polimorfismo
**Conceito**: Diferentes classes implementando os mesmos métodos de formas diferentes.

```python
class Forma:
    def calcular_area(self):
        raise NotImplementedError("Método deve ser implementado na subclasse")

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return 3.14159 * self.raio ** 2

# Polimorfismo em ação
formas = [
    Retangulo(5, 3),
    Circulo(4),
    Retangulo(2, 8)
]

for forma in formas:
    print(f"Área: {forma.calcular_area():.2f}")
```

## 🔍 Nível 7: Manipulação de Arquivos

### 7.1 Leitura e Escrita de Arquivos
**Conceito**: Persistência de dados em arquivos.

```python
# Escrita de arquivo
def escrever_arquivo():
    with open('exemplo.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write("Primeira linha\n")
        arquivo.write("Segunda linha\n")
        
        # Escrevendo lista
        linhas = ["Terceira linha\n", "Quarta linha\n"]
        arquivo.writelines(linhas)

# Leitura de arquivo
def ler_arquivo():
    with open('exemplo.txt', 'r', encoding='utf-8') as arquivo:
        # Ler tudo
        conteudo = arquivo.read()
        print("Conteúdo completo:")
        print(conteudo)
        
        # Voltar ao início
        arquivo.seek(0)
        
        # Ler linha por linha
        print("\nLinha por linha:")
        for linha in arquivo:
            print(linha.strip())

escrever_arquivo()
ler_arquivo()
```

### 7.2 Trabalhando com JSON
**Conceito**: Serialização e deserialização de dados JSON.

```python
import json

# Dados Python para JSON
dados = {
    "nome": "João",
    "idade": 25,
    "habilidades": ["Python", "JavaScript", "SQL"],
    "ativo": True
}

# Salvando em arquivo JSON
with open('dados.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, indent=2, ensure_ascii=False)

# Lendo arquivo JSON
with open('dados.json', 'r', encoding='utf-8') as arquivo:
    dados_carregados = json.load(arquivo)
    print(dados_carregados)

# Convertendo para string JSON
json_string = json.dumps(dados, indent=2, ensure_ascii=False)
print(json_string)

# Convertendo string JSON para Python
dados_python = json.loads(json_string)
print(dados_python["habilidades"])
```

### 7.3 Manipulação de CSV
**Conceito**: Trabalho com arquivos de dados tabulares.

```python
import csv

# Escrevendo CSV
dados_funcionarios = [
    ['Nome', 'Idade', 'Departamento', 'Salário'],
    ['João', 25, 'TI', 5000],
    ['Maria', 30, 'RH', 4500],
    ['Pedro', 28, 'Vendas', 4000]
]

with open('funcionarios.csv', 'w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados_funcionarios)

# Lendo CSV
with open('funcionarios.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)

# Usando DictReader/DictWriter
with open('funcionarios.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for funcionario in leitor:
        print(f"{funcionario['Nome']} trabalha em {funcionario['Departamento']}")
```

## ⚠️ Nível 8: Tratamento de Erros

### 8.1 Try/Except
**Conceito**: Tratamento de exceções para código mais robusto.

```python
def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Erro: Divisão por zero!")
        return None
    except TypeError:
        print("Erro: Tipos inválidos para divisão!")
        return None

# Múltiplas exceções
def processar_entrada():
    try:
        numero = int(input("Digite um número: "))
        resultado = 10 / numero
        print(f"Resultado: {resultado}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Testando
print(dividir(10, 2))   # 5.0
print(dividir(10, 0))   # Erro: Divisão por zero!
print(dividir("10", 2)) # Erro: Tipos inválidos para divisão!
```

### 8.2 Finally e Else
**Conceito**: Código que sempre executa (finally) ou executa apenas sem exceções (else).

```python
def processar_arquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'r')
        conteudo = arquivo.read()
        print(f"Arquivo lido com sucesso: {len(conteudo)} caracteres")
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado!")
    except PermissionError:
        print(f"Sem permissão para ler {nome_arquivo}")
    else:
        print("Arquivo processado sem erros")
    finally:
        # Sempre executado
        try:
            arquivo.close()
            print("Arquivo fechado")
        except NameError:
            print("Arquivo não foi aberto")

processar_arquivo("arquivo_inexistente.txt")
```

### 8.3 Exceções Personalizadas
**Conceito**: Criação de tipos específicos de exceções.

```python
class IdadeInvalidaError(Exception):
    def __init__(self, idade, mensagem="Idade inválida"):
        self.idade = idade
        self.mensagem = mensagem
        super().__init__(self.mensagem)

class ContaBancariaError(Exception):
    pass

class SaldoInsuficienteError(ContaBancariaError):
    def __init__(self, saldo_atual, valor_saque):
        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque
        mensagem = f"Saldo insuficiente: R${saldo_atual}, tentativa de saque: R${valor_saque}"
        super().__init__(mensagem)

def validar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaError(idade, "Idade não pode ser negativa")
    if idade > 150:
        raise IdadeInvalidaError(idade, "Idade muito alta")
    return True

# Uso
try:
    validar_idade(-5)
except IdadeInvalidaError as e:
    print(f"Erro: {e.mensagem} (Idade: {e.idade})")
```

## 🔄 Nível 9: Iteradores e Geradores

### 9.1 Iteradores
**Conceito**: Objetos que implementam o protocolo de iteração.

```python
class ContadorRegressivo:
    def __init__(self, inicio):
        self.inicio = inicio
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.inicio <= 0:
            raise StopIteration
        self.inicio -= 1
        return self.inicio + 1

# Uso
contador = ContadorRegressivo(5)
for numero in contador:
    print(numero)

# Usando iter() com função
def contador_funcao():
    return iter(range(5, 0, -1))

for numero in contador_funcao():
    print(numero)
```

### 9.2 Geradores
**Conceito**: Funções que retornam iteradores usando yield.

```python
def fibonacci(n):
    """Gera os primeiros n números da sequência de Fibonacci"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Uso
fib = fibonacci(10)
print(list(fib))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Gerador infinito
def numeros_pares():
    numero = 0
    while True:
        yield numero
        numero += 2

# Uso com next()
pares = numeros_pares()
print(next(pares))  # 0
print(next(pares))  # 2
print(next(pares))  # 4

# Generator expression
quadrados = (x**2 for x in range(10))
print(list(quadrados))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### 9.3 Expressões Geradoras
**Conceito**: Sintaxe concisa para criar geradores.

```python
# Generator expression vs List comprehension
numeros = range(1000000)

# List comprehension - cria toda a lista na memória
quadrados_lista = [x**2 for x in numeros]

# Generator expression - cria sob demanda
quadrados_gen = (x**2 for x in numeros)

# Usando em funções
def processar_grandes_dados():
    # Eficiente em memória
    for quadrado in (x**2 for x in range(1000000) if x % 2 == 0):
        if quadrado > 1000:
            break
        yield quadrado

# Soma de quadrados pares usando generator
soma = sum(x**2 for x in range(100) if x % 2 == 0)
print(f"Soma dos quadrados pares: {soma}")
```

## 🎯 Nível 10: Decorators

### 10.1 Decorators Básicos
**Conceito**: Funções que modificam o comportamento de outras funções.

```python
def meu_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Executando {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"Finalizou {func.__name__}")
        return resultado
    return wrapper

@meu_decorator
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("João"))

# Decorator com parâmetros
def repetir(vezes):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(vezes):
                resultado = func(*args, **kwargs)
            return resultado
        return wrapper
    return decorator

@repetir(3)
def cumprimentar():
    print("Oi!")

cumprimentar()
```

### 10.2 Decorators Úteis
**Conceito**: Decorators práticos para diferentes situações.

```python
import time
import functools

def cronometrar(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"{func.__name__} executou em {fim - inicio:.4f} segundos")
        return resultado
    return wrapper

def cache_simples(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Cache hit para {args}")
            return cache[args]
        resultado = func(*args)
        cache[args] = resultado
        return resultado
    return wrapper

@cronometrar
@cache_simples
def fibonacci_lento(n):
    if n < 2:
        return n
    return fibonacci_lento(n-1) + fibonacci_lento(n-2)

# Testando
print(fibonacci_lento(10))
print(fibonacci_lento(10))  # Segunda chamada usa cache
```

### 10.3 Decorators de Classe
**Conceito**: Decorators aplicados a classes e métodos.

```python
def singleton(cls):
    instancias = {}
    def get_instance(*args, **kwargs):
        if cls not in instancias:
            instancias[cls] = cls(*args, **kwargs)
        return instancias[cls]
    return get_instance

@singleton
class ConfiguracaoApp:
    def __init__(self):
        self.configuracoes = {}
    
    def set_config(self, chave, valor):
        self.configuracoes[chave] = valor
    
    def get_config(self, chave):
        return self.configuracoes.get(chave)

# Testando singleton
config1 = ConfiguracaoApp()
config2 = ConfiguracaoApp()
print(config1 is config2)  # True

# Property decorator
class Temperatura:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("Temperatura abaixo do zero absoluto")
        self._celsius = valor
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

temp = Temperatura()
temp.celsius = 25
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")
```

## 📊 Nível 11: Bibliotecas Essenciais

### 11.1 Collections
**Conceito**: Estruturas de dados especializadas.

```python
from collections import Counter, defaultdict, deque, namedtuple, OrderedDict

# Counter - contagem automática
texto = "abracadabra"
contador = Counter(texto)
print(contador)  # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
print(contador.most_common(2))  # [('a', 5), ('b', 2)]

# defaultdict - valor padrão automático
grupos = defaultdict(list)
pessoas = [
    ("João", "TI"),
    ("Maria", "RH"),
    ("Pedro", "TI"),
    ("Ana", "RH")
]

for nome, departamento in pessoas:
    grupos[departamento].append(nome)

print(dict(grupos))  # {'TI': ['João', 'Pedro'], 'RH': ['Maria', 'Ana']}

# deque - fila dupla eficiente
fila = deque([1, 2, 3])
fila.appendleft(0)
fila.append(4)
print(fila)  # deque([0, 1, 2, 3, 4])
print(fila.popleft())  # 0
```

### 11.2 Itertools
**Conceito**: Ferramentas para criar iteradores ef

## 📅 **MÊS 1: Fundamentos Sólidos e Boas Práticas**

### Semana 1-2: Python Avançado e Estruturas de Dados

#### 1. List Comprehensions e Generator Expressions
```python
# List Comprehension
numeros_pares = [x for x in range(20) if x % 2 == 0]
print(numeros_pares)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Generator Expression (economiza memória)
quadrados = (x**2 for x in range(1000000))
primeiro_quadrado = next(quadrados)  # 0
```

#### 2. Decorators
```python
import functools
import time

def medir_tempo(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"{func.__name__} executou em {fim - inicio:.4f}s")
        return resultado
    return wrapper

@medir_tempo
def operacao_lenta():
    time.sleep(1)
    return "Operação concluída"

resultado = operacao_lenta()
```

#### 3. Context Managers
```python
from contextlib import contextmanager

@contextmanager
def gerenciar_conexao():
    print("Abrindo conexão...")
    conexao = "Conexão ativa"
    try:
        yield conexao
    finally:
        print("Fechando conexão...")

# Uso
with gerenciar_conexao() as conn:
    print(f"Usando: {conn}")
```

### Semana 3-4: Programação Orientada a Objetos Avançada

#### 4. Classes Abstratas e Interfaces
```python
from abc import ABC, abstractmethod
from typing import Protocol

class Processador(ABC):
    @abstractmethod
    def processar(self, dados):
        pass

class ProcessadorTexto(Processador):
    def processar(self, dados):
        return dados.upper()

# Protocol (Interface moderna)
class Serializable(Protocol):
    def serialize(self) -> str: ...

class Usuario:
    def __init__(self, nome: str):
        self.nome = nome
    
    def serialize(self) -> str:
        return f"Usuario: {self.nome}"
```

#### 5. Metaclasses
```python
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self):
        self.connected = True
        
# Teste
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True
```

---

## 📅 **MÊS 2: Ferramentas de Desenvolvimento e Testing**

### Semana 1-2: Testing e TDD

#### 6. Testes Unitários com pytest
```python
# arquivo: test_calculadora.py
import pytest

class Calculadora:
    def somar(self, a, b):
        return a + b
    
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero")
        return a / b

# Testes
def test_somar():
    calc = Calculadora()
    assert calc.somar(2, 3) == 5

def test_dividir_por_zero():
    calc = Calculadora()
    with pytest.raises(ValueError):
        calc.dividir(10, 0)

@pytest.mark.parametrize("a,b,esperado", [
    (10, 2, 5),
    (20, 4, 5),
    (100, 10, 10)
])
def test_dividir_parametrizado(a, b, esperado):
    calc = Calculadora()
    assert calc.dividir(a, b) == esperado
```

#### 7. Mocking e Fixtures
```python
from unittest.mock import Mock, patch
import requests

class ApiClient:
    def buscar_usuario(self, user_id):
        response = requests.get(f"https://api.exemplo.com/users/{user_id}")
        return response.json()

# Teste com mock
@patch('requests.get')
def test_buscar_usuario(mock_get):
    # Configurar mock
    mock_response = Mock()
    mock_response.json.return_value = {"id": 1, "nome": "João"}
    mock_get.return_value = mock_response
    
    # Testar
    client = ApiClient()
    resultado = client.buscar_usuario(1)
    
    assert resultado["nome"] == "João"
    mock_get.assert_called_once_with("https://api.exemplo.com/users/1")
```

### Semana 3-4: Gerenciamento de Dependências e Ambientes

#### 8. Poetry e Gerenciamento de Dependências
```toml
# pyproject.toml
[tool.poetry]
name = "meu-projeto"
version = "0.1.0"
description = "Projeto exemplo"

[tool.poetry.dependencies]
python = "^3.9"
requests = "^2.28.0"
pydantic = "^1.10.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.0.0"
black = "^22.0.0"
mypy = "^0.991"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

#### 9. Type Hints Avançados
```python
from typing import Union, Optional, List, Dict, TypeVar, Generic, Callable
from dataclasses import dataclass

T = TypeVar('T')

@dataclass
class ApiResponse(Generic[T]):
    data: T
    status_code: int
    message: Optional[str] = None

def processar_dados(
    dados: List[Dict[str, Union[str, int]]],
    filtro: Callable[[Dict], bool]
) -> List[Dict[str, Union[str, int]]]:
    return [item for item in dados if filtro(item)]

# Uso
usuarios = [
    {"nome": "João", "idade": 25},
    {"nome": "Maria", "idade": 30}
]

adultos = processar_dados(usuarios, lambda u: u["idade"] >= 18)
```

---

## 📅 **MÊS 3: Programação Assíncrona e Performance**

### Semana 1-2: AsyncIO e Programação Assíncrona

#### 10. Async/Await Básico
```python
import asyncio
import aiohttp
import time

async def buscar_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def buscar_multiplas_urls():
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/1"
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [buscar_url(session, url) for url in urls]
        resultados = await asyncio.gather(*tasks)
        return resultados

# Comparação sync vs async
def versao_sincrona():
    import requests
    inicio = time.time()
    for _ in range(3):
        requests.get("https://httpbin.org/delay/1")
    print(f"Síncrono: {time.time() - inicio:.2f}s")

async def versao_assincrona():
    inicio = time.time()
    await buscar_multiplas_urls()
    print(f"Assíncrono: {time.time() - inicio:.2f}s")

# asyncio.run(versao_assincrona())
```

#### 11. Concurrent.futures e Threading
```python
import concurrent.futures
import requests
import threading
from queue import Queue

# ThreadPoolExecutor
def fetch_url(url):
    response = requests.get(url)
    return f"{url}: {response.status_code}"

urls = ["https://httpbin.org/status/200"] * 5

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    resultados = list(executor.map(fetch_url, urls))
    print(resultados)

# Producer-Consumer com Queue
def producer(queue):
    for i in range(5):
        queue.put(f"item-{i}")
        print(f"Produzido: item-{i}")

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consumido: {item}")
        queue.task_done()

q = Queue()
threading.Thread(target=producer, args=(q,)).start()
threading.Thread(target=consumer, args=(q,)).start()
```

### Semana 3-4: Otimização e Profiling

#### 12. Profiling e Otimização
```python
import cProfile
import pstats
from functools import lru_cache
import timeit

# Fibonacci com cache
@lru_cache(maxsize=None)
def fibonacci_cache(n):
    if n < 2:
        return n
    return fibonacci_cache(n-1) + fibonacci_cache(n-2)

def fibonacci_sem_cache(n):
    if n < 2:
        return n
    return fibonacci_sem_cache(n-1) + fibonacci_sem_cache(n-2)

# Comparação de performance
def comparar_performance():
    n = 30
    
    # Com cache
    tempo_cache = timeit.timeit(lambda: fibonacci_cache(n), number=1)
    print(f"Com cache: {tempo_cache:.6f}s")
    
    # Sem cache
    tempo_sem_cache = timeit.timeit(lambda: fibonacci_sem_cache(n), number=1)
    print(f"Sem cache: {tempo_sem_cache:.6f}s")

# Profiling
def exemplo_profiling():
    pr = cProfile.Profile()
    pr.enable()
    
    # Código a ser analisado
    fibonacci_cache(35)
    
    pr.disable()
    stats = pstats.Stats(pr)
    stats.sort_stats('cumulative').print_stats(10)
```

---

## 📅 **MÊS 4: Frameworks Web e APIs**

### Semana 1-2: FastAPI Avançado

#### 13. FastAPI com Pydantic e Validação
```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr, validator
from typing import Optional, List
import uuid

app = FastAPI(title="API Avançada", version="1.0.0")

class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    idade: int
    
    @validator('idade')
    def validar_idade(cls, v):
        if v < 18:
            raise ValueError('Usuário deve ser maior de idade')
        return v

class Usuario(UsuarioCreate):
    id: uuid.UUID
    ativo: bool = True

# Simulação de banco de dados
usuarios_db = {}

def get_usuario_service():
    return UsuarioService()

class UsuarioService:
    def criar_usuario(self, usuario_data: UsuarioCreate) -> Usuario:
        user_id = uuid.uuid4()
        usuario = Usuario(**usuario_data.dict(), id=user_id)
        usuarios_db[user_id] = usuario
        return usuario

@app.post("/usuarios/", response_model=Usuario)
async def criar_usuario(
    usuario: UsuarioCreate,
    service: UsuarioService = Depends(get_usuario_service)
):
    return service.criar_usuario(usuario)

@app.get("/usuarios/{user_id}", response_model=Usuario)
async def buscar_usuario(user_id: uuid.UUID):
    if user_id not in usuarios_db:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuarios_db[user_id]
```

#### 14. Middleware e Autenticação JWT
```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from passlib.context import CryptContext
import datetime

SECRET_KEY = "seu-secret-key-aqui"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()

def criar_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

@app.post("/login")
async def login(username: str, password: str):
    # Verificação simplificada
    if username == "admin" and password == "senha123":
        token = criar_access_token({"sub": username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Credenciais inválidas")

@app.get("/protegido")
async def rota_protegida(current_user: str = Depends(verificar_token)):
    return {"message": f"Olá {current_user}, você está autenticado!"}
```

### Semana 3-4: Django REST Framework

#### 15. Django REST API com Serializers
```python
# models.py
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)
    criado_em = models.DateTimeField(auto_now_add=True)

# serializers.py
from rest_framework import serializers
from .models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
    
    def validate_preco(self, value):
        if value <= 0:
            raise serializers.ValidationError("Preço deve ser positivo")
        return value

# views.py
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['categoria']
    search_fields = ['nome']
    
    @action(detail=False, methods=['get'])
    def por_categoria(self, request):
        categoria = request.query_params.get('categoria')
        produtos = self.queryset.filter(categoria=categoria)
        serializer = self.get_serializer(produtos, many=True)
        return Response(serializer.data)

# urls.py
from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
urlpatterns = router.urls
```

---

## 📅 **MÊS 5: Bancos de Dados e ORMs**

### Semana 1-2: SQLAlchemy Avançado

#### 16. SQLAlchemy Core e ORM
```python
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import select, func
import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    criado_em = Column(DateTime, default=datetime.datetime.utcnow)
    
    posts = relationship("Post", back_populates="autor")

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    titulo = Column(String(200), nullable=False)
    conteudo = Column(String(1000))
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    criado_em = Column(DateTime, default=datetime.datetime.utcnow)
    
    autor = relationship("Usuario", back_populates="posts")

# Uso
engine = create_engine('sqlite:///exemplo.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def criar_usuario_com_posts():
    session = Session()
    
    # Criar usuário
    usuario = Usuario(nome="João Silva", email="joao@exemplo.com")
    session.add(usuario)
    session.flush()  # Para obter o ID
    
    # Criar posts
    posts = [
        Post(titulo="Primeiro Post", conteudo="Conteúdo...", usuario_id=usuario.id),
        Post(titulo="Segundo Post", conteudo="Mais conteúdo...", usuario_id=usuario.id)
    ]
    session.add_all(posts)
    session.commit()
    
    # Query complexa
    resultado = session.query(Usuario.nome, func.count(Post.id).label('total_posts'))\
                     .join(Post)\
                     .group_by(Usuario.id)\
                     .all()
    
    print(resultado)
    session.close()
```

#### 17. Migrações e Schema Evolution
```python
# alembic/versions/001_initial.py
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'usuarios',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nome', sa.String(100), nullable=False),
        sa.Column('email', sa.String(100), nullable=False),
        sa.Column('criado_em', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )

def downgrade():
    op.drop_table('usuarios')

# Repository Pattern
class UsuarioRepository:
    def __init__(self, session):
        self.session = session
    
    def criar(self, usuario_data):
        usuario = Usuario(**usuario_data)
        self.session.add(usuario)
        self.session.commit()
        return usuario
    
    def buscar_por_email(self, email):
        return self.session.query(Usuario).filter_by(email=email).first()
    
    def listar_com_posts(self):
        return self.session.query(Usuario)\
                          .join(Post)\
                          .options(relationship(Usuario.posts))\
                          .all()
```

### Semana 3-4: NoSQL e Redis

#### 18. MongoDB com PyMongo
```python
from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId

client = MongoClient('mongodb://localhost:27017/')
db = client.minha_app
collection = db.usuarios

class UsuarioMongo:
    def __init__(self):
        self.collection = collection
    
    def criar_usuario(self, nome, email, metadata=None):
        documento = {
            "nome": nome,
            "email": email,
            "criado_em": datetime.utcnow(),
            "metadata": metadata or {}
        }
        resultado = self.collection.insert_one(documento)
        return str(resultado.inserted_id)
    
    def buscar_usuarios_por_filtro(self, filtros):
        # Busca com agregação
        pipeline = [
            {"$match": filtros},
            {"$lookup": {
                "from": "posts",
                "localField": "_id",
                "foreignField": "usuario_id",
                "as": "posts"
            }},
            {"$addFields": {
                "total_posts": {"$size": "$posts"}
            }}
        ]
        return list(self.collection.aggregate(pipeline))

# Uso
usuario_service = UsuarioMongo()
user_id = usuario_service.criar_usuario(
    "Maria Silva", 
    "maria@exemplo.com",
    {"preferences": {"theme": "dark"}}
)

usuarios = usuario_service.buscar_usuarios_por_filtro({
    "criado_em": {"$gte": datetime(2024, 1, 1)}
})
```

#### 19. Redis para Cache e Sessions
```python
import redis
import json
import pickle
from functools import wraps

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def cache_result(expiration=3600):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Criar chave única
            cache_key = f"{func.__name__}:{hash(str(args) + str(kwargs))}"
            
            # Tentar buscar no cache
            cached = redis_client.get(cache_key)
            if cached:
                return pickle.loads(cached)
            
            # Executar função e cachear resultado
            result = func(*args, **kwargs)
            redis_client.setex(cache_key, expiration, pickle.dumps(result))
            return result
        return wrapper
    return decorator

@cache_result(expiration=1800)
def buscar_dados_api(endpoint):
    # Simulação de chamada cara para API
    import time
    time.sleep(2)  # Simula latência
    return {"data": f"Dados de {endpoint}", "timestamp": time.time()}

# Session management
class SessionManager:
    def __init__(self, redis_client):
        self.redis = redis_client
    
    def criar_sessao(self, user_id, dados_sessao):
        session_key = f"session:{user_id}"
        self.redis.hmset(session_key, dados_sessao)
        self.redis.expire(session_key, 86400)  # 24 horas
        return session_key
    
    def obter_sessao(self, session_key):
        return self.redis.hgetall(session_key)
    
    def invalidar_sessao(self, session_key):
        self.redis.delete(session_key)

# Uso
session_mgr = SessionManager(redis_client)
session_key = session_mgr.criar_sessao("user123", {
    "nome": "João",
    "role": "admin",
    "login_time": str(datetime.now())
})
```

---

## 📅 **MÊS 6: DevOps, Deploy e Arquitetura**

### Semana 1-2: Containerização e Docker

#### 20. Docker e Docker Compose
```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY . .

# Criar usuário não-root
RUN useradd --create-home --shell /bin/bash app
USER app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```yaml
# docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/myapp
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis
    volumes:
      - ./app:/app/app
    
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
  
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
  
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - web

volumes:
  postgres_data:
```

#### 21. Health Checks e Monitoring
```python
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import psutil
import time

app = FastAPI()

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "version": "1.0.0"
    }

@app.get("/health/detailed")
async def detailed_health_check():
    try:
        # Verificar recursos do sistema
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        # Verificar dependências (banco, redis, etc.)
        db_status = await verificar_database()
        redis_status = await verificar_redis()
        
        health_data = {
            "status": "healthy" if all([db_status, redis_status]) else "unhealthy",
            "timestamp": time.time(),
            "system": {
                "cpu_percent": cpu_percent,
                "memory_percent": memory.percent,
                "disk_percent": (disk.used / disk.total) * 100
            },
            "dependencies": {
                "database": "up" if db_status else "down",
                "redis": "up" if redis_status else "down"
            }
        }
        
        status_code = status.HTTP_200_OK if health_data["status"] == "healthy" else status.HTTP_503_SERVICE_UNAVAILABLE
        return JSONResponse(content=health_data, status_code=status_code)
        
    except Exception as e:
        return JSONResponse(
            content={"status": "unhealthy", "error": str(e)},
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE
        )

async def verificar_database():
    # Implementar verificação do banco
    return True

async def verificar_redis():
    # Implementar verificação do Redis
    return True
```

### Semana 3-4: CI/CD e Observabilidade

#### 22. GitHub Actions para CI/CD
```yaml
# .github/workflows/ci-cd.yml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: postgres
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Cache dependencies
      uses: actions/cache@v3
      with:
        path: ~/.cache/pip
        key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-dev.txt
    
    - name: Lint with flake8
      run: |
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        flake8 . --count --exit-zero --max-complexity=10 --statistics
    
    - name: Type check with mypy
      run: mypy .
    
    - name: Test with pytest
      run: |
        pytest --cov=app --cov-report=xml
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Deploy to production
      run: |
        echo "Deploy para produção"
        # Implementar deploy real
```

#### 23. Logging e Observabilidade
```python
import logging
import structlog
from pythonjsonlogger import jsonlogger
import time
from functools import wraps

# Configuração de logging estruturado
def configurar_logging():
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.JSONRenderer()
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

# Decorator para logging de performance
def log_performance(logger):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            
            logger.info(
                "function_started",
                function=func.__name__,
                args=len(args),
                kwargs=list(kwargs.keys())
            )
            
            try:
                result = func(*args, **kwargs)
                execution_time = time.time() - start_time
                
                logger.info(
                    "function_completed",
                    