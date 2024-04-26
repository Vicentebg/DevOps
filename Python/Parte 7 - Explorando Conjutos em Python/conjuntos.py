# Sets - Coleção que não possui objetos repetidos, usamos o sets para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável

numeros = set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}
print(numeros)

letras = set("abacaxi") # {"b", "a", "c", "x", "i"}
print(letras)

carros = set(("palio", "gol", "celta", "palio")) # {"gol", "celta", "palio"}
print(carros)

linguagens = {"python", "java", "python"}
print(linguagens)

# Acessando dados - Conjutos não suportam indexação e nem fatiamento, para acessar os valores precisa-se converter o set em lista

numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])

# Enumerate

carros = {"gol","celta","palio"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# {}.union

conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b) # {1, 2, 3, 4}

# {}.intersection

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.intersection(conjunto_b) # {2, 3}

# {}.difference

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.difference(conjunto_b) # {1}
conjunto_b.difference(conjunto_a) # {4}

# {}.symmetric_difference - Todos os elementos que estão na intersecção ou seja os que não se tocam

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.symmetric_difference(conjunto_b) # {1, 4}

# {}.issubset - Todos os elementos de A pertencem a B e todos os elementos de B não pertencem a A

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b) # True
conjunto_b.issubset(conjunto_a) # False

# {}.issuperset - Todos os elementos de B não pertecem a A, mas todos os elementos de A estão em B

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issuperset(conjunto_b) # False
conjunto_b.issuperset(conjunto_a) # True

# {}.isdisjoint - Operação de conjunto disjunto, é um conjunto onde eles não se tocam, ou seja todos os elementos de um conjunto não estão presente em outro conjunto

conjunto_a = {1, 2, 3, 5, 6}
conjunto_b = {6, 7, 8, 9}
onjunto_c = {1,0}

conjunto_a.isdisjoint(conjunto_b) # True
conjunto_b.isdisjoint(conjunto_a) # False

# {}.add - Elemento é adicionado caso ele não exista, caso já exista ele será ignorado

sorteio = {1, 23}

sorteio.add(25) # {1, 23, 25}
sorteio.add(42) # {1, 23, 25, 42}
sorteio.add(25) # {1, 23, 25, 42}

# {}.clear - Vai limpar o set

sorteio = {1, 23}

sorteio # {1, 23}
sorteio.clear()
sorteio # {}

# {}.copy - Vai gerar uma cópia do set

sorteio = {1, 23}

sorteio # {1, 23}
sorteio.copy()
sorteio # {1, 23}

# {}.discard - Ele irá descartar um valor

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

numeros # {0,1,2,3,4,5,6,7,8,9} - elimina duplicados e ordena
numeros.discard(1)
numeros.discard(45)
numeros # {2,3,2,4,5,5,6,7,8,9,0}

# {}.pop - Vai removendo os números da frente

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

numeros # {0,1,2,3,4,5,6,7,8,9} - elimina duplicados e ordena
numeros.pop() # 0
numeros.pop() # 1
numeros # {2,3,4,5,6,7,8,9}

# {}.remove - Voce consegue passar o que quer remover, se o elemento não existir o programa irá dar um erro diferente do discard

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

numeros # {0,1,2,3,4,5,6,7,8,9} - elimina duplicados e ordena
numeros.remove(0) # 0
numeros # {1,2,3,4,5,6,7,8,9}

# len - Mostra a quantidade de elementos que tem dentro do set

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

len(numeros) # 10

# in - Para verificar se existe algum elemento dentro do nosso conjunto

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

1 in numeros # True
10 in numeros # False


