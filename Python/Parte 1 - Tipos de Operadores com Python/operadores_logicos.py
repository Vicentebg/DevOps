# Tabela
print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)
# AND = para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser True

# Operador E podemos considerar uma multiplicação X
# As duas partes da expressão precisam ser verdadeiras para que retorne true, saldo >= saque é True, porém saque <= limite é False é como se True = 1 e False = 0 -> 1 x 0 = 0
# Em AND se apenas 1 for falso dá falso, para ser verdadeiro todos tem que ser verdadeiro.
saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite # False

# Operador OU podemos considerar uma soma +
# No OR apenas uma parte da expressão precisa ser verdadeira para ela retornar True, seria mais ou menos como True = 1 e False = 0 -> 1 + 0 = 1 
# Em OR se apenas 1 for verdadeiro dá verdadeiro, para ser falso todos tem que ser falso
saldo = 1000
saque = 200
limite = 100

saldo >= saque or saque <= limite # True


# Operador de Negação
not 1000 > 1500 # True, pois o not inverte o resultado original que seria False pois 1000 não é maior que 1500

contatos_emergencia = []

not contatos_emergencia # True, lista vazia em python é considerado falso

not "saque 1500;" # False

not "" # True

# Parênteses
saldo = 1000
saque = 250
limite = 200
conta_especial = True

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) # True

