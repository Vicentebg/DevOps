# Transformando tudo para maiúsculo, minúsculo ou título
curso = "pYtHon"

print(curso.upper()) # Maiúsculo

print(curso.lower()) # Minúsculo

print(curso.title()) # Título (Só a primeira letra maiúscula)

# Eliminando espaços em branco

curso = "         Python  "

print(curso.strip()) # Tira todos os espaços em brancos

print(curso.lstrip()) # Tira os espaços em branco da esquerda

print(curso.rstrip()) # Tira os espaços em branco da direita

# Junções e centralizações

curso = "Python"

print(curso.center(10, "#")) # "##Python##" 10 é o numero de quantos caracteres voce quer que tenha ou seja python tem 6 e ele preenche com # porque definimos # para preencher os espaços em branco

print(".".join(curso)) # "P.y.t.h.o.n"