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

# O que é Cloud Computing?
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