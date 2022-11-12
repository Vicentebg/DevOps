# Iniciando com terraform
1 - Utilizaremos AWS, podemos configurar no EC2 da AWS uma máquina Ubuntu Server

2 - Para isso precisamos primeiramente instalar o AWS CLI `https://docs.aws.amazon.com/pt_br/cli/latest/userguide/getting-started-install.html`
e depois rodar o comando aws configure no PowerShell, será pedido o AWS Acess Key ID e o AWS Secret Acess Key, para configurar os seus iremos nessa página `https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1&skipRegion=true#/security_credentials` no campo "Chaves de acesso (ID da chave de acesso e a chave de acesso secreta)" iremos em "Criar nova chave de acesso".

3 - Teremos esse código fornecido pela própria Hashicorp - https://developer.hashicorp.com/terraform/tutorials/aws-get-started/aws-build

Iremos criar um arquivo chamado "main.tf" e colocaremos o código abaixo neste arquivo.

```yaml
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "us-west-2"
}

resource "aws_instance" "app_server" {
  ami           = "ami-830c94e3"
  instance_type = "t2.micro"

  tags = {
    Name = "Primeira instancia"
  }
}
```
4 - Precisamos mudar apenas alguns parametrôs como o ami que será apresentado na AWS e também o parametro tags.

5 - Agora iremos dar o comando "terraform init" e logo em seguida o "terraform plan" e depois "terraform apply" e vamos passar depois em "Enter a value:" yes

# Acessando via SSH
1 - Primeiramente precisamos ir até a interface da AWS ir em Redes e segurança > Pares de chave, vamos gerar uma chave com um nome da sua escolha, pode escolher o formato de criptografia que você quiser e após isso vamos selecionar o formato .pem que é o padrão do Ubuntu, vamos salvar o arquivo na mesma pasta do nosso "main.tf"

2 - Vamos adicionar na nossa parte de resource um atributo chamado key_name ficará assim: 
```yaml
resource "aws_instance" "app_server" {
  ami           = "ami-017fecd1353bcc96e"
  instance_type = "t2.micro"
  key_name = "iac-alura"
  tags = {
    Name = "Primeira instancia"
  }
}
```
3 - Caso estejamos no linux podemos executar o comando `chmod 400 iac-alura.pem`, caso estejamos no Windows precisamos clicar com o botão direito no arquivo pem, ir em Propriedades>Segurança>Avançadas>Desabilitar heranças>Converter as permissões herdadas em permissöes explícitas no objeto.

4 - Agora vamos voltar para a AWS em Redes e segurança>Security groups>Regras de entrada>Editar regras de entrada>Adicionar regra (Regras de entrada) e Redes e segurança>Security groups>Regras de saída>Editar regras de saída>Adicionar regra (Regras de saída)

5 - Em tipo iremos setar da seguinte maneira(Regras de entrada):
<br>Tipo: Todo o tráfego <br/> Origem: Qualquer local-IPv4 <br/>
<br>Tipo: Todo o tráfego <br/> Origem: Qualquer local-IPv6

6 - Em tipo iremos setar da seguinte maneira(Regras de saída):
<br>Tipo: Todo o tráfego <br/> Origem: Qualquer local-IPv4 <br/>
<br>Tipo: Todo o tráfego <br/> Origem: Qualquer local-IPv6

7 - Agora vamos no painel da AWS novamente em Instâncias>Instâncias>Selecionar a instância desejada> Conectar > Copiar o comando de exemplo SSH e colar em seu terminal após isso dar yes e pronto, você terá conseguido realizar o acesso via SSH,

# Criando um servidor web
1 - Após realizarmos o acesso SSH iremos dar o seguinte comando `echo "<h1> Ola mundo </h1>" > index.html` depois podemas dar um `cat index.html` para verificar se foi criado corretamente.

2 - Agora iremos rodar nosso servidor web com o comando nohup `busybox httpd -f -p 8080 &`

3 - Agora vamos na nossa instância na AWS e iremos pegar o IPv4 dela copia-lo, jogar no navegador e colocar a porta em que criamos o busybox e ficará mais ou menos isso 54.187.241.55:8080

`PLUS: Existem dois comandos para te ajudar que são "terraform fmt" ele formata seu arquivo automáticamente e te retorna o que foi modificado e também tem o comando "terraform validate" que garante se o seu código de configuração está válido.`

# Ansible com Terraform
1 - Para utilizar o Ansible no Windows precisaremos instalar o WSL:

Abra o PowerShell em modo Administrador e rode o comando  `wsl --instal -d Ubuntu`
<br> Reinicie o computador e execute o Ubuntu for Windows, rode dentro dele os comandos `sudo apt update && sudo apt install ansible`

2 - Vamos voltar para nossa pasta aonde está o arquivo "main.tf", iremos criar mais dois arquivos: "hosts.yml" e "playbook.yml" 

#### **hosts.yml**
```yaml
[terraform-ansible]
18.236.162.130
```
#### **playbook.yml**
```yaml
- hosts: terraform-ansible
  tasks:
  - name: criando arquivo
    copy: 
      dest: /home/ubuntu/index.html
      content: <h1> Feito com terraform e ansible </h1>
  - name: criando servidor
    shell: "nohup busybox httpd -f -p 8080 &"
```
 Agora dentro da máquina Ubuntu execute o comando `cd../../mnt/c` e agora rode o comando `ansible-playbook playbook.yml -u ubuntu --private-key iac-alura.pem -i hosts.yml`
<br>Obs: O IP inserido no arquivo hosts vai ser de acordo com o IPv4(Público) que está em sua instancia.

`Plus: Se estiver no Windows provavelmente dará problema na chave .pem, você terá que configurar o arquivo para de funcione, você pode tentar entrar em modo root para rodar o comando ssh via WSL, caso de errado pode-se tentar rodar o comando chmod 400 iac-alura.pem ou chmod 600 iac-alura.pem`

Você irá até o arquivo que possuí a chave e irá clicar botão direito Propriedades>Segurança>Avançadas, irá deletar todos os usuários e irá criar um conforme a imagem 2.
Na imagem 3 mostra como se deve ficar as permissões do arquivo para visualizar as permissões basta dar o comando `grep || ll`

Imagem 1

![image](https://user-images.githubusercontent.com/19577547/201449639-cbf4811f-dec4-4004-afb8-06d410a4c818.png)

Imagem 2 <br>
![image](https://user-images.githubusercontent.com/19577547/201449700-1f116b5a-c029-4246-8fa6-123505420bd3.png)

Imagem 3 <br>
![image](https://user-images.githubusercontent.com/19577547/201449718-4251bec8-2751-4875-ab4d-093673bfe0ec.png)

