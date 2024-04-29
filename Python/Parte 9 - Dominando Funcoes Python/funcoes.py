# Função é um bloco de código identificado por um nome e pode receber uma lista de parametros, esses parametros podem ou não ter valores padrões.
# Usar funções torna o código mais legível e possibilita o reaproveitamento de código.
# Programar baseado em funções, é o mesmo que dizer que estamos programando de maneira estruturada.

def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")

# Retornando valores
# Para retornar um valor, utilizamos a palavra reservada return.
# Toda função em Python retorna None por padrão.
# Diferente de outras linguagens de programação, em Python uma função pode retornar mais de um valor.

def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11)

# Argumentos nomeados
# Funções também podem ser chamadas usando argumetnos nomeados da forma chave-valor

def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})

