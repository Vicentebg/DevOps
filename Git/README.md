# Principais comandos GIT
`git init`- Iniciar repositório

`git init --bare`- Iniciar repositório em servidor local

`git ls-files`- Listar arquivos

`git status`- Mostrar o status

`git add .`- Adicionar arquivo para a staging area

`git reset HEAD (nome)`- Remove o arquivo da staging area

`git commit -m "Mensagem"`- Salvar mudança e explica-la no "Mensagem"

`git commit -a -m "Mensagem"`- Salvar mudanças pulando a etapa do git add

`git log` - Exibir registro log de mudanças

`git whatchanged`-- Exibir mudanças

`git whatchanged-p`- Exibir mais detalhes de mudanças

`git remote`- Acessar arquivo remoto

`git remote origin diretorio`- Criar diretorio remoto

`git push origin main`- Lançar mudanças do arquivo local para o arquivo remoto

`git pull origin main`- Puxar dados do servidor para o local

`git fetch origin main` - Puxar dados do servidor para o local sem realizar o merge das branchs

`git checkout (branch_nome)`- Selecionar branch para trabalho

`git checkout -b <branch> <commit>`- Cria uma nova branch a partir de um commit

`git checkout -b (branch_nome)`- Cria uma nova branch e ja migra para ela

`git checkout -- (arq_nome)`- Retorna o arquivo ao modo do ultimo commit

`git checkout (tag_nome)`- Seleciona a tag desejada

`git rm (nome)`- Remove o arquivo da staging area

`git tag -a (nome_tag) -m "Mensagem"`- Cria uma tag atual

`git tag`- Exibe a tag atual

`git tag -d (nome_tag)`- Remove a tag selecionada

`git push origin (nome_tag)`- Gera um release na tag

`gitk`- Abrir o relatório visual git

`git branch (nome_branch)`- Cria uma nova branch

`git branch -d (nome_branch)`- Deleta a branch selecionada

`git merge (branch_origen)`- Traz da origin para a branch atual

`touch gitignore`- Criar arquivo para ser ignorado pelo git no repositório

------------------------------------------------------------------------------------

# Dicas:

Ao entrar em um repositório, tanto Github como Gitlab, você pode clicar . e irá carregar o visual studio code cloud

Ou ao entrar em uma pasta e abrir o Git Bash digitar code . o repositório irá abrir no VS Code

------------------------------------------------------------------------------------
Em casos de conflitos de código:
1 - Entrar na sua branch
2 - Executar os dois comandos : git fetch
				git pull origin develop
Puxando as coisas da branch develop pra sua branch
3 - git push para enviar as alterações

3.1 - Se der conflito, utilizar o comando code . para abrir VSCode e tratar os erros.

------------------------------------------------------------------------------------
![Git Cheat Sheet](https://res.cloudinary.com/practicaldev/image/fetch/s--Zib71Fgv--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/n082uxea33j6zq3mca7u.png)
