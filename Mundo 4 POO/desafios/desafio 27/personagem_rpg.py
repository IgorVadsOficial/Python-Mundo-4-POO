from abc import ABC, abstractmethod
from random import randint
from rich import print


class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = ""

    def atacar(self, alvo, forca=100):
        valor = randint(1, forca)
        print(
            f"[green]{self.nome}[/green]([bold violet]{self.vida}[/bold violet]) atacou [red]{alvo.nome}[/red]([violet]{alvo.vida}[/violet]) com [blue]{self.golpes}[/blue] de força [bold violet]{forca}[/bold violet]."
        )
        alvo.vida -= valor
        print(
            f"[blue]{alvo.nome}[/blue] recebeu [red]dano de[/red] [bold red]{valor}[/bold red]."
        )

    def receber_dano(self, dano):
        self.vida -= dano

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        golpe = randint(1, 3)
        if golpe == 1:
            self.golpes = "Soco"
        elif golpe == 2:
            self.golpes = "Golpe com Machado"
        elif golpe == 3:
            self.golpes = "Pulo Giratório"

    def atacar(self, alvo, forca=100):
        return super().atacar(alvo, forca)

    def receber_dano(self, dano):
        return super().receber_dano(dano)

    def curar(self):
        cura = randint(1, 100)
        self.vida += self.vida
        print(
            f"[bold blue]{self.nome}[/bold blue] enrolou uma atadura nos ferimentos e [green]recuperou [bold green]{cura}[/bold green] pontos[/green] de vida."
        )


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        golpe = randint(1, 3)

        if golpe == 1:
            self.golpes = "Bola de fogo"
        elif golpe == 2:
            self.golpes = "Magia Estática"
        elif golpe == 3:
            self.golpes = "Raio Congelante"

    def atacar(self, alvo, forca=100):
        return super().atacar(alvo, forca)

    def receber_dano(self, dano):
        return super().receber_dano(dano)

    def curar(self):
        cura = randint(1, 100)
        self.vida += self.vida
        print(
            f"[bold blue]{self.nome}[/bold blue] fez uma magia de cura e [green]recuperou [bold green]{cura}[/bold green] pontos[/green] de vida."
        )
