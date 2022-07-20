#### Caso não queira fazer os testes em sua máquina existe este site para "treinar" os comandos
`https://labs.play-with-docker.com/`

## Comandos

- **Para baixar/criar um container** - `docker run "iso"`
	
	Exemplo: `docker run ubuntu`

- **Para listar containers ativos** - `docker ps`

- **Para listar containers baixados e que não estão ativos** - `docker ps -a`
 ![image](https://user-images.githubusercontent.com/19577547/140802090-216dfe0a-619d-4efc-b1c1-f652e603d587.png)


- **Atrelar terminal do S.O com o do docker** - `docker run -it ubuntu`

- **Para iniciar um container** - `docker start "CONTAINER ID"`

	Exemplo: `docker start 05eeeed5e5a6`

- **Para parar um container** - `docker stop "CONTAINER ID"`

	Exemplo: `docker stop 05eeeed5e5a6`

- **Para iniciar um container e já atrelhar um terminal** - `docker start -a -i "CONTAINER ID"`

	Exemplo: `docker start -a -i a69`

- **Para buscar ajuda sobre como iniciar um container** - `docker start --help`

- **Para remover containers** - `docker rm "CONTAINER ID"`
	
	Exemplo: docker rm 1b4

- **Para remover containers:** `docker rm "CONTAINER ID"`
	
	Exemplo: `docker rm 1b4`

- **Para remover containers inativos** - `docker container prune`

- **Para visualizar as imagens do docker** - `docker images`

- **Para remover imagens do docker** - `docker rmi "REPOSITORY"`
 ![image](https://user-images.githubusercontent.com/19577547/140802187-8a94686f-e17d-4f32-bfe2-6186548630f7.png)

	
	Exemplo: `docker rmi hello-world`

- **Pare instalar uma imagem especifica (baixa várias camadas)** - `docker run ubuntu:14.04`

## WEB
#### Iremos hospedar um site estático
- **Baixando imagens não oficiais(feitos por outra pessoa)** - `docker run dockersamples/static-site`

	*Obs: Está imagem é para hospedar uma página html estática*

- **Rodando este container** - `docker run -d dockersamples/static-site`

	*Obs: A flag -d serve para rodar este comando "fora"do terminal, o docker vai rodar ele, não travando o próprio*
	
- **Para linkar uma porta do container para sua máquina** - `docker run dockersamples/static-site`	
![image](https://user-images.githubusercontent.com/19577547/140806834-539a8ea2-71b4-4c56-8c58-a574da421c24.png)

	*Obs: A flag -P faz com que o docker atribua as portas aleatorias que ele vai escolher para o mundo externo(máquina) para poder falar com o container.*

- **Para ver qual porta o container está utilizando** - `docker port "CONTAINER ID"`

	![image](https://user-images.githubusercontent.com/19577547/140807169-48a380a9-ca08-4d88-ab07-8bc4baefc8ba.png)

- **Para dar um nome ao container** - `docker run -d -P --name meu-site dockersamples/static-site`

- **Para mapear uma porta** -` docker run -d -p "IP+PORTA" dockersamples/static-site`

	Exemplo: `docker run -d -p 192.168.0.2:80 dockersamples/static-site`

- **Setar uma váriavel de ambiente** - `docker run -d -P -e AUTHOR="Vicente" dockersamples/static-site`

- **Para retornar apenas os IDs** - `docker ps -q`

- **Para parar containers em massa** - `docker stop -t 0 $(docker ps -q)`

	*Obs: Ele irá parar todos os containers que forem listados no comando (docker ps -q) e a flag -t 0, diz para o container parar na hora, pois o tempo default do docker é de 10 segundos.*

## Trabalhando com Volumes

 - O Volume sempre fica salvo no docker host
	
- **Para criar um container** - `docker run -v "/var/www" ubuntu`
- `docker run -it -v "C:\Users\Vicente\Desktop:/var/www" ubuntu`

	*Obs: Quando utiliza-se o Desktop:, o dois pontos separa o que é da minha máquina para o que é do container*
![image](https://user-images.githubusercontent.com/19577547/141129507-f8e762eb-e175-48e9-b578-daf42472f90b.png)

- **Para inspecionar o container** - `docker inspect "CONTAINER ID"`
	
	**Exemplo:** `docker inspect f3`

## Construindo nossas próprias imagens
Precisamos criar um arquivo chamado dockerfile em nosso programa com os seguintes exemplos de configuração:
![image](https://user-images.githubusercontent.com/19577547/141155742-dc5b3b6a-95c2-4c4c-a128-923e16518bf1.png)

	FROM node:latest
	MAINTAINER Vicente
	COPY . /var/www
	WORKDIR /var/www
	RUN npm install
	ENTRYPOINT npm start
	EXPOSE 3000

`docker build -f Dockerfile -t vicente/node . `

*Obs: Iremos passar a tag da imagem, o seu nome, através da flag -t, imagens nao oficiais precisamos colocar NOME_DO_USUARIO/NOME_DA_IMAGEM.*

**Também podemos criar variáveis de ambiente utilizando o ENV, por exemplo a variável PORT diz em que porta nossa aplicação irá rodar.**

![image](https://user-images.githubusercontent.com/19577547/141158848-9e864516-471a-4eaf-8f48-7565184f2d12.png)

`docker run -p -d 8080:3000 -v "C:\Users\Vicente\Desktop\volume-exemplo:/var/www" -w "/var/www" node npm start`
- **Melhorando o comando** - docker run -a -p 8080:3000 -v "$(pwd):/var/www" -w "/var/www" node npm start
	Exemplo: `docker run -v "[CAMINHO_VOLUME_LOCAL:]CAMINHO_VOLUME_CONTAINER" NOME_DA_IMAGEM`

## Subindo a imagem no Docker Hub

- **Para logar no docker hub** - `docker login`

- **Para dar um push na imagem que quer enviar para o Docker hub** - `docker push USERNAME/node`
	Exemplo:`docker push vicente/node`

- **Para dar um pull em alguma imagem** - `docker pull USERNAME/node`
	Exemplo: `docker pull vicente/node`

## Conectando Múltiplos Containers

- **Criando uma rede** - docker network create --driver bridge minha-rede
- **Listando as redes** - dcoker network ls

- **Para não deixar o container ser associado a rede padrão** - docker run -it --name meu-container-de-ubuntu --network minha-rede ubuntu
	*Obs: A flag --network diz para atrelar a rede, a rede que acabamos de criar*

## Pegando dados de um banco

**No exemplo a seguir utilizaremos dois comandos**
	
	docker pull douglasq/alura-books:cap05
	docker pull mongo

- **Subindo o banco de dados** - `docker run -d --name meu-mongo --network minha-rede mongo`

- **Subindo a aplicação** - `docker run --network minha-rede -d -p 8080:3000 douglasq/alura-books:Cap05`

*Obs: Não esquecer de definir a rede em que ele vai subir, se não definir ele vai jogar na rede padrão do docker e não vai conseguir se comunicar com o banco*
