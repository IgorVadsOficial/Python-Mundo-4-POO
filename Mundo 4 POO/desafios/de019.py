from rich import print
from time import sleep


class Livro:
    def __init__(self, nome, paginas):
        self.nome = nome
        self.paginas = paginas
        self.pagina_atual = 1

    def avancar_paginas(self, avancar):
        print(f"Pág{self.pagina_atual}", end=" > ")
        cont = 0
        for _ in range(avancar):
            if self.pagina_atual >= self.paginas:
                break
            self.pagina_atual += 1
            print(f"Pág{self.pagina_atual}", end=" > ")
            sleep(0.5)
            cont += 1

        if self.pagina_atual == self.paginas:
            print(f"[bold blue]Você avançou {cont} páginas e agora está na [bold yellow]página {self.pagina_atual}[/bold yellow]")
            print(f"[bold red]🚨 Você chegou ao final do livro '{self.nome}'[/bold red]")
        else:
            print(f"[bold blue]Você avançou {avancar} páginas e agora está na [bold yellow]página {self.pagina_atual}[/bold yellow]")


li = Livro("Dez coisas que eu aprendi", 20)
li.avancar_paginas(5)
li.avancar_paginas(10)
li.avancar_paginas(50)
