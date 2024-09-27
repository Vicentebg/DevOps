### Comandos básicos de Linux 

- `sudo apt update` - Atualizando as referências dos pacotes com as versões dos pacotes do servidor. 

- `sudo apt install openssh-server` - Se tivesse na versão de desktop, para ter o acesso via SSH. 

- `pwd` - Mostra em que diretório estou no sistema. 

- `ls` - Conteúdo do diretório 

- `ls -a` - Lista todo o conteúdo do diretório (arquivos ocultos), começam com ponto os - arquivos ocultos, exemplo .profile . 

- `ls -la` - Lista todo o conteúdo, mas no formato de lista com mais detalhes. 

- `ll` - Mesma coisa do comando de cima, só que é um atalho. 

- `clear` - Limpa tela. 

- `Ctrl + L` - Atalho para limpar a tela. 

- `ls --help` - Neste comando ele me dará uma ajuda sobre os argumentos que posso passar para o comando ls, mas posso utilizar qualquer comando --help, por exemplo `pwd` --help . 

- `man ls` - Comando que exibe tipo de um manual para o comando. 

- `cd` - Volta pra minha /home/ . 

- `cd /etc` - Vai para o diretório etc. 

- `cd -` - Ele realiza um switch do diretório em que estou e do diretório em que estava. 

- `cd ~` - Vai para /home/ . 

- `mkdir labs` - Cria diretório chamado labs. 

- `mkdir -p dir1/dir2/dir3` - O argumento -p possibilita criar vários diretórios de uma vez. 

- `touch arq1` - Cria um novo arquivo. 

- `touch arq2 arq3` - Cria 2 arquivos. 

- `touch .arq4` - Cria um arquivo oculto (oculto por causa do . no começo). 

- `rmdir` - Remove diretório. 

- `rm -r dir1` - Deleta diretórios e arquivos usando recursividade, deleta do dir1 para – frente. 

- `rm -r` - Para apagar diretórios. 

- `mkdir diretorio\ 2` - Para criar um diretório com o nome com espaço, ficará diretório 2 o nome dessa pasta. 

- `cp dir1 dir2` - Faz uma cópia do dir1 para o dir2 onde a estrutura é diretório: Da origem para diretório de destino. 

- `cp -r * ../dir2` - Considerando o caso de ter dois diretórios dir1 e dir2 na mesma hierarquia, dentro do dir1 tenho alguns arquivos e quero copiar esses arquivos para o dir2, o comando seria este, representando copiar em recursão todo o conteúdo de dir1 para dir2. 

- `cp -R * /var/www/html` - Este comando diz, copie tudo que está na pasta e jogue para var/www/html

- `cp -r dir1/* dir2` - Mesmo caso do de cima. 

- `mv dir1 dir4` - Ele vai renomear o diretório dir1 para dir4. 

- `mv dir1/* dir4` - Irá mover todos os arquivos dentro de dir1 para o dir4. 

- `history` - Mostra todos os comandos utilizados até o momento. 

- `ls arq1*` - Me retorne todos os arquivos a partir de arq1 incluindo nada. 

- `ls arq1?` - O ? irá substituir um caractere, no caso posso utilizar arq??? e caso tenha um diretório arq100 ele irá me retornar ele . 

- `ls *1* `- Ele irá procurar tudo que tem 1 no nome. 

- `ls ???[1-5]` - Em um cenário que estou considerando que os 3 primeiros caracteres seriam ou arq ou tmp e eu preciso encontrar os arquivos dentro de um intervalo, no caso de 1 a 5. 

- `ls arq[1,5]`- Para procurar arquivos que começam com arq e tenham 1 e 5. 

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

- `ip a` - Para verificar as configurações de IP.

# Trabalhando com usuários

### Criando e excluindo usuários

- `useradd joao.silva` - Criar um usuário dando um nome de login no sistema (Evitar usar acento e espaço em branco)

- `useradd joao -m -c "João da Silva" -s /bin/bash -p $(openssl passwd -crypt Senha123) -G GRP_ADM` - Criar um usuário (-m cria a pasta do usuário na home) (-c nome completo do usuário) (-s definir o tipo de bash que ele vai usar ou terminal) -p $(openssl passwd -crypt Senha123) isso irá criar a senha criptografada que é um requisito para criar um novo usuário já com senha (-G permite inserir o novo usuário a um grupo no caso o grupo GRP_ADM)

- `userdel -f joao.silva` - Excluir usuário

- `userdel -f -r joao.silva` - Excluir usuário e a pasta home e configurações de e-mail

- `passwd joao` - Definir senha do usuário

- `chsh -s /bin/bash joao` - Definir o bash como uso quando for logado no usuário CASO NÃO TENHA SIDO DEFINIDO NA CRIAÇÃO DO USUÁRIO

- `su joao` - Logar no usuário

### Editando informações do usuário

- `usermod joao` - Realizar mudanças no usuário

- `passwd joao -e` - Força o usuário a alterar a senha pois o -e faz expirar sua senha caso não passe nenhuma data

- `cat /etc/passwd` - Informações dos usuários criados

### Shell Script - Criando usuários em lote

- `nano criar_user.sh` - Para criar o arquivo do script

```
#!/bin/bash

for i in {1..50}
do
    username-"guest$i"
    useradd $username -c "Usuário convidado $i" -s /bin/bash -m -p $(openssl passwd -crypt Senha123)
    echo "Usuário $username criado com sucesso."
    passwd $username -e
done
```
- `chmod +x criar_user.sh` - Dar permissões para executar o script

- `./criar_user.sh` - Para executar o script você precisa estar na mesma pasta em que ele está ou o comando irá mudar

### Adicionando usuários a grupos

- `cat /etc/group` - Informações dos grupos

- `usermod -G adm,sudo joao` - Colocar em grupos com privilegios administrativos (-G significa que posso adicionar o usuario em mais de um grupo)
**Caso seja este usuário já esteja em outro grupo ele será retirado deles e será colocado somente nesses que foram passados**

### Criando novos grupos

- `groupadd GRP_ADM` - Criando um grupo chamado GRP_ADM

- `groupdel GRP_ADM` - Deletando um grupo chamado GRP_ADM

- `gpasswd -d joao sudo` - Removendo o usuário joao do grupo sudo

### Permissões

- `https://chmod-calculator.com/` - Este site é muito bom para saber qual as permissões.

- `ls -la` - Irá informar os arquivos ocultos e permissões

```
   d   rwx  r-x  r-x
  |    |    |    |
Tipo  Dono Grupo Outros



```

![image](https://github.com/Vicentebg/DevOps/assets/19577547/a15c7957-0c9b-4635-a37b-691de4b13a47)

- `chown joao:GRP_ADM /adm/` - Trocando o dono e o grupo do diretório onde o diretório é o /adm/ e o GRP_ADM o grupo

```
----------------------
| Leitura (R) |  4   |
| Gravação (W)|  2   |
| Execução (X)|  1   |
| Nenhuma     |  0   |
----------------------
```
Para dar permissão basta somar os números sendo que o 7 é permissão total

- `chmod 750 /adm/` - Permissão total para o DONO / Permissão de Leitura e Execução para o GRUPO e nada para OUTROS

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

# Trabalhando com pacotes

## Ubuntu & Debian

- `apt-get --help` - Para ver as funções disponíveis do apt-get, normalmente ele é usado para atualizar os pacotes do sistema com o comando `apt-get update` e `apt-get upgrade`é uma versão mais antiga e menos amigável.

- `apt --help` - Uma versão mais nova e mais amigável.

- `apt update` - Será checado os repositórios e caso possua atualização ele irá informar quantos estão disponiveis e será baixado, mas ainda não instalado.

- `apt upgrade` - Atualiza os pacotes do sistema operacional

*ALERTA* - CASO ESTEJA EM PRODUÇÃO OU FOR ATUALIZAR NORMALMENTE, SEMPRE RODAR O UPDATE ANTES DO UPGRADE E ANALISAR O QUE SERÁ ATUALIZADO.

- `apt list --installed` - Consegue ver os pacotes instalados na máquina.

- `apt list --upgradeable` - Ver quais pacotes estão disponíveis para serem atualizados.

- `apt search samba` - Para buscar se o pacote que você deseja está disponível, no caso estamos buscando do samba.

- `wget https://github.com/Vicentebg/DevOps/archive/refs/heads/main.zip` - Fará o download do repositório informado, pode ser utilizado para outros tipos de download.

- `unzip main.zip` - Irá descompactar o arquivo, caso a ferramenta não esteja instalada rodar o comando `apt install unzip`, caso seja .rar você pode utilizar o unrar.

- `apt install net-tools -y` - Irá instalar o pacote net-tools

- `apt remove net-tools -y` - Para remover alguma pacote caso o usuário deseje, neste exemplo estamos utilizando a ferramente net-tools, o `-y` retira as perguntas que o script de desinstalação vai realizar, é como se ele desse Yes para todas as perguntas.

- `apt edit-sources` - Aparece um arquivo de texto com os repositórios oficiais do sistema operacional, caso precise colocar algum repositório que não esteja disponível será neste arquivo que será colocado.

## Fedora, Debian, Red Hat & CentOS

- `dnf --help` - Mais amigável similiar ao apt

- `yum --help` - Normalmente utilizado para criação de scripts e mais antigo, similiar ao apt-get

- `dnf update` - Diferente do Ubuntu ele já realiza a instalação dos pacotes *TOMAR CUIDADO* criar um backup antes

- `dpkg -i nome_do_pacote.deb` - Debian para instalar algum pacote

# Gerenciamento de discos

O sistema de arquivo utilizado no Linux normalmente é o Ext3, Ext4 e XFS.

No Linux cada disco recebe um nome iniciado por sd.

Exemplo: sda, sdb, sdc...

Cada partição do disco é numerada

Exemplo: sda1, sda2, sda3, sdb1, sdb2...

- `lsblk` - Visualiza os discos disponíveis.

- `fdisk -l` - Outra forma de visualizar os discos disponíveis.

- `fdisk /dev/sdb` - Adicionando um novo disco na sua partição, ele entrará no menu do fdisk logo após entrar no menu iremos clicar a letra `n` e logo em seguida vamos teclar o `p` depois o `1`, `enter`para ficar definido como default, `enter` novamente e logo após terminar o processo iremos teclar o `w` para salvar as alterações. Agora precisamos formator o disco para se tornar utilizado, devemos formator no formato utilizado pelo sistema operacional.
O sdb indicado no comando significa que é um segundo disco

- `mkfs.ext4 /dev/sdb` - Para formatar iremos rodar este comando, onde o ext4 é o formato indicado para o Linux e o /dev/sdb indica qual disco será formatado.

*Agora vamos ter que montar o disco, ele já está pronto para uso.*

Normalmente é utilizado para a montagem o diretório mnt então vamos usar o comando `cd mnt` e criar uma pasta `mkdir disco2` logo em seguida vamos digitar o comando `mount /dev/sdb /mnt/disco2/` a partir de agora tudo que for salvo no disco sdb ficará neste repositório.

Para desmontar o disco `unmount /dev/sdb`

Bom agora tudo está funcionando, porém caso a máquina seja reiniciada ou desligada, você terá que refazer o processo novamente para isso iremos abordar a partir de agora uma maneira de montar automaticamente quando a máquina for reiniciada ou desligada.

## Montando discos automaticamente

- `vi /etc/fstab` - Irá para o arquivo de configuração dos discos que já estão montados, iremos editar com as novas configurações.

```
LABEL=cloudimg-rootfs   /        ext4   discard,errors=remount-ro       0 1
LABEL=UEFI      /boot/efi       vfat    umask=0077      0 1
/dev/sdb /mnt/disco2 ext4 defaults 0 0
# a swapfile is not a swap partition, no line here
#   use  dphys-swapfile swap[on|off]  for that
~                                
~                                
```
Iremos adicionar a terceira linha `/dev/sdb /mnt/disco2 ext4 defaults 0 0`, isso será de acordo com sua configuração, caso o diretório seja outro terá que ser passado o local certo.

## Iniciando, visualizando e encerrando processos

- `ps aux` - O comando ps mostra os processos porém só do terminal e não de todos os usuários, com `a` ele irá mostrar os processos de todos os usuários, o `u` fornece o nome do usuário e o horário que foi inicializado, já o `x` mostra os processos que foram iniciados fora do terminal utilizado. 

Iremos ter um retorno parecido com este:

```
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.2 167976  9732 ?        Ss   Mar23  16:11 /sbin/init
root           2  0.0  0.0      0     0 ?        S    Mar23   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        I<   Mar23   0:00 [rcu_gp]
root           4  0.0  0.0      0     0 ?        I<   Mar23   0:00 [rcu_par_gp]
root           5  0.0  0.0      0     0 ?        I<   Mar23   0:00 [slub_flushwq]
root           6  0.0  0.0      0     0 ?        I<   Mar23   0:00 [netns]
```

- `kill 2` - Iremos encerrar o processo da segunda linha, iremos passar o PID para encerrar o processo.

- `killall chrome` - Também podemos encerrar um processo passando um nome neste caso utilizamos o chrome como exemplo.

- `w` - Visualiza quais usuários estão logados na máquina no momento.

- `who -a` - Mostra o PID do usuário, com isso podemos ver um usuário que não era para estar logado em determinado horário ou um invasor e podemos dar um `kill` no seu PID e com isso desconectaremos ele.

## Servidor de Arquivos

- `apt install samba -y` - Instalar o SAMBA

Criaremos no disco 2 para não causar lentidão no sistema operacional e no servidor de arquivos,o diretório terá o nome de publica.

- `vi /etc/samba/smb.conf` - Arquivo de configuração do samba, no final do arquivo vamos colocar o nome da pasta que será compartilhada vamos adicionar da seguinte maneira

```
[publica]

path = /disk2/publica
writable = yes
guest ok = yes
guest only = yes
```

- `systemctl restart smbd` - Após adicionar as configurações acima e salvar o arquivo devemos realizar este comando para restartar o samba para ele identificar nossas alterações

- `systemctl restart smbd` - Para verificar o status do serviço

- `systemctl enable smbd` - Caso reinicie o servidor o serviço não irá startar automáticamente, para isso usamos este comando que sempre que reiniciar ele irá startar automáticamente.

Agora vamos tentar acessar a pasta compartilhada através do Windows, vamos colocar na barra do windows da seguinte forma `\\ip_do_servidor\publica` e irá pedir algumas credenciais, esse usuário precisa estar cadastrado no servidor linux, você pode utilizar as credenciais de usuário e senha nesta etapa e conseguirá acessar o servidor.

## Servidor Web

- `apt install apache2 -y` - Instalar o apache.

- `systemctl status apache2` - Verificar se ele está running.

Logo após colocar o IP do servidor no navegador para ver se o servidor web está rodando, lá ele irá te informar o caminho onde está o html `var/www/html` podemos alterar esse html e ter um site na nossa rede local.

## Servidor de Banco de Dados

- `apt search mysql` - Verificar qual versão está disponível.

- `apt install mysql-server-8.0 -y` - Instalando o MySQL.

- `mysql -u root -p` - Logar no banco de dados como usuário root.

- `create database meubanco;` - Cria um banco de dados com o nome de meubanco

- `show databases;` - Apresenta todos os bancos de dados que possuí.

- `use meubanco;` - Para utilizar o banco que foi criado

- `create table Pessoas (PessoaID int, Nome varchar (50), Sobrenome varchar(50), Endereco varchar(100), Cidade varchar(50));`  - Criando uma tabela no banco de dados meubanco com a coluna PessoaID, Nome, Sobrenome, Endereco e Cidade.

- `show tables;` - Para verificar se a tabela foi criada.

- `insert into Pessoas (PessoaID, Nome, Sobrenome, Endereco, Cidade) VALUES (1, 'Carlos', 'da Silva', 'Av. do carmo, 500', 'Jaboticabal-SP');` - Populando a nossa tabela com dados.

- `select * FROM Pessoas;` - Para ver o que tem dentro de Pessoas.

- `exit` - Para sair da interface do MySQL.
