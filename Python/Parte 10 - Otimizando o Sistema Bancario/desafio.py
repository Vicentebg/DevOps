# Cria um sistema bancário com as operações: sacar, depositar e visualizar extrato.
# Regras de negócio: Deve ser possível depositar valores POSITIVOS para a conta bancária
# A primeira versão do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária
# DEPÓSITO: Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato
# SAQUE: Deve se permitir realizar 3 saques diários com limite máximo de R$500,00 por saque.
# Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
# Todos os saques devem ser armazenados em uma váriavel e exibidos na operação de extrato.
# EXTRATO: Deve listar todos os depósitos e saques realizados na conta.
# No fim da listagem deve ser exibido o saldo atual da conta.
# Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
# Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo : 1500.45 = R$ 1500.45


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
saque = 0
numero_saques = 0
LIMITE_SAQUES = 3
DEPOSITOS = 0

while True:
    
    opcao = input(menu)


    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
    
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == "e":
        print("\n==============EXTRATO==============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n===================================")
        
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

