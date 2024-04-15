# FOR - É usado para percorrer um objeto iterável. Faz sentido usar FOR quando sabemos o número exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print() # adiciona uma quebra de linha

# FOR com ELSE, mesma coisa do exemplo de cima porém fica mais organizado

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

else:
    print() # adiciona uma quebra de linha
    print("Executa no final do laço")

# Funçao Built-in Range - Recebe 3 argumentos: stop(obrigatorio), start (opcional) e step (opcional)
# 0 o inicio e 11 o final
# Colocamos 11 pois ele é exclusivo contamos o 0, então se fosse colocado 10, ele só ia até o 9 então podemos pensar sempre assim
# Queremos um range de 20, iremos colocar 21

for numero in range(0,11):
    print(numero, end=" ")

# Exibindo tabuada do 5 
# 0 Start | 51 Stop | 5 Step
for numero in range(0,51, 5):
    print(numero, end=" ")

# WHILE(Enquanto) - É usado para repetir um bloco de código várias vezes. Faz sentido usar while quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema")

# BREAK (Quebra) - O programa irá executar até o número ser igual a 10, o break é a condição de parada
opcao = -1

while True:
    numero = int(input("Informe um número"))

    if opcao == 10:
        break

    print(opcao)

# CONTINUE - Ao contrário do break ele não para a execução ele pula a execução
for numero in range(100):

    if numero == 12:
        break
    
    print(numero, end=" ")
# Nesse caso ele vai encerrar no 11 e não vai chegar até 99
for numero in range(100):

    if numero == 12:
        continue
    
    print(numero, end=" ")
# Com o CONTINUE ele irá pular o número 12, ele não será apresentado na lista de números

# Exibir somente números ímpares

for numero in range(100):

    if numero  % 2 == 0:
        continue
    
    print(numero, end=" ")