class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos = []

    def add_favoritos(self, jogo):
        self.jogos.append(jogo)

    def ficha(self):
        print(f"Nome real: {self.nome}\nNick: {self.nick}\n")
        print(f"Jogos favoritos: {sorted(self.jogos)}")


j1 = Gamer("Fabricio da Silva", "detonator2025")
j1.add_favoritos("Mario Bros.")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
j1.ficha()

print("\n")
j2 = Gamer("Olivia de Souza","")
j2.add_favoritos("Call of Duty")
j2.add_favoritos("Marios Bros")
j2.ficha()
print("\n")