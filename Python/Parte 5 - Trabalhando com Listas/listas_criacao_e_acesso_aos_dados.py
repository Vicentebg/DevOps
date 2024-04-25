# Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto
# Podemos criar listas utilizando o construtor list, a função range ou colocando valores separados por vírgula dentro de colchetes
# Listas são objetos mutáveis, portanto podemos alterar seus valores após a criação.

# Exemplos

frutas = ["laranja", "maçã", "uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list (range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2024, 2900, "São Paulo", True]
print(carro)

# Acesso direto - Para acessar os dados iremos utilizar o índice, o índice se inicia em 0 ou seja algo com range de 10 será de 0 a 9.

#             0        1       2       3
frutas = ["laranja", "maçã", "uva", "pera"]
print(frutas[0]) # maçã
print(frutas[2]) # uva

# Quando utilizamos o -1 ele pega o último elemento, ele irá começar da direita para esquerda
print(frutas[-1]) # pera
print(frutas[-3]) # laranja

# Lista aninhadas - São listas de matriz bidimensionais(tabelas), e iremos acessar usando o índice de linha e coluna.

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

# Se eu quiser recuperar o valor de uma linha vou usar matriz[0] por exemplo mas se eu quiser um elemento especifico vou passar linhaXcoluna

print(matriz[0]) # [1, "a", 2]
print(matriz[0][0]) # 1
print(matriz[0][-1]) # 2
print(matriz[-1][-1]) # "c"

# Fatiamento - Precisamos passar um valor inicial e/ou final para acessar o conjunto. Também podemos informar quantas posições vão ser "puladas" no acesso.

lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:]) # ['t', 'h', 'o', 'n']
print(lista[:2]) # ['p', 'y']
print(lista[1:3]) # ['y', 't']
print(lista[0:3:2]) # ['p', 't']
print(lista[::]) # ['p', 'y', 't', 'h', 'o', 'n']
print(lista[::-1]) # ['n', 'o', 'h', 't', 'y', 'p']

# Iterar listas - Iremos utilizar o for para percorrer os dados de uma lista

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

# Função enumerate - Para saber qual o índice do objeto dentro do laço for iremos usar a função enumerate

carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# Compreensão de listas - Serve para criar uma nova lista com base nos valores de uma lista existente
# Filtro versão 1 - Pegar todos os números pares

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# Filtro versão 2 - Pegar todos os números pares

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

# Modificando valores versão 1
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

# Modificando valores versão 1
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]