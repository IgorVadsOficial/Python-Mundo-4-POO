class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f"Olá, sou {self.nome} e eu sou {self.cargo} no setor de {self.setor} da empresa Curso em Video.\n"


c1 = Funcionario("Maria", "Administração", "Diretora")
print(c1.apresentacao())

c2 = Funcionario("Pedro", "TI", "Programador")
print(c2.apresentacao())
