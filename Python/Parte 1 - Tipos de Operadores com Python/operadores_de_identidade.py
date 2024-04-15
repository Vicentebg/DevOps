# Servem para comparar se dois os dois objetos testados ocupam a mesma posição na memória

curso = "Curso de Python"
nome_curso = curso
saldo, limite =  200, 200

curso is nome_curso # True

curso is not nome_curso # False

saldo is limite # True

