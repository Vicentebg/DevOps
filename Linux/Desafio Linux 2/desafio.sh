#!/bin/bash

### Iniciando o Script ###

echo "Iniciando o Script"

### Atualizando Servidor ###

echo "Atualizando Servidor"
apt-get update
apt-get upgrade -y

### Instalando Apache ###

echo "Instalando Apache"
apt-get install apache2 -y

### Instalando Unzip ###

echo "Instalando Unzip"
apt-get install unzip -y

### Baixando aplicação ###

echo "Baixando aplicação"
cd /tmp
wget https://github.com/denilsonbonatti/linux-site-dio/archive/refs/heads/main.zip
unzip main.zip
cd linux-site-dio-main

### Copiando arquivos ###

echo "Copiando arquivos"
cp -R * /var/www/html/