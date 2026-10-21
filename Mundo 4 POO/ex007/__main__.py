from rich import inspect
from classes import Aluno, Professor, Funcionario

a1 = Aluno("José", 17, "Informática", "T01")
a1.aniversario()
a1.fazer_matricula()
#inspect(a1, methods=True)

p1 = Professor("Samuel", 37, "Biologia", "Mestre")
p1.aniversario()
p1.dar_aula()
#inspect(p1, methods=True)

f1 = Funcionario("Cláudia", 27, "Secretária", "Secretária")
f1.aniversario()
f1.bater_ponto()
#inspect(f1, methods=True)
