#!/bin/bash

### Criando diretórios ###
echo "Criando diretórios"

mkdir /publico
mkdir /adm
mkdir /ven
mkdir /sec

### Criando grupos ###
echo "Criando grupos"

groupadd GRP_ADM
groupadd GRP_VEN
groupadd GRP_SEC

### Criando usuários ###
echo "Criando usuários"

# GRP_ADM #
echo "Adicionando usuários ao grupo GRP_ADM"

useradd carlos -m -c "Carlos" -s /bin/bash -p $(openssl passwd -crypt Senha123) -G GRP_ADM
useradd maria -m -c "Maria" -s /bin/bash -p $(openssl passwd -crypt Senha123) -G GRP_ADM
useradd joao -m -c "João" -s /bin/bash -p $(openssl passwd -crypt Senha123) -G GRP_ADM

# GRP_VEN #
echo "Adicionando usuários ao grupo GRP_VEN"

useradd debora -m -c "Debora" -s /bin/bash -p $(openssl passwd -crypt Senha123) -G GRP_VEN
useradd sebastiana -m -c "Sebastiana" -s /bin/bash -p $(openssl passwd -crypt Senha123) -G GRP_VEN
useradd roberto -m -c "Roberto" -s /bin/bash -p $(openssl passwd -crypt Senha123) -G GRP_VEN

# GRP_SEC #
echo "Adicionando usuários ao grupo GRP_SEC"

useradd josefina -m -c "Josefina" -s /bin/bash -p $(openssl passwd -crypt Senha123) -G GRP_SEC
useradd amanda -m -c "Amanda" -s /bin/bash -p $(openssl passwd -crypt Senha123) -G GRP_SEC
useradd rogerio -m -c "Rogerio" -s /bin/bash -p $(openssl passwd -crypt Senha123) -G GRP_SEC

### Administrando permissões dos diretórios ###
echo "Administrando permissões dos diretórios"

chown root:GRP_ADM /adm
chown root:GRP_VEN /ven
chown root:GRP_SEC /sec

chmod 770 /adm
chmod 770 /ven
chmod 770 /sec
chmod 777 /publico

echo "Finalizando o script"