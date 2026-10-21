from classes import Aluno, Professor, Funcionario

a1 = Aluno("José", 17, "Informática", "T01")
a1.aniversario()
a1.fazer_matricula()
a1.estudar()
print("\n")

p1 = Professor("Samuel", 37, "Biologia", "Mestre")
p1.aniversario()
p1.dar_aula()
p1.estudar()
print("\n")

f1 = Funcionario("Cláudia", 27, "Secretária", "Secretária")
f1.aniversario()
f1.bater_ponto()
f1.estudar()
print("\n")