# Temos o IF, ELIF e ELSE onde IF é SE, ELIF senão se, ELSE senão
# 1-Exemplo só utilizando IF(se)

MAIOR_IDADE = 18

IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")

if idade < MAIOR_IDADE:
    print("Menor de idade, não pode tirar CNH.")

# 2-Exemplo utilizando IF e ELSE

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")
else:
    print("Menor de idade, não pode tirar CNH.")

# 3-Exemplo utilizando IF,ELIF e ELSE

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas")
else:
    print("Menor de idade, não pode tirar CNH.")

# IFs aninhados
# DICA: Altere os valores como saque para 2500 para ver o comportamento das condições, altere também a conta normal para False e a universitaria para True
# Teste conta_normal = False / conta_universitaria = False | saque = 500 / saque = 2500 / saque = 1500
conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com seu gerente!")


# IF Ternário
# Permite escrever uma condição em uma única linha. É composto por três partes, primeira parte é o retorno caso a expressão retorne True, a segunda parte é a expressão lógica e a terceira parte é o retorno caso a expressão não seja atendida
# Quando saldo 2000 e saque 2500 irá dar sucesso e quando saldo 2000 e saque 2500 tem que dar falha
saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")