def menu():
    menu = """
[u] Cadastrar Usuário
[c] Cadastrar Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

    lista_clientes = []
    lista_de_contas = []
    valor = 0


    while True:
    
        opcao = input(menu)

        if opcao == "d":
            deposito(saldo, valor, extrato)
        elif opcao == "s":
            saque(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)
        elif opcao == "e":
            deposito(saldo, valor, extrato)
        elif opcao == "u":
            lista_clientes = cadastrar_usuario(lista_clientes)
        elif opcao == "c":
            lista_de_contas = cadastrar_conta(lista_de_contas, lista_clientes)
        elif opcao == "q":
            break
        
def cadastrar_usuario(lista):
    lista_aux = []
    lista_aux.append(input("Informe o seu CPF: "))
    cpf = lista_aux[0]
    error = False
    tamanho_lista = len(lista)

    for i in range(tamanho_lista):
        if cpf == lista[i][0]:
            error = True
            print("Este CPF já existe!")
            return lista
        
    lista_aux.append(input("Informe o seu nome: "))
    lista_aux.append(input("Informe a data do seu nascimento: "))
    lista_aux.append(input("Informe o seu endereço: Logradouro, número - bairro - cidade/sigla estado: "))
    
    if error == False:
        print("O seu usuário foi cadastrado")
        lista.append(lista_aux)

    return lista
    
def cadastrar_conta(lista_de_contas,lista_de_clientes, AGENCIA="001"):
    nova_conta = []
    cpf = input("Informe o seu CPF para o cadastro de conta: ")
    error = True
    for i in range(len(lista_de_clientes)):
        if cpf == lista_de_clientes[i][0]:
            error = False
    if error == True:
        print("Você deve criar um usuário primeiro")
        return lista_de_contas

    numero_da_conta = len(lista_de_contas) + 1
    saldo = 0
    limite_saque = float(input("Informe o limite de saque diário: "))
    numero_de_saques_diarios = int(input("Informe o número máximo de saques diários desejado: "))
    nova_conta.append(cpf)
    nova_conta.append(numero_da_conta)
    nova_conta.append(saldo)
    nova_conta.append(limite_saque)
    nova_conta.append(numero_de_saques_diarios)
    print("Sua conta corrente foi criada!")

    return lista_de_contas

def saque(*,saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    
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

    return saldo, extrato

def deposito(saldo, valor, extrato, /):
    valor = float(input("Informe o valor do depósito: "))
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        
    else:
        print("Operação falhou! O valor informado é inválido")

    return saldo, extrato

def extrato(saldo, *, extrato):
    print("\n==============EXTRATO==============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n===================================")
    

menu()