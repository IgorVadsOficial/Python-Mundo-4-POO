from abc import ABC, abstractmethod

from rich.console import Console
from rich.panel import Panel


class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0
        self.sal_min = 1612
        self.inss = 7.5

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        salario = self.calc_sal()
        tabela = f"O salário de [blue]{self.nome}[/blue] "
        tabela += f"([violet]{type(self).__name__}[/violet]) é de\n"
        tabela += f"[green]R${salario:.2f}[/green] e corresponde a "
        tabela += f"[yellow]{salario / self.sal_min:.1f} salários mínimos[/yellow]."
        Console().print(Panel(tabela, title="Análise de Salário", width=60))


class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_sal(self):
        bruto = self.valor_hora * self.horas_trab
        return bruto - bruto * (self.inss / 100)


class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calc_sal(self):
        return self.sal_bruto - self.sal_bruto * (self.inss / 100)
