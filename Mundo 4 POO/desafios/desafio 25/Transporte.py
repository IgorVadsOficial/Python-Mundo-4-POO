from abc import ABC, abstractmethod
from rich import print


class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = self.calcular_frete()

    @abstractmethod
    def calcular_frete(self):
        pass


class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        return f"R$[bold blue]{self.distancia * 0.50:.2f}[/bold blue]"


class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia < 50:
            return f"Raio minimo de 50Km"
        else:
            return f"R$[bold blue]{self.distancia * 1.20:.2f}[/bold blue]"


class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia > 10:
            return f"Raio maximo de 10Km"
        else:
            return f"R$[bold blue]{self.distancia * 9.50:.2f}[/bold blue]"
