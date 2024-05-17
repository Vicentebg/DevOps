### Comandos básicos de Linux 

  

- `sudo apt update` = Atualizando as referências dos pacotes com as versões dos pacotes do servidor. 

- `sudo apt install openssh-server` = Se tivesse na versão de desktop, para ter o acesso via SSH. 

- `pwd` = Mostra em que diretório estou no sistema. 

- `ls` = Conteúdo do diretório 

- `ls -a` = Lista todo o conteúdo do diretório (arquivos ocultos), começam com ponto os - arquivos ocultos, exemplo .profile . 

- `ls -la` = Lista todo o conteúdo, mas no formato de lista com mais detalhes. 

- `ll` = Mesma coisa do comando de cima, só que é um atalho. 

- `clear` = Limpa tela. 

- `Ctrl + L` = Atalho para limpar a tela. 

- `ls --help` = Neste comando ele me dará uma ajuda sobre os argumentos que posso passar para o comando ls, mas posso utilizar qualquer comando --help, por exemplo `pwd` --help . 

- `man ls` = Comando que exibe tipo de um manual para o comando. 

- `cd` = Volta pra minha /home/ . 

- `cd /etc` = Vai para o diretório etc. 

- `cd -` = Ele realiza um switch do diretório em que estou e do diretório em que estava. 

- `cd ~` = Vai para /home/ . 

- `mkdir labs` = Cria diretório chamado labs. 

- `mkdir -p dir1/dir2/dir3` = O argumento -p possibilita criar vários diretórios de uma vez. 

- `touch arq1` = Cria um novo arquivo. 

- `touch arq2 arq3` = Cria 2 arquivos. 

- `touch .arq4` = Cria um arquivo oculto (oculto por causa do . no começo). 

- `rmdir` = Remove diretório. 

- `rm -r dir1` = Deleta diretórios e arquivos usando recursividade, deleta do dir1 para – frente. 

- `rm -r` = Para apagar diretórios. 

- `mkdir diretorio\ 2` = Para criar um diretório com o nome com espaço, ficará diretório 2 o nome dessa pasta. 

- `cp dir1 dir2` = Estrutura é diretório de origem para diretório de destino. 

- `cp -r * ../dir2` = Considerando o caso de ter dois diretórios dir1 e dir2 na mesma hierarquia, dentro do dir1 tenho alguns arquivos e quero copiar esses arquivos para o dir2, o comando seria este, representando copiar em recursão todo o conteúdo de dir1 para dir2. 

- `cp -r dir1/* dir2` = Mesmo caso do de cima. 

- `mv dir1 dir4` = Ele vai renomear o diretório dir1 para dir4. 

- `mv dir1/* dir4` = Irá mover todos os arquivos dentro de dir1 para o dir4. 

- `history` = Mostra todos os comandos utilizados até o momento. 

- `ls arq1*` = Me retorne todos os arquivos a partir de arq1 incluindo nada. 

- `ls arq1?` = O ? irá substituir um caractere, no caso posso utilizar arq??? e caso tenha um diretório arq100 ele irá me retornar ele . 

- `ls *1* `= Ele irá procurar tudo que tem 1 no nome. 

- `ls ???[1-5]` = Em um cenário que estou considerando que os 3 primeiros caracteres seriam ou arq ou tmp e eu preciso encontrar os arquivos dentro de um intervalo, no caso de 1 a 5. 

- `ls arq[1,5]`= Para procurar arquivos que começam com arq e tenham 1 e 5. 

## Filesystem Hierarchy Standard (padrão para sistema de arquivos hierárquico) ou FHS
![image](https://user-images.githubusercontent.com/19577547/180101809-2ac41b67-4f77-4bde-a891-dd5001f8ced5.png)

# Linux: Localizando arquivos e conteúdos

- `grep -i http services` - -i significa para para ignorar o case sensitive, ele trás http e HTTP, retorna a linha.

- `grep vicente *` - vai varrer todos os arquivos e me retornar a pasta e a linha onde aparece o nome.

- `grep -l vicente` - retorna o arquivo que tem o conteúdo que procuro

- `grep -L vicente` - ele retorna todos os arquivos que não tem o que estamos procurando

- `grep -r HTTP *` - o -r representa recursividade, ou seja daquele ponto em diante, ele irá procurar dali para frente

- `grep -rl HTTP *` - irá me retornar os diretorios com recursividade que possuem o HTTP 

- `more services` - irá retornar a tela com paginacao iterativa, sendo que o espaço pula para proxima pagina, enter pula linha a linha, B ele volta uma pagina, Q ele sai da pagina

- `find . -amin -5` - Mostra o que foi modificado ou criado nos últimos 5 minutos

- `find . -atime -2` - Mostra o que foi modificado nos últimos  2 dias

- `sudo find / -size +100M` - Procurar arquivos de  mais 100mb

- `ls -lh /swap.img` - Formata de um jeito mais humano para visualizar o tamanho

- `grep 3389 services >> listagem.txt` - O >> é muito importante pois se usar só o > ele irá sobrescrever o arquivo, então esse comandos busca 3389 e inclui no final do arquivo listagem.txt, caso não exista o arquivo ele irá criar

- `cut -d " " -f6-` - O -d no cut define um limitador, que no caso é o espaço, depois -f6- representa, o sexto espaço e o - no final representa até o final do arquivo

- `wc` - o comando retorna tres numeros, número de linhas, o número de palavras e a informação em bytes

- `wc -l` - retorna somente o numero de linhas do arquivo

- `cat logs | cut -d " " -f1-3,6- > logs-completo.txt` - Nesse comando ele vai conseguir pegar o time stamp e a mensagem do log completo e salvar em um arquivo

- `cat american-english | grep -iE "^smartphone$|^computer$"` - Vai buscar no arquivo american-english as palavras smartphone e computer, e nos retornar somente elas por conta do regex de inicio ^ e o de final $, o -i é para ignorar maiuscula ou minuscula e o -E para passar uma expressão regular(regex)


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