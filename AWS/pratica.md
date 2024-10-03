# Prática AWS 1
## O que será feito
![image](https://github.com/Vicentebg/DevOps/assets/19577547/4c04dd1f-f290-416e-be1e-7cac60d53089)

## Arquitetura da prática
![image](https://github.com/Vicentebg/DevOps/assets/19577547/8609257a-d86e-4695-bf65-612416a39bf2)

## Roteiro
- Criar tabela no DynamoDB
    - Inserir item de demonstração
- Criar função lambda
    - Permissões de escrita no DynamoDB
- Criar API com rotas no API Gateway
    - Integração com a função lambda

Obs: Se atentetar as regiões dos serviços.

- Serviços relevantes
    - Cognito
    - EC2
    - Amplify
    - RDS
    - S3

## Hands On
### DynamoDB
- Procurar DynamoDB no search da AWS e entrar no serviço.
- Criar tabela
- Nome: Product
- Chave de partição: id [String]
- Configuração padrão
- Criar tabela
- Após criar a tabela vamos acessar nossa tabela "Product" e ir no botão laranja "Explorar itens da tabela" e depois em "Criar item"
- Vamos criar um item do tipo String chamado "prod01" e o nome do atributo será "id", e um tipo String chamado "Batata" e o nome do atributo será "name.
- E agora vamos criar outro item mas com o nome de "prod02"e "Laranja"
![image](https://github.com/Vicentebg/DevOps/assets/19577547/936492fb-7eb0-4707-a9a9-5bd79caf5d30)
- Logo após ter criado vamos selecionar a caixa de "Consulta" e procurar por "prod01" e agora vemos ele retornar nosso prod01.

### Lambda
- Procurar Lambda no search da AWS e entrar no serviço.
- Vamos no botão "Criar uma função"
- Deixe na opção "Criar do zero
- No nome irei utilizar "DioDemoFunction" "
- No meu caso "Node.js 16.x"
- Arquitetura x86_64
- Agora "Criar função"
- Agora vamos editar o index.js
```
const AWS = require("aws-sdk");

const dynamo = new AWS.DynamoDB.DocumentClient();

exports.handler = async (event, context) => {
  let body;
  let statusCode = 200;
  const headers = {
    "Content-Type": "application/json"
  };
  
  
  let requestJSON;

  try {
    switch (event.routeKey) {
      case "POST /items":
        requestJSON = JSON.parse(event.body);
        await dynamo
          .put({
            TableName: "Product",
            Item: {
              id: requestJSON.id,
              price: requestJSON.price,
              name: requestJSON.name
            }
          })
          .promise();
        body = `Put item ${requestJSON.id}`;
        break;
      case "DELETE /items/{id}":
        console.log(event.pathParameters.id)
        await dynamo
          .delete({
            TableName: "Product",
            Key: {
              id: event.pathParameters.id
            }
          })
          .promise();
        body = `Deleted item ${event.pathParameters.id}`;
        break;
      case "GET /items/{id}":
        body = await dynamo
          .get({
            TableName: "Product",
            Key: {
              id: event.pathParameters.id
            }
          })
          .promise();
        break;
      case "GET /items":
        body = await dynamo.scan({ TableName: "Products" }).promise();
        break;
      case "PUT /items/{id}":
         requestJSON = JSON.parse(event.body);
        await dynamo
          .update({
            TableName: "Product",
            Key: {
              id: event.pathParameters.id
            },
            UpdateExpression: 'set price = :r',
            ExpressionAttributeValues: {
             ':r': requestJSON.price,
            },
          })
          .promise();
        body = `Put item ${event.pathParameters.id}`;
        break;
      default:
        throw new Error(`Unsupported route: "${event.routeKey}"`);
    }
  } catch (err) {
    statusCode = 400;
    body = err.message;
  } finally {
    body = JSON.stringify(body);
  }

  return {
    statusCode,
    body,
    headers
  };
};
```
[Fonte](https://github.com/cassianobrexbit/dio-live-coding-aws)

- Logo após colar o código vamos clicar em "Deploy"

- Agora vamos clicar em "DioDemoFunction" -> Configuração -> "Permissões" -> clique no link do "Nome da função", ele irá encaminhar para a interface do IAM
- Agora vamos em "Adicionar permissões" -> "Anexar políticas" -> Procure por "dynamodb" e selecione a política "AmazonDynamoDBFullAccess"

### API Gateway
- Procurar API Gateway no search da AWS e entrar no serviço.
- Selecione "API HTTP" -> "Compilar"
- Dar um nome, vou usar "DIODemoAPI"
- Na parte de rotas só vamos "Avançar" e estágios também.
- Agora vamos clicar em "Criar"
- Após ter criado vamos em "Routes" do lado esquerdo do painel.
- Vamos criar da seguinte forma:
    - POST /items
    - DELETE /items/{id}
    - GET /items
    - GET /items/{id}
    - PUT /items/{id}
![image](https://github.com/Vicentebg/DevOps/assets/19577547/aea6ab84-d4d4-48c6-8a6d-fc0e52a31330)

### Desenvolvendo as integrações

- Agora para integrar vamos clicar no primeiro GET e "Anexar integração" -> "Criar e anexar uma integração" -> "Tipo de integração" -> "Função do Lambda"
- Verifique se a região seleciona é a mesma que a você criou o Lambda, clique na caixa da lupa e selecione sua função lambda que foi criada anteriormente e depois clique no botão "Criar".
- Agora vamos clicar nos outros metódos e selecionar a caixa "Escolher uma integração existente", selecione a integração que criou agora e clique no botão "Anexar integração".
- Agora vamos utilizar o Postman para testar, se quiser pode usar o de sua preferência.
- Primeiramente vamos clicar no lado esquerdo do painel onde no meu caso está escrito "API:DIODemoAPI...(njp7i89o23)"
- Vamos copiar a URL do campo "Invocar URL"
- Agora vamos colar essa URL no Postman e inserir no final /items
![image](https://github.com/Vicentebg/DevOps/assets/19577547/56132bc1-9716-49d3-adc6-3c7fe8662496)
- Com isso inserimos um item na nossa tabela, também podemos consultar ele
![image](https://github.com/Vicentebg/DevOps/assets/19577547/346e6177-45e5-4fc9-ac33-f21664ea76b4)
