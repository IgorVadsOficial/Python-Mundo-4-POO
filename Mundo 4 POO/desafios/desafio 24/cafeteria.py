from abc import ABC, abstractmethod


class BebidaQuente(ABC):

    def ferver_agua(self):
        print(f"1. Fervendo água a 100 graus Celsius.")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

    def preparar(self):
        print("--- Iniciando o Preparo ---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("--- Bebida Pronta ---")


class Cafe(BebidaQuente):

    def ferver_agua(self):
        return super().ferver_agua()

    def misturar(self):
        print(f"2. Passando água pressurizada pelo pó de café moido.")

    def servir(self):
        print(f"3. Servindo em xicara pequena.")

    def preparar(self):
        return super().preparar()


class Cha(BebidaQuente):

    def ferver_agua(self):
        return super().ferver_agua()

    def misturar(self):
        print("2. Mergulhando o sachê de ervas na água.")

    def servir(self):
        print("3. Servindo na caneca de porcelana com limão.")

    def preparar(self):
        return super().preparar()


class Leite(BebidaQuente):

    def ferver_agua(self):
        return super().ferver_agua()

    def misturar(self):
        print("2. Passando vapor pressurizado pelo bico do leite.")

    def servir(self):
        print("3. Servindo na caneca grande, já com café.")

    def preparar(self):
        return super().preparar()
