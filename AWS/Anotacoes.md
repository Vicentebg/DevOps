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

### Elastic Compute Cloud - EC2
#### O que é?
- Servidor virtual na nuvem AWS que possui configurações de memória, CPU, disco, rede e sistema operacional

#### Vantagens
- Capacidade computacional segura e redimensionável.
- Computação: CPU, memória, rede, armazenamento, sistema operacional.
- Definição de preço conforme uso e modalidades específicas a necessidade.
- Instâncias com tipos otimizados para sua atividade.

#### Ciclo de vida

![image](https://github.com/Vicentebg/DevOps/assets/19577547/25957192-1e5d-48a2-a702-e364c11245a0)

#### Tipos de instância
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

### Amazon EC2 AutoScaling
#### O que é?
- Uma instância EC2 que ajusta o uso conforme o uso dos dias, por exemplo de domingo temos mais usuários ele irá prover mais recurso para o domingo.
#### Vantagens
- Provê escalabilidade horizontal(adicionar uma máquina para dividir as requisições) para seus serviços.
- Melhora a tolerância a falhas com identificação de instâncias indisponíveis e implantação multi-AZ
- Melhor gerenciamento de custos

#### Como é a configuração?
![image](https://github.com/Vicentebg/DevOps/assets/19577547/dbc7841b-4e23-4c84-a2d7-a3b907130ac7)

#### Abordagem
- Scaling Preditivo (conhecer bem o uso do sistema).
- Scaling Dinâmico 
- É possível combinar os dois.

### Elastic Load Balacing - ELB
- Balanceamento de carga de aplicação, gateway e rede.
- Escopo regional.
- Escala de forma automática, sem custos.
- Junto ao EC2 AutoScaling permite criar aplicações altamente disponíveis.

### Serviços de mensageria