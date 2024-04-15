# De acordo com uma convençao em Python as boas práticas de indentação
# É indiciado usar 4 espaços em branco por nível de indentação
# Ou seja cada novo bloco adicionamos 4 novos espaços em branco
def sacar (self, valor: float) -> None: # inicio do bloco do método
    
    if self.saldo >= valor: #inicio do bloco do if

        self.saldo -= valor

    # fim do bloco do if

# fim do bloco do método