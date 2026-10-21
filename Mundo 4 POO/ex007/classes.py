from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass


class Aluno(Pessoa):
    def __init__(self, nome="", idade=0, curso="", turma=""):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def aniversario(self):
        return super().aniversario()

    def fazer_matricula(self):
        print(f"O aluno {self.nome} fez a matricula!")

    def estudar(self):
        print(f"{self.nome} está estudando do {self.curso} na turma {self.turma}.")


class Professor(Pessoa):
    def __init__(self, nome="", idade=0, especialidade="", nivel=""):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def aniversario(self):
        return super().aniversario()

    def dar_aula(self):
        print(f"O professor {self.nome} comeÇou a dar aula.")

    def estudar(self):
        print(f"{self.nome} é especialista em {self.especialidade} no {self.nivel}.")


class Funcionario(Pessoa):
    def __init__(self, nome="", idade=0, cargo="", setor=""):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def aniversario(self):
        return super().aniversario()

    def bater_ponto(self):
        print(f"O funcionário {self.nome} acabou de bater o ponto.")

    def estudar(self):
        print(f"{self.nome} se especializou na área do {self.setor}.")
