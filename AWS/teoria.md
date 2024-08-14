# AWS

## Infraestrutura Global AWS

- **Regiões AZ**: Regiões geográficas.
- **Availability Zones**: Datacenters.
- **Local Zones**: Datacenters de menores dimensões, conectado a uma AZ.
- **Wave Length**: Servidor específico de aplicações com baixa latência conectado a uma AZ.
- **Outspots**: Datacenters terceiros (colocations) com servidores AWS.

## AWS IAM

### O que é o AWS IAM?

O AWS Identity and Access Management - IAM permite o gerenciamento seguro do acesso aos serviços e recursos da AWS por meio da criação de usuários, grupos de usuários e permissões.

![image](https://github.com/Vicentebg/DevOps/assets/19577547/d965c4c8-8cdb-46b6-bff5-5a491214bef3)

### Recursos do IAM

- **Acesso compartilhado a contas da AWS**: Fornece permissões de acesso a outros usuários.
- **Permissões granulares**: Usuários podem ter níveis de acesso diferentes de acordo com suas funções em uma conta AWS.
- **MFA**: Autenticação de múltiplos fatores.
- **Identidades federadas**: Credenciais podem ser importadas de outros provedores de identidade.
- **Integração com serviços AWS**: Estabelece níveis de permissões de acesso aos serviços AWS .
- **Gratuito**: O IAM não possui custos ou limites de uso.

### Termos e conceitos do IAM

- **Identity**: Fornece acesso a uma conta na AWS.
- **IAM Users**: Representa uma pessoa ou serviço que utiliza serviços AWS.
  
![image](https://github.com/Vicentebg/DevOps/assets/19577547/f9c51b55-77a3-4d99-bb92-d89ce9268622)

- **User Groups**: Coleção de usuários IAM.

![image](https://github.com/Vicentebg/DevOps/assets/19577547/3c0bd019-7df3-4b05-92ce-85cab791bc76)

- **IAM Roles**: Conjunto de permissões que determinam o nível de acesso de uma identidade aos serviços AWS.
- **Inline policy**: Permissões atreladas diretamente a uma identidade (não são reaproveitáveis).
- **Managed policy**: Conjunto de permissões disponível para várias identidades.
- **IAM Policies**: Define permissões de acesso a serviços AWS.
  
![image](https://github.com/Vicentebg/DevOps/assets/19577547/f97ea3e9-b1e4-4381-819a-df7443068d65)

- **IAM Permissions**: Nível mais baixo da hierarquia, determina se uma identidade pode ou não tomar uma ação sobre um recurso na AWS (Allow/Deny).

### Boas práticas

A AWS tem uma lista de melhores práticas para ajudar desenvolvedores e profissionais de TI a gerenciar o acesso aos recursos da AWS.
- **Conta raiz**: Não utilizá-la em tarefas diárias de desenvolvimento.
- **Usuários**: Crie usuários individuais..
- **Privilégios mínimos**: Prover apenas o nível de acesso necessário.
- **Permissões**: Utilizar grupos de usuários com permissões.
- **Auditoria**: Ativar o AWS CloudTrail.
- **Senhas**: Senhas fortes.
- **MFA**: Ativar para usuários privilegiados.

## Criando usuários no AWS IAM

- Acessar o IAM no Console através do link: https://console.aws.amazon.com/iamv2/home?#/users
- Criar um novo usuário.
- Gerar credenciais de acesso.
- Atribuir permissões ao novo usuário criado.
- Acessar o console da AWS com o novo usuário criado.
- Testar permissões de acesso atribuídas.

## Criando grupos de usuários no AWS IAM

- Para criar grupos de usuários, acesse o seguinte link: https://console.aws.amazon.com/iamv2/home#/groups
- Criar grupos de usuários.
- Atribuir permissões de acesso aos grupos.
- Adicionar usuários aos grupos.
- Testar permissões dos usuários.

## Criando Roles e Policies AWS IAM

Uma política (policy) é um objeto na AWS que, quando associado a uma identidade ou a um recurso, define suas permissões. Uma função (role) é uma identidades da AWS com políticas de permissão que determinam quais ações podem ou não serem executadas na AWS.

![image](https://github.com/Vicentebg/DevOps/assets/19577547/9ac9e61d-5ebc-4fb8-8399-6a3eb42d918e)

- Para criar roles, acesse o seguinte link: https://console.aws.amazon.com/iamv2/home?#/roles
- Para criar policies, acesse o seguinte link: https://console.aws.amazon.com/iamv2/home?#/policies
- Criar políticas com permissões.
- Criar roles com policies atreladas.
- Atribuir as novas roles a usuários.

## O que é Cloud Computing?
**Antes de um mundo com cloud** 
- Modelo cliente servidor
- Ambientes on-premises
- Virtualização

**Principal Benefício de Cloud**
- Pagamento conforme uso (Pay as you go)

## **Cloud Computing é**
A computação em nuvem é a entrega de recursos de TI sob demanda por meio da internet com definição de preço de **pagamento conforme o uso.**

## Benefícios de Cloud Computing
- Troque despesas iniciais por despesas variáveis.
- Pare de tentar adivinhar a capacidade.
- Beneficie-se de enormes economias de escala.
- Aumente a velocidade e agilidade.
- Tenha alcance global em minutos.

## Modelos de Serviço
### O que são modelos de serviço?
- Chamado de modelos de computação em nuvem
- Escolha com base no usuário do serviço e seu objetivo/responsabilidade

#### IaaS
Infraestrutura como serviço. (Amazon EC2)
- Componentes básicos de TI.
- Disco, memória, CPU.
- Usuário: Sysadmin.
- Usuário gerencia .infraestrutura.

#### PaaS
Plataforma como serviço (Elastic Beanstalk).
- Plataforma para implantar (deploy).
- Não se preocupe com infraestrutura.
- Usuário: Desenvolvedores.

#### SaaS
Software como serviço (Gmail)
- Produto completo, executado e gerenciado pelo provedor.
- Não se preocupe com a infraestrutura.
- Pense apenas em utilizar.

## Comparações
![image](https://github.com/Vicentebg/DevOps/assets/19577547/b43d0ddf-6185-49a1-bcac-5b6b0e10959a)

![image](https://github.com/Vicentebg/DevOps/assets/19577547/d033d3f2-8779-4a3a-b8b0-6c7b0ce1dd53)

## Modelos de implantação
### O que são modelos de implantação?
- Modelos de implantação se relaciona com como os recursos de computação estão estruturados e distribuídos.
- Em outras palavras, onde o serviço está implantado.

#### On-premise, Híbrido e Cloud
![image](https://github.com/Vicentebg/DevOps/assets/19577547/98957c57-d55f-4d51-9cef-f73c87ffed21)

# Infraestrutura Global AWS
**Infraestrutura Global AWS é**
- Infraestrutura de datacenters em todo o mundo que fornecem os diversos serviços que você pode utilizar na AWS
- Composto por Regiões e Zonas de disponibilidade
- Vantagens: Alta disponibilidade, tolerância a falhas

![image](https://github.com/Vicentebg/DevOps/assets/19577547/32408575-d135-4a2d-ac35-7ade714d33c3)

## Regiões e Zonas de Disponibilidade

### Regiões
- Locais onde são hospedados os datacenters da AWS.
- Cada **Região** possuem locais isolados chamados de Zonas de Disponibilidade.
- Todas as regiões são conectadas com rede de alta velocidade.
- Isolamento de dados.
- Regulação de dados local.

### Zonas de Disponibilidade
- Também chamadas de AZs (Availability Zones)
- Agrupamento de datacenters isolados dentro de uma **Região**.
- Rede, energia e conectividade redundantes.
- Próximas o suficiente para manter baixa latência, longe o suficiente para evitar que um desastre afete mais de uma AZ.
- Recomendação: Execute pelo menos em duas AZs.

![image](https://github.com/Vicentebg/DevOps/assets/19577547/d2036209-9732-40c0-86a6-5d84539370ce)

## Pontos de presença
- Também chamado de **Edge Locations**, **Locais de Borda** ou **Redes de Borda**.
- Funcionam como pontos específicos pelo globo para distribuir conteúdo de forma rápida.
- Exemplos de serviços que se encontram nos locais de borda: Route 53(DNS), Cloud Front(CDN).

![image](https://github.com/Vicentebg/DevOps/assets/19577547/4e3f51d6-9e97-4a94-92f9-34f51649bc10)

### Amazon CloudFront
- Serviço de entrega de conteúdo: CDN
- Melhora a performance do seu serviço (baixa latência, alta taxa de transferência)
- Provê conteúdo o mais próximo possível do seu usuário.

### Amazon Route 53
- Serviço de DNS.
- Ajuda os clientes a redirecionar corretamente as requisições.

## Provisionamento de recursos na AWS
### Como é possível interagir com serviços AWS?
- Console de gerenciamento
- AWS CLI
- SDKs

#### Console de gerenciamento
![image](https://github.com/Vicentebg/DevOps/assets/19577547/b2497994-aaae-4731-9809-471ca4a601ac)

- https://aws.amazon.com/pt/console/

#### AWS CLI

![image](https://github.com/Vicentebg/DevOps/assets/19577547/1529fc50-3372-4de0-a482-f2f3fe10e5a2)

- Instalado na sua máquina.
- Opera com APIs da AWS através de linha de comando.

#### AWS SDKs
![image](https://github.com/Vicentebg/DevOps/assets/19577547/a63d1a3a-6981-4e50-8605-accfe0dc7ed5)
- Utiliza-se para acessar algum serviço dentro da AWS atráves de alguma aplicação.
- Acesso as APIs AWS atráves de SDK
- SDK possui versões em diversas linguagens como: Java, C#, Go, Python, Javascript.

### Provisionando infraestrutura
#### Elastic Beanstalk

![image](https://github.com/Vicentebg/DevOps/assets/19577547/ec3c259b-757d-4d14-b2dd-958bc57e2430)

- Provisiona a infraestrutura para sua aplicação.

#### CloudFormation

![image](https://github.com/Vicentebg/DevOps/assets/19577547/98f9b103-445b-4fb2-b8dc-14b5872fb496)

- Define a infraestrutura como código IaC.


## Computação em AWS

### [Elastic Compute Cloud - EC2](https://aws.amazon.com/pt/ec2)
#### O que é?
- Servidor virtual na nuvem AWS que possui configurações de memória, CPU, disco, rede e sistema operacional

#### Vantagens
- Capacidade computacional segura e redimensionável.
- Computação: CPU, memória, rede, armazenamento, sistema operacional.
- Definição de preço conforme uso e modalidades específicas a necessidade.
- Instâncias com tipos otimizados para sua atividade.

#### Ciclo de vida

![image](https://github.com/Vicentebg/DevOps/assets/19577547/25957192-1e5d-48a2-a702-e364c11245a0)

#### [Tipos de instância](https://aws.amazon.com/pt/ec2/instance-types/)
- **Uso geral**
    - Equilíbrio de recursos de computação, memória e rede.
    - Indicado para servidores de aplicativo, jogos, backend, banco de dados pequenos.
- **Otimizadas para computação**
    - Ideal para cargas de trabalho que exigem processadores de alto desempenho.
    - Pode ser usado para os mesmos casos de uso da categoria de uso geral mas quando se deseja um melhor desempenho.
    - Ideal também para processamento em lote.
- **Otimizadas para memória**
    - Projeto para alto desempenho no processamento de grandes quantidades de informações na memória.
    - Exemplo: Banco de dados de alto desempenho, processamento em tempo real de dados.
- **Computação acelerada**
    - Usa aceleração de hardware ou coprocessadores para executar algumas funções de forma mais eficiente do que em um software executado direto na CPU.
    - Exemplo: Cálculo de ponto flutuante, processamento de gráficos e correspondência de padrões de dados.
- **Otimizadas para armazenamento**
    - Ideal para cargas de trabalho que exigem acesso de leitura e gravação com grande volume de dados.
    - Exemplo: Sistemas de arquivos distribuídos, Data Warehouse, sistema de processamento de transações online.

#### [User Guide](https://docs.aws.amazon.com/pt_br/AWSEC2/latest/UserGuide/concepts.html)

### [Amazon EC2 AutoScaling](https://aws.amazon.com/pt/ec2/autoscaling)
#### [O que é Escalabilidade?](https://pt.wikipedia.org/wiki/Escalabilidade)
#### O que é?
- Uma instância EC2 que ajusta o uso conforme o uso dos dias, por exemplo de domingo temos mais usuários ele irá prover mais recurso para o domingo.
#### Vantagens
- Provê escalabilidade horizontal(adicionar uma máquina para dividir as requisições) para seus serviços.
- Melhora a tolerância a falhas com identificação de instâncias indisponíveis e implantação multi-AZ
- Melhor gerenciamento de custos

#### Como é a configuração?
![image](https://github.com/Vicentebg/DevOps/assets/19577547/dbc7841b-4e23-4c84-a2d7-a3b907130ac7)

#### Abordagem
- [Scaling Preditivo (conhecer bem o uso do sistema).](https://docs.aws.amazon.com/pt_br/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html)
- [Scaling Dinâmico](https://docs.aws.amazon.com/pt_br/autoscaling/ec2/userguide/as-scale-based-on-demand.html)
- É possível combinar os dois.

### [Elastic Load Balacing - ELB](https://aws.amazon.com/pt/elasticloadbalancing/)
- Balanceamento de carga de aplicação, gateway e rede.
- Escopo regional.
- Escala de forma automática, sem custos.
- Junto ao EC2 AutoScaling permite criar aplicações altamente disponíveis.

### Serviços de mensageria (SQS e SNS)

#### [Amazon Simple Queue Service - SQS](https://aws.amazon.com/pt/sqs)
- Sistema de fila de mensagens.
- Um sistema envia uma mensagem para fila, o outro sistema lê, processa e exclui da fila.

#### [Amazon Simple Notification Service - SNS](https://aws.amazon.com/pt/sns/)
- Sistema pub/sub(publicador e assinante).
- Utiliza tópicos como estrutura.
- Sistema publica mensagens no tópico e assinantes escutam.
- Um exemplo é quando uma compra é autorizada, tem alguns sistemas que interessam para eles essa notificação de compra autorizada, então por exemplo um sistema de envio de e-mail, sms, estoque, todos eles ficam escutando e quando chega essa notificação eles vão enviar e-mails para o cliente, sms, dar baixa no estoque.

[Mais serviços de mensageria AWS](https://aws.amazon.com/pt/messaging/)

### [Computação sem servidor(Servless)](https://aws.amazon.com/pt/lambda/getting-started)

- O termo "sem servidor" ou em inglês "servless" significa que o código é executado em servidores sem que você precise provisionar ou gerenciar esses servidores.
- Capacidade automaticamente ajustada pelo serviço, sem necessidade de nenhuma configuração.

#### [AWS Lambda](https://docs.aws.amazon.com/pt_br/lambda/latest/dg/welcome.html)
- Execução de código sem provisionar servidores.
- Código organizado em funções.
- Você pode escolher a linguagem de programação de sua preferência.
- Executa a partir de eventos ou chamadas diretas a API do Lambda.

##### Como ele funciona?
![image](https://github.com/Vicentebg/DevOps/assets/19577547/b8294d39-770f-4ce8-b8ba-251a87b1efd9)

### [Containers em AWS](https://aws.amazon.com/pt/containers)
#### O que são Containers?
- Forma padrão de empacotar seu aplicativo em um único objetivo.
- Executados como processos isolados.
- Docker.

![image](https://github.com/Vicentebg/DevOps/assets/19577547/bd5a46df-3dc0-4475-8a4d-2588ba818935)

#### Serviços AWS 
- [ECR - Elastic Container Registry](https://aws.amazon.com/pt/ecr)
![image](https://github.com/Vicentebg/DevOps/assets/19577547/45fc1ae1-4bcb-46f5-81e2-b531e071772e)
- [ECS - Elastic Container Service](https://aws.amazon.com/pt/ecs)
![image](https://github.com/Vicentebg/DevOps/assets/19577547/3187e831-72d9-47d1-a9e7-f7ed1d451060)
- [EKS - Elastic Kubernetes Service](https://aws.amazon.com/pt/eks)
![image](https://github.com/Vicentebg/DevOps/assets/19577547/2f38b4ad-afe1-47e2-97ff-1b8a9d86074e)
- [AWS Fargate](https://aws.amazon.com/pt/fargate/)
![image](https://github.com/Vicentebg/DevOps/assets/19577547/f2a66288-ce7a-4991-b0b5-9e398c334b3e)

# Redes AWS
#### [Amazon VPC](https://aws.amazon.com/pt/vpc/)
- VPC: Virtual Private Cloud
- Permite construir e configurar redes virtuais na AWS
- Sub-redes: privadas e públicas (Privada: Um banco de dados que conecta em duas instancias EC2 não necessita de acesso a internet.)
- "Tudo começa dentro de um VPC"

##### Caso de uso
![image](https://github.com/user-attachments/assets/3f8bc38b-2174-43e8-bef5-ac3bd8dba8ce)

##### Materias de apoio
- https://www.youtube.com/watch?v=3UCwOfHKZ38&ab_channel=DouglasMugnos
- https://docs.aws.amazon.com/pt_br/vpc/latest/userguide/what-is-amazon-vpc.html

#### Conectividade com AWS

##### Conecte sua VPC e a Internet
![image](https://github.com/user-attachments/assets/a479d78d-6c74-48bf-89ec-9525e1465d2c)
- O conector roxo significa que está conectando a internet na sub-rede pública(IGW ou Gateway da Internet)

##### Conecte sua VPC a sub-redes privadas
![image](https://github.com/user-attachments/assets/656acace-43da-4286-8777-8741ac6f4c5d)

##### AWS Direct Connect
- Conexão dedicada do meu escritório até a nuvem.
![image](https://github.com/user-attachments/assets/2a416a79-e664-48f1-8f64-d69395876391)

##### Materias de apoio
- https://docs.aws.amazon.com/pt_br/vpc/latest/userguide/VPC_Internet_Gateway.html
- https://www.youtube.com/watch?v=-e2yw1STfNo&ab_channel=GuilhermeTeles
- https://docs.aws.amazon.com/pt_br/vpc/latest/userguide/vpn-connections.html

#### Sub-redes e listas de controle de acesso
- Como dados trafegam em uma VPC?
![image](https://github.com/user-attachments/assets/89e7e05a-2e0c-4845-94c9-12802c54d95c)

##### Network ACLs
![image](https://github.com/user-attachments/assets/76ae220a-e895-49a0-924f-b435d6cabf23)
- Prove controle de tráfego de entra e saída de sub-redes.
- Comportamento Stateless (Não guarda estado, tem regras para entrada e saída de dados, por exemplo um banco de dados pedindo para se conectar, ele vai verificar se está na regra dele permitir esta conexão, uma consulta ao banco de dados, ele vai verificar se tem uma regra de saída de dados para te fornecer os resultados da consulta).
- Por padrão, permite todo tráfego de entrada e saída.

##### Segurança para recursos
![image](https://github.com/user-attachments/assets/c8b8552a-e593-4f77-8ff7-5c2b78e00967)

##### Grupos de segurança
![image](https://github.com/user-attachments/assets/2378d9f0-ce31-4146-bef5-2820f3eb1acd)
- Controle de tráfego de entrada e saída de instância EC2.
- Comportamento Stateful (Uma vez que um pacote chega até a entrada e ele é permitido entrar na instancia EC2,as regras definidas para entrada elas também servem para saída)
- Por padrão, nega todo o tráfego de entrada e permite todo tráfego de saída.

##### Materias de apoio
- https://docs.aws.amazon.com/pt_br/vpc/latest/userguide/vpc-network-acls.html
- https://docs.aws.amazon.com/pt_br/vpc/latest/userguide/vpc-security-groups.html

#### Revisão 
![image](https://github.com/user-attachments/assets/fa88adfe-8f71-4c3b-845e-fb598caeaad8)