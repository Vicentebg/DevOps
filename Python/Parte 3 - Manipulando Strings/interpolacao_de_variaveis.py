# Método format

nome = "Vicente"
idade = 28
profissao = "Programador"
linguagem = "Python"

# AS variaveis precisam estar em ordem
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade , profissao, linguagem))


# Marcando as posições das variaveis começando em 0
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade , nome))


print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

# Dicionario

dicionario = {"nome": "Vicente", "idade": 28, "profissao": "Programador", "linguagem": "Python"}
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**dicionario))

# F-string
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

# Formatando strings com f-string

PI = 3.14159

print(f"Valor de PI: {PI:.2f}") # 2f significa que ele irá usar até 2 casas decimais

print(f"Valor de PI: {PI:10.2f}") # 10.2f ele irá dar 10 espaços em branco na frente