from rich import print
from rich.panel import Panel


class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos = []

    def add_favoritos(self, jogo):
        self.jogos.append(jogo)

    def ficha(self):
        tabela = f"Nome real: {self.nome}\n"
        tabela += f"Jogos favoritos: "
        for game in self.jogos:
            tabela += f"\n[bold blue]🎮 {game}[/bold blue]"
        print(Panel(tabela, title=f"Jogador {self.nick}", width=40))


j1 = Gamer("Fabricio da Silva", "detonator2025")
j1.add_favoritos("Mario Bros.")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
j1.ficha()

print("\n")
j2 = Gamer("Olivia de Souza", "peach_raivosa")
j2.add_favoritos("Call of Duty")
j2.add_favoritos("Marios Bros.")
j2.ficha()
print("\n")
