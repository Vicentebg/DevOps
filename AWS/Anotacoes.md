# Anotações AWS

1 - Procurar por IAM e configurar MFA(Multifator de autenticação)

2 - aws sts get-caller-identity (Para ver os usuários que estão validados busca so os default) ou aws sts get-caller-identity —profile vicente (para procurar um perfil especifico)

3 - Criar um grupo com as politicas desejadas e posteriormente adicionar usuário ao grupo e criar a chave de acesso

4 - Configurar AWS CLI com o comando aws configure, depois inserir a Chave de Acesso, depois a Chave de acesso secreta, depois a região (prestar atenção pois o IAM é global, observar a região clicando para ir no menu inicial da AWS), depois preencher o output com json ou text

5 - Para saber se foi configurado corretamente: aws configure list

6 - cat ~/.aws/config (consegue visualizar a região) 

7 - cat ~/.aws/credentials (consegue visualizar as chaves de acesso)

8  - Para configurar um profile: aws configure --profile vicente

9 - (Stop Protection/Shutdown Behavior/Termination Protection)

Clicar com o botão direito em cima da instancia → Configurações da instancia → Alterar proteção contra interrupção → Habilitar Checkbox e estará habilitado a proteção (Stop Protection)