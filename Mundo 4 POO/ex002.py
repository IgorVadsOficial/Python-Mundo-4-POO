class Gafanhoto:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade = self.idade + 1

    def __str__(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."


g1 = Gafanhoto("Maria", 17)
g1.aniversario()
print(g1)