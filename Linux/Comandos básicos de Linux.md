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
