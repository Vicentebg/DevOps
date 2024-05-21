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

- **Acesso compartilhado a contas da AWS**: Forneces permissões de acesso a outros usuários.
- **Permissões granulares**: Usuários podem ter níveis de acesso diferentes de acordo com suas funções em uma conta AWS
- **MFA**: Autenticação de múltiplos fatores
- **Identidades federadas**: Credenciais podem ser importadas de outros provedores de identidade
- **Integração com serviços AWS**: Estabelece níveis de permissões de acesso aos serviços AWS 
- **Gratuito**: O IAM não possui custos ou limites de uso

### Termos e conceitos do IAM

- **Identity**: Fornece acesso a uma conta na AWS.
- **IAM Users**: Representa uma pessoa ou serviço que utiliza serviços AWS.
  
![image](https://github.com/Vicentebg/DevOps/assets/19577547/f9c51b55-77a3-4d99-bb92-d89ce9268622)

- **User Groups**: Coleção de usuários IAM.

![image](https://github.com/Vicentebg/DevOps/assets/19577547/3c0bd019-7df3-4b05-92ce-85cab791bc76)

- **IAM Roles**: Conjunto de permissões que determinam o nível de acesso de uma identidade aos serviços AWS.
- **Inline policy**: permissões atreladas diretamente a uma identidade (não são reaproveitáveis)
- **Managed policy**: Conjunto de permissões disponível para várias identidades.
- **IAM Policies**: Define permissões de acesso a serviços AWS.
  
![image](https://github.com/Vicentebg/DevOps/assets/19577547/f97ea3e9-b1e4-4381-819a-df7443068d65)

- **IAM Permissions**: Nível mais baixo da hierarquia, determina se uma identidade pode ou não tomar uma ação sobre um recurso na AWS (Allow/Deny).
