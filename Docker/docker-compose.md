## Docker Compose

![image](https://user-images.githubusercontent.com/19577547/141357182-2891c8a0-64e3-4ed1-90f3-e4885be1e736.png)

    version: '3'
    services:
      nginx:
          build:
              dockerfile: ./docker/nginx.dockerfile
              context: .
          image: douglasq/nginx
          container_name: nginx
          ports:
              - "80:80"
          networks: 
              - production-network
          depends_on: 
              - "node1"
              - "node2"
              - "node3"

      mongodb:
          image: mongo
          networks: 
              - production-network

      node1:
          build:
              dockerfile: ./docker/alura-books.dockerfile
              context: .
          image: douglasq/alura-books
          container_name: alura-books-1
          ports:
              - "3000"
          networks: 
              - production-network
          depends_on:
              - "mongodb"

      node2:
          build:
              dockerfile: ./docker/alura-books.dockerfile
              context: .
          image: douglasq/alura-books
          container_name: alura-books-2
          ports:
              - "3000"
          networks: 
              - production-network
          depends_on:
              - "mongodb"

      node3:
          build:
              dockerfile: ./docker/alura-books.dockerfile
              context: .
          image: douglasq/alura-books
          container_name: alura-books-3
          ports:
              - "3000"
          networks: 
              - production-network
          depends_on:
              - "mongodb"

    networks: 
      production-network:
          driver: bridge
          
- **Após o docker-compose.yml pronto, vamos rodar o seguinte comando no terminal** - `docker-compose build`

- **Para subir os container sem o log** - `docker-compose up -d`

- **Para visualizar os serviços que estão rodando** - `docker-compose ps`
