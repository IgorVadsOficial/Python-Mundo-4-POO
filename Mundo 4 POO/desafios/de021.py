from rich import print


class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.destampada = False

    def destampar(self):
        self.destampada = True

    def quebrar_linha(self, vezes):
        for i in range(1, vezes, 1):
            print("\n")

    def escrever(self, mensagem):
        cor = self.cor.lower()
        if self.destampada == True:

            if cor == "azul":
                print(f"[bold blue]{mensagem}[/bold blue]")
            elif cor == "verde":
                print(f"[bold green]{mensagem}[/bold green]")
            elif cor == "vermelha":
                print(f"[bold red]{mensagem}[/bold red]")
        else:
            if cor == "azul":
                print(f"A [bold blue]caneta[/bold blue] está tampada")
            elif cor == "verde":
                print(f"A [bold green]caneta[/bold green] está tampada")
            elif cor == "vermelha":
                print(f"A [bold red]caneta[/bold red] está tampada")


c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem? ")
c1.quebrar_linha(2)
c2.escrever("Olá, Gafanhoto! ")
c3.escrever("Vamos exercitar!")
