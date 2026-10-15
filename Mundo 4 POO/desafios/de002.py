class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        return f"\n|---------------------|\n|-------Produto-------|\n|  {self.nome}  | \n|{"-"*21}|\n|-----R${self.preco:,.2f}-----|\n|---------------------|"


p1 = Produto("iPhone 17 Pro Max", 25000.85)
p2 = Produto("Notebook Gamer", 8000.00)

print(p1.etiqueta())
print(p2.etiqueta())