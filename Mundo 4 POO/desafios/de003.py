class Churrasco:
    def __init__(self, pessoas):
        self.pessoas = pessoas

    def analisar(self):
        return f"\nAnalisando Churras dos Amigos com {self.pessoas} convidado(s).\nCada participante comerá 0.4kg e cada Kg custa R$82.40.\nRecomendo comprar {self.pessoas * 0.4}kg de carne.\nO custo total será de R${(self.pessoas * 0.4) * 82.40:,.2f}.\nCada pessoa pagará R${((self.pessoas * 0.4) * 82.40) / self.pessoas}.\n"


c1 = Churrasco(15)

print(c1.analisar())
