from abc import ABC, abstractmethod


class Poligono(ABC):
    def __init__(self):
        self.qtd_lados = 0

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado):
        self.qtd_lados = 4
        self.lado = lado

    def perimetro(self):
        return self.lado * self.qtd_lados

    def area(self):
        return self.lado * self.lado


class Circulo(Poligono):
    def __init__(self, raio):
        self.qtd_lados = 0
        self.raio = raio

    def perimetro(self):
        return 2 * 3.14 * self.raio

    def area(self):
        return 3.14 * pow(self.raio, 2)
