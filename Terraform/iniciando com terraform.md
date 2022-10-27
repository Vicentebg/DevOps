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
3 - Caso estejamos no linux podemos executar o comando "chmod 400 iac-alura.pem", caso estejamos no Windows precisamos clicar com o botão direito no arquivo pem, ir em Propriedades>Segurança>Avançadas>Desabilitar heranças>Converter as permissões herdadas em permissöes explícitas no objeto.

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

3 - Agora vamos na nossa instância na AWS e iremos pegar o IPv4 dela copia-lo, jogar no navegador e ficará mais ou menos isso http://54.187.241.59:8080/



PLUS: Existem dois comandos para te ajudar que são "terraform fmt" ele formata seu arquivo automáticamente e te retorna o que foi modificado e também tem o comando "terraform validate" que garante se o seu código de configuração está válido.