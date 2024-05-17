# Trabalhando com usuários

### Criando e excluindo usuários

- `useradd joao.silva` = Criar um usuário dando um nome de login no sistema (Evitar usar acento e espaço em branco)

- `useradd joao -m -c "João da Silva" -s /bin/bash -p $(openssl passwd -crypt Senha123) -G GRP_ADM` = Criar um usuário (-m cria a pasta do usuário na home) (-c nome completo do usuário) (-s definir o tipo de bash que ele vai usar ou terminal) -p $(openssl passwd -crypt Senha123) isso irá criar a senha criptografada que é um requisito para criar um novo usuário já com senha (-G permite inserir o novo usuário a um grupo no caso o grupo GRP_ADM)

- `userdel -f joao.silva` = Excluir usuário

- `userdel -f -r joao.silva` = Excluir usuário e a pasta home e configurações de e-mail

- `passwd joao` = Definir senha do usuário

- `chsh -s /bin/bash joao` = Definir o bash como uso quando for logado no usuário CASO NÃO TENHA SIDO DEFINIDO NA CRIAÇÃO DO USUÁRIO

- `su joao` = Logar no usuário

### Editando informações do usuário

- `usermod joao` = Realizar mudanças no usuário

- `passwd joao -e` = Força o usuário a alterar a senha pois o -e faz expirar sua senha caso não passe nenhuma data

- `cat /etc/passwd` = Informações dos usuários criados

### Shell Script - Criando usuários em lote

- `nano criar_user.sh` = Para criar o arquivo do script

```
#!/bin/bash

for i in {1..50}
do
    username="guest$i"
    useradd $username -c "Usuário convidado $i" -s /bin/bash -m -p $(openssl passwd -crypt Senha123)
    echo "Usuário $username criado com sucesso."
    passwd $username -e
done
```
- `chmod +x criar_user.sh` = Dar permissões para executar o script

- `./criar_user.sh` = Para executar o script você precisa estar na mesma pasta em que ele está ou o comando irá mudar

### Adicionando usuários a grupos

- `cat /etc/group` = Informações dos grupos

- `usermod -G adm,sudo joao` = Colocar em grupos com privilegios administrativos (-G significa que posso adicionar o usuario em mais de um grupo)
**Caso seja este usuário já esteja em outro grupo ele será retirado deles e será colocado somente nesses que foram passados**

### Criando novos grupos

- `groupadd GRP_ADM` = Criando um grupo chamado GRP_ADM

- `groupdel GRP_ADM` = Deletando um grupo chamado GRP_ADM

- `gpasswd -d joao sudo` = Removendo o usuário joao do grupo sudo

### Permissões

- `https://chmod-calculator.com/` = Este site é muito bom para saber qual as permissões.

- `ls -la` = Irá informar os arquivos ocultos e permissões

```
   d   rwx  r-x  r-x
  |    |    |    |
Tipo  Dono Grupo Outros



```

![image](https://github.com/Vicentebg/DevOps/assets/19577547/a15c7957-0c9b-4635-a37b-691de4b13a47)

- `chown joao:GRP_ADM /adm/` = Trocando o dono e o grupo do diretório onde o diretório é o /adm/ e o GRP_ADM o grupo

```
----------------------
| Leitura (R) |  4   |
| Gravação (W)|  2   |
| Execução (X)|  1   |
| Nenhuma     |  0   |
----------------------
```
Para dar permissão basta somar os números sendo que o 7 é permissão total

- `chmod 750 /adm/` = Permissão total para o DONO / Permissão de Leitura e Execução para o GRUPO e nada para OUTROS

```
chmod [tipo][operador][permissão] arquivo

Onde tipo pode ser:

u: dono do arquivo (user who owns it)
g: grupo do arquivo (group)
o: outros (others)
a: todos os acima (all)
Os operadores podem ser:

+: o sinal de mais adicionará as permissões a seguir
-: o sinal de menos removerá as permissões a seguir
E a permissão, pode ser a combinação de uma ou mais das letras que já vimos acima.

r: para leitura (read)
w: para escrita (write)
x: para execução (execute)


Exemplos:

chmod u+rwx arquivo.txt
Adiciona permissão de leitura, escrita e execução para o dono do arquivo
chmod g-w arquivo.txt
Remove permissão de escrita para pessoas inseridas no grupo ao qual o arquivo pertence
chmod a+r arquivo.txt
Dá permissão de leitura para todo mundo
chmod u+x,g-w,o+r arquivo.txt
Acrescenta permissão de execução para o dono, remove permissão de escrita para o grupo, e adiciona permissão de leitura para outros.
chmod -R u+rw diretório
Dá permissão de leitura e escrita para o dono em todos os arquivos e diretórios dentro de uma pasta recursivamente.
chmod o-rwx *.sql
Remove todas as permissões de que não é o dono nem faz parte do grupo, em todos os arquivos do diretório atual com extensão .sql.
```