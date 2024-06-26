# Comandos docker intermediários

- `docker ps` - Mostra os containers em execução

- `docker ps -a` - Mostra os containers que estão parados

- `docker container rm $(docker container ls -aq)` - Remover todos os containers -q pegar os IDs e o -a pegar todos os meus containers inclusive os parados

- `docker images` - Mostra as imagens que eu tenho

- `docker ps -s` - Mostra as imagens com o tamanho dela

- `docker ps -sa` - Mostra a imagem ativa e os antigos que já estiveram em executação

- `docker history ubuntu` - Para ver as camadas da imagem

- `docker rmi $(docker image ls -aq)` - Remove todas as imagens

- `docker run -it ubuntu bash` - Executar container sem precisar acionar o sleep

- `docker run -d dockersamples/static-site` - Flag -d para nao travar o terminal

- `docker run -d -P dockersamples/static-site` - Flag -P faz um redirecionamento da porta do container(interface de rede do container) para minha máquina

- `docker run -d -p 8080:80 dockersamples/static-site` - Posso mapear o redirecionamento atráves da flag -p e passando a porta do host : a porta do container, isso quer dizer onde eu quero refletir a porta do container na minha máquina, no caso, a porta 80 do container vai redirecionar para a porta 8080 da minha máquina

- `docker stop $(docker container ls -q)` - Parar parar todos os containers

----------------------------------------------------------------------------------------------------------------------------------------------------------
## Persistência de dados

### Bind mount
- `docker run -it -v /home/vicente/volume-docker:/app ubuntu bash` - Estou passando que quero que todos os dados dentro do meu container sejam persistidos neste diretório no meu host

- `docker run –mount type=bind,source=/home/diretorio,target=/app nginx` - Faz a mesma coisa que o comando de cima

### Volume
- `docker volume ls` - Lista os volumes criados

- `docker volume create meu-volume` - Cria um volume

- `docker run -it -v meu-volume:/app ubuntu bash` - Mesmo comando do Bind mount, mas passando o caminho diferente

- `docker run -it --mount soruce=meu-volume, target=/ app ubuntu bash` - Para criar um volume usando o mount

*Os volumes ficam dentro da pasta do docker em /var/lib/docker/volumes*

- `Tmpfs` - Só irá funcionar se o host for linux - Persiste os dados na memória então ele não salva os arquivos na camada R/W, e sim na memória, serve para dados sensiveis, e quando o container para ele perde os dados

- `docker run -it --tmpfs=/app ubuntu bash` - Criar um tmpfs, cria uma pasta tmp(que é temporaria)

--------------------------------------------------------------------------------------------------------------------------------------------------------------
## Comunicação através de redes

- `docker inspect <id_do_container>` - Mostra vários detalhes do container

- `docker network ls` - Listar as redes criadas

## Driver bridge

- `docker network create -- driver bridge minha-bridge` - Criando minha rede bridge

- `docker run -t --name ubuntu1 --network minha-bridge ubuntu bash` - Rodar o container dando um nome para ele e executando na rede criada acima

- `docker run -d --name pong --network minha-bridge ubuntu sleep 1d` - Rodar container dando o nome pong e sem ser no modo iterativo

*No final conseguimos ver os containers se pingando e fechando uma comunicacao entre si, ubuntu1 no modo bash pingando no pong.*

## None

- `docker run -d --network none ubuntu sleep 1d` - Criando um container na rede none
Se dermos um docker inspect neste container, vamos observar que suas configuraçoes sao vazias e nulas, isso porque o driver none é para alguma aplicacao que vai ficar isolada, e n ter acesso a rede

## Host

- `docker run -d --network host aluradocker/app-node:1.0` - Iniciar um container com a imagem do alura, essa versao roda na porta 3000, como esta setado para o driver host, se formos na nossa maquina e digitarmos no navegador localhost:3000 vamos conseguir acessar a aplicacao.
Utilizando o driver host o container estaria utilizando a mesma interface de rede do seu hospedeiro (host)

## Comunicação aplicação e banco de dados

Realizar um pull na imagem do mongo

- `docker run -d --network minha-bridge --name meu-mongo mongo:4.4.6` - minha-bridge é a rede que nos criamos, meu-mongo é o hostname que esta definido na aplicação no caso o banco

- `docker run -d --network minha-bridge --name alurabooks -p 3000:3000 aluradocker/alura-books:1.0` - O name na aplicação não importa nesse caso, pois a aplicação que busca o banco

## Docker-compose

- `docker-compose ps` - Mostra os servicos que foram criados pelo docker compose

- `docker-compose down` - Para e remove os containers e a rede

- `docker-compose up` - Dentro da pasta onde o compose está ele sobe o container do serviço










