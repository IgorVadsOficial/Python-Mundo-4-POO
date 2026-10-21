class Pessoa:
    def __init__(self, nome=" ", idade=0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome=" ", idade=0, curso="", turma=""):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def aniversario(self):
        return super().aniversario()

    def fazer_matricula(self):
        pass


class Professor(Pessoa):
    def __init__(self, nome=" ", idade=0, especialidade="", nivel=0):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def aniversario(self):
        return super().aniversario()

    def dar_aula(self):
        pass


class Funcionario(Pessoa):
    def __init__(self, nome=" ", idade=0, cargo="", setor=""):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def aniversario(self):
        return super().aniversario()

    def bater_ponto(self):
        pass
