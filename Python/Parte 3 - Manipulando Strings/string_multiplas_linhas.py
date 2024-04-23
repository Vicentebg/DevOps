# Strings triplas ou strings de multiplas linhas

nome = "Vicente"

mensagem = f"""
Olá meu nome é {nome},
Eu estou aprendendo Python
"""

print(mensagem)
# OUTPUT
# Olá meu nome é Vicente,
# Eu estou aprendendo Python

# Ele mantém o posicionamento da minha string

mensagem = f'''
    Olá meu nome é {nome},
Eu estou aprendendo Python.
        Essa mensagem tem diferentes recuos.
'''

print(mensagem)