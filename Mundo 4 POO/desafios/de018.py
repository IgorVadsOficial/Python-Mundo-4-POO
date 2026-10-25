from rich import print
from rich.panel import Panel


class Churrasco:
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant

    def analisar(self):
        tabela = f"Analisando [bold green]{self.titulo}[/bold green] com [bold blue]{self.quant} convidados[/bold blue].\n"
        tabela += f"Cada participante comerá 0.4KG e cada KG custa R$82.40.\n"
        quant_carne = self.quant * 0.4
        tabela += (
            f"Recomendo [bold blue]comprar {quant_carne}KG[/bold blue] de carne.\n"
        )
        preco_carne = quant_carne * 82.40
        tabela += (
            f"O custo total será de [bold green]R${preco_carne:.2f}[/bold green].\n"
        )
        tabela += f"Cada pessoa pagará [bold yellow]R${preco_carne / self.quant}[/bold yellow] para participar."
        analisador = Panel(tabela, title=self.titulo, width=60)
        return analisador


c1 = Churrasco("Churras dos Amigos", 15)

print(c1.analisar())
