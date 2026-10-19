from rich import print
from rich.panel import Panel


class ControleRemoto:
    canal_min: int = 1
    canal_max: int = 6
    volume_min: int = 1
    volume_max: int = 5

    def __init__(self, canal=1, volume=2):
        self.canal_atual: int = (
            canal if self.canal_min <= canal <= self.canal_max else self.canal_min
        )
        self.volume_atual: int = volume
        self.ligado: bool = False

    def ligar_tv(self, ligar):
        if ligar == "@" and self.ligado == False:
            self.ligado = True
        elif ligar == "@" and self.ligado == True:
            self.ligado = False

    def mostrar_tv(self):
        if self.ligado == False:
            tv = f"[bold red]🚫 A TV está desligada![/bold red]"
            print(Panel(tv, title="[ TV ]", width=30))
        else:
            tv = f"[bold yellow]CANAL = {self.canal_atual}[/bold yellow]\n"
            tv += f"[bold blue]VOLUME = {self.volume_atual}[/bold blue]"
            print(Panel(tv, title="[ TV ]", width=30))

    def comandos(self):
        while True:
            acao = input(f"< CH{self.canal_atual} > - VOL{self.volume_atual} + ")

            if acao == "0":
                break
            elif acao == "@":
                self.ligar_tv("@")
            elif acao == "<":
                self.canal_atual = (
                    self.canal_max
                    if self.canal_atual <= self.canal_min
                    else self.canal_atual - 1
                )
            elif acao == ">":
                self.canal_atual = (
                    self.canal_min
                    if self.canal_atual >= self.canal_max
                    else self.canal_atual + 1
                )
            elif acao == "-":
                self.volume_atual = max(self.volume_min, self.volume_atual - 1)
            elif acao == "+":
                self.volume_atual = min(self.volume_max, self.volume_atual + 1)

            self.mostrar_tv()


c1 = ControleRemoto(1, 1)

c1.mostrar_tv()
c1.comandos()
