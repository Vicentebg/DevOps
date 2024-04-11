# AWS CLI

# Listas instâncias

`aws ec2 describe-instances`

# Criar instância

`aws ec2 run-instances --image-id "ami-0323c3dd2da7fb37d" --count 1 --instance-type "t2.micro" --key-name "MyKeySSH" --security-group-ids "sg-0529062a5d07f8eab" --subnet-id "subnet-1deb2d7c"`

Obs: Remover as aspas

# Terminar instância

`aws ec2 terminate-instances --instance-ids "id-xyz"`

# Acesso SSH

`ssh -i "caminho da chave pem" ec2-user@ip`

Exemplo: `ssh -i C:\Users\Vicente\Desktop\MyKeySSH.pem ec2-user@175.31.93.179`