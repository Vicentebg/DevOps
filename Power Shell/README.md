# Prompt de Comando ou Power Shell

- `echo Hello World` - Escreve no terminal

- `dir` - Mostrar os arquivos de dentro da pasta

- `cd Desktop` - Entrar dentro de alguma pasta

- `mkdir Dicas` - Para criar pasta

- `rmdir Dicas` - Para deletar a pasta

- `move dica.txt Dicas` - Para mover um arquivo

- `type dica.txt` - Para ler um arquivo

- `echo O comando cd alterna entre pastas! > dica4.txt` - Para escrever a mensagem em algum arquivo, o > redireciona o lugar em que quero escrever, caso o arquivo não exista ele irá criar, caso eu queira inserir dados em algum arquivo já existente, posso utilizar o >>

- `cd ..` - Para voltar um pasta

- `copy logo-alura.png logo-alura2.png` - Para copiar algum arquivo

- `rename logo-alura2.png logo-alura-backup.png` - Para renomear o nome de algum arquivo

- `del logo-alura.png` - Deletar arquivo

- `cls` - Limpar a tela

- `help dir` - Dá mais informações sobre algum comando, neste caso o dir

- `tree` - Mostra as pastas e subpastas organizadas em uma árvore

- `more arquivo.txt` - Irá ler um arquivo também igual ao type, mas irá exibir uma página de cada vez

------------------------------------------------------------------------------------
## Criando um script:

Rodar o comando echo cls > script.bat ou criar um arquivo .bat

## Script
```
cls
echo Realmente quer fazer backup?
pause

cls
echo ok, fazendo backup...
cd C:\Users\caelum
mkdir backup

xcopy /E /Y "C:\Users\caelum\codigo" "C:\Users\caelum\backup"  

echo Listando os arquivos do backup
dir C:\Users\caelum\backup
```
--------------------------------------------------------------
## Explicando o script

O pause pede uma interação do usuário para continuar o script, neste caso pede para que o usuário aperte uma tecla para dar continuidade no processo

O comando xcopy é para copiar pastas e sub-pastas desde que usamos o parametro /e (copia subpastas) e /y (confirma automaticamente a sobrescrita de arquivos).

Se também começarmos nosso script com @echo off as mensagens irão aparecer de forma mais limpa, exemplo de script com @echo off

--------------------------------------------------------------
## Script
```
@echo off
cls
echo Dia de hoje:
echo %date%
echo Hora atual:
echo %time%
```

## Dica: Instalar cmder para uma interface melhor e alguns funções a mais