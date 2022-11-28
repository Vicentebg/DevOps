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

2 - Agora iremos rodar nosso servidor web com o comando `nohup busybox httpd -f -p 8080 &`

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
 Agora dentro da máquina Ubuntu execute o comando `cd../../mnt/c` e agora rode o comando `sudo ansible-playbook playbook.yml -u ubuntu --private-key iac-alura.pem -i hosts.yml`
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

# Ansible e Python

Agora vamos criar um outro playbook

#### **playbook.yml**
```yaml
- hosts: terraform-ansible
  tasks:
  - name: Instalando python3 e virtualenv
    apt:
      pkg:
      - python3
      - virtualenv
      update_cache: yes
  become: yes
```
Vamos mudar o nome da nossa instancia no arquivo `main.tf` irei colocar Ansible e Python, em seguida vamos rodar o comando `terraform destroy` logo após acabar essa tarefa iremos rodar `terraform apply` , iremos até a instancia nova criada, iremos pegar o IPv4 público dela e coloca-lo no nosso arquivo `hosts.yml` , e agora vamos para nosso Ubuntu WSL e vamos rodar novamente o comando `sudo ansible-playbook playbook.yml -u ubuntu --private-key iac-alura.pem -i hosts.yml` , logo após o termino podemos realizar o acesso via ssh da máquian e rodar os comandos `python3 --version` e `virtualenv --version` para verificar se foi instalado corretamente na nossa máquina

# Ansible com virtualenv e django

Agora vamos criar um ambiente de desenvolvimento o django, iremos alterar nosso playbook conforme mostra abaixo:

#### **playbook.yml**
```yaml
- hosts: terraform-ansible
  tasks:
  - name: Instalando python3 e virtualenv
    apt:
      pkg:
      - python3
      - virtualenv
      update_cache: yes
    become: yes
  - name: Instalando dependencias com pip (Djando e Django Rest)
    pip:
      virtualenv: /home/ubuntu/tcc/venv
      name:
        - django
        - djangorestframework
```

Logo após fazer todo o procedimento padrão, vamos acessar a máquina via SSH e verificar se a pasta tcc foi criada e agora vamos rodar o comando `. venv/bin/activate` e estaremos dentro do "ambiente virtual" criado pela venv, vamos rodar também para averiguar os pacotes instalados na nossa venv o comando `pip freeze` e com isso iremos certificar as versões dos pacotes django.

Agora vamos iniciar um projeto dentro da venv com o comando `djando-admin startproject setup .` e agora vamos rodar o comando `python manage.py runserver 0.0.0.0:8000`. Agora podemos pegar o IPv4 da nossa máquina colar ele no navegador passando por exemplo: 43.23.42.12:8000.

Essa página que está aparecendo nos alertas que possuem hosts que não estão permitidos(DisallowedHost) no nosso django, então vamos ter que dar a permissão, para isso pare o servidor e acesse `/home/ubuntu/tcc/setup` e agora `vi settings.py`

Dentro do arquivo settings.py vamos edita-lo na parte ALLOWED_HOSTS, ficará igual na abaixo:

![image](https://user-images.githubusercontent.com/19577547/201756129-68ac8983-bd1c-4616-b946-ce9a5deae391.png)

Após alterar está configuração, vamos salvar o arquivo e voltar uma pasta e executar o comando `python manage.py runserver 0.0.0.0:8000` novamente e agora será apresentado uma tela de sucesso para gente.

Agora vamos sair da venv utilizando o comando `deactivate`. Vamos também utilizar o comando `rm -rf manager.py setup/` para limpar nossa VM.

# Iniciando projeto via Ansible
Agora vamos configurar um novo playbook com os passos que fizemos manualmente anteriormente, porém vamos utilizar a tag shell para rodar estes comandos, lembrando que o ; é para executar dois comandos seguidos no mesmo shell, se não utilizarmos o ; ele rodará um comando independente do outro, não salvando seu estado. Neste caso queremos que ele tenha essa dependencia e então por isso utilizaremos o ponto e vírgula.
```yaml
- hosts: terraform-ansible
  tasks:
  - name: Instalando python3 e virtualenv
    apt:
      pkg:
      - python3
      - virtualenv
      update_cache: yes
    become: yes
  - name: Instalando dependencias com pip (Djando e Django Rest)
    pip:
      virtualenv: /home/ubuntu/tcc/venv
      name:
        - django
        - djangorestframework
  - name: Iniciando projeto
    shell: '. /home/ubuntu/tcc/venv/bin/activate; django-admin startproject setup /home/ubuntu/tcc'
  ```

  Agora só repetir os passos de executar o playbook novamente e entrar via SSH.

  Agora navegando dentro da VM podemos ver que o manager.py e a pasta setup foram criadas automáticamente.

Iremos agora deixar que o nosso playbook faça toda a etapa anterior que fizemos manualmente, como alterar o ALLOWED_HOSTS.

```yaml
- hosts: terraform-ansible
  tasks:
  - name: Instalando python3 e virtualenv
    apt:
      pkg:
      - python3
      - virtualenv
      update_cache: yes
    become: yes
  - name: Instalando dependencias com pip (Djando e Django Rest)
    pip:
      virtualenv: /home/ubuntu/tcc/venv
      name:
        - django
        - djangorestframework
  - name: Iniciando projeto
    shell: '. /home/ubuntu/tcc/venv/bin/activate; django-admin startproject setup /home/ubuntu/tcc'
  - name: Alterando o host do settings
    lineinfile:
      path: /home/ubuntu/tcc/setup/settings.py
      regexp: 'ALLOWED_HOSTS'
      line: 'ALLOWED_HOSTS = ["*"]'
      backrefs: yes
  ```
Para se alterar alguma coisa dentro de um arquivo precisamos utilizar o comando lineinfile do Ansible, em seguida vamos passar o arquivo do arquivo a ser editado no caso settings.py, como boa prática passamos todo o caminho para não ocorrer problemas. No comando regexp vamos colocar o que estamos buscando que no caso é ALLOWED_HOSTS e logo abaixo com o comando line vamos colocar o que queremos mudar, ou seja ele vai buscar pela linha onde contém ALLOWED_HOSTS e mudar a para ALLOWED_HOSTS = ["*"], também utilizados aspas duplas dentro do colchetes para não "atrapalhar" o funcionamento do comando, então podemos partir do princípio de aspas simples fora, utiliza-se aspas duplas dentro ou vice versa.
 O parametro backrefs serve para se ele não achar nada dentro do nosso arquivo ele não irá fazer nada.

 Também podemos adicionar o comando `ignore_errors: yes` abaixo do backrefs para que ele substitua os arquivos dentro da nossa VM, por padrão caso tenha algum arquivo que nosso playbook queira criar igual ou substituir ele irá apresentar um erro para que não se perca o que já tem, caso não seja a prioridade passamos esté comando para que possamos executar nosso playbook quantas vezes quisermos sem problema de erro. Porém tome cuidado pois pode comprometer a integridade de algum projeto.

 Bom agora basta acessar a máquina e certificar de que tudo foi criado corretamente!
