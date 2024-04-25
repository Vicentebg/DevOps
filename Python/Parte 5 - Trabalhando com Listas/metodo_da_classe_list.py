# [].append

lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista) # [1, "Python", [40, 30, 20]]

# [].clear

lista = [1, "Python", [40, 30, 20]]

print(lista) # [1, "Python", [40, 30, 20]]

lista.clear()

print(lista) # []

# [].copy - O que eu fizer na lista copiada não reflete na lista principal

lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(lista) # [1, "Python", [40, 30, 20]]

print(id(l2), id(lista))

# [].count - Conta quantas vezes o objeto apareceu na lista

cores = ["vermelho", "azul", "verde", "azul"]

cores.count("vermelho") # 1
cores.count("azul") # 2
cores.count("verde") # 1

# [].extend - Serve para juntar listas

linguagens = ["python", "js", "c"]

print(linguagens) # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens) # ["python", "js", "c", "java", "csharp"]

# [].index - Se tiver alguma coisa igual ele sempre vai buscar o primeiro

print(linguagens) # ["python", "js", "c", "java", "csharp"]

linguagens.index("java") # 3

linguagens.index("python") # 0

# [].pop - Funciona como uma pilha tira sempre o último elemento da lista
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.pop() # csharp
linguagens.pop()# java
linguagens.pop() # c
linguagens.pop(0) #python

# [].remove - Diferente do pop você passa o que quer remover, também irá remover a primeira ocorrencia caso tenha algo repetido
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens) # ["python", "js", "java", "csharp"]

# [].reverse

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.reverse()

print(linguagens) # linguagens = ["python", "js", "c", "java", "csharp"]

# [].sort - Ordena nossa lista

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.sort() # ['csharp', 'java', 'c', 'js', 'python']

print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.sort(reverse=True) # ['python', 'js', 'java', 'csharp', 'c']

print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.sort(key=lambda x: len(x)) # ['c', 'js', 'java', 'python', 'csharp']

print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.sort(key=lambda x: len(x), reverse=True) # ['python', 'csharp', 'java', 'js', 'c']

print(linguagens)

# Len

linguagens = ["python", "js", "c", "java", "csharp"]

len(linguagens) # 5

# Sorted

linguagens = ["python", "js", "c", "java", "csharp"]

sorted(linguagens, key=lambda x: len(x)) # ["c", "js", "java", "python", "csharp"]

sorted(linguagens, key=lambda x: len(x), reverse=True) # ["python", "csharp","java","js", "c"]

