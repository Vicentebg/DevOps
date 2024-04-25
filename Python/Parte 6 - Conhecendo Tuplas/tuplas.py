# Muito semelhante a tupla, porém seus dados são imutáveis enquanto listas seus dados são mutáveis

frutas = ("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)

# A vírgula no final é para o interpretador do Python entender que é uma tupla e não uma precedencia

# Acesso direto

frutas = ("maçã", "laranja", "uva", "pera",)

print(frutas[0]) # maçã
print(frutas[2]) # uva

print(frutas[-1]) # pera
print(frutas[-3]) # laranja

# Tuplas aninhadas - Seria como se criassemos uma tabela imutavel

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0]) # (1, "a", 2)
print(matriz[0][0]) # 1
print(matriz[0][-1]) # 2
print(matriz[-1][-1]) # "c"

# Fatiamento - Passar start, step, stop

tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:]) # ['t', 'h', 'o', 'n']
print(tupla[:2]) # ['p', 'y']
print(tupla[1:3]) # ['y', 't']
print(tupla[0:3:2]) # ['p', 't']
print(tupla[::]) # ['p', 'y', 't', 'h', 'o', 'n']
print(tupla[::-1]) # ['n', 'o', 'h', 't', 'y', 'p']

# Iterar tuplas

carros = ("gol", "celta", "palio",)

for carro in carros:
    print(carro)

# Enumerate

carros = ("gol", "celta", "palio",)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# Metódos da Tupla

# ().count

cores = ("vermelho", "azul", "verde", "azul",)

cores.count("vermelho") # 1
cores.count("azul") # 2
cores.count("verde") # 1

# ().index

linguagens = ("python", "js", "c", "java", "csharp",)

linguagens.index("java") # 3
linguagens.index("python") # 0

# len

linguagens = ("python", "js", "c", "java", "csharp",)

len(linguagens) # 5

