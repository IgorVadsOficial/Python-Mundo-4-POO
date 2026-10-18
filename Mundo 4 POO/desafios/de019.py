class Livro:
    def __init__(self, nome, paginas):
        self.nome = nome
        self.paginas = paginas
        self.pagina_atual = 0

    def avancar_paginas(self, avancar):
        self.pagina_atual += avancar

        if self.pagina_atual >= self.paginas:
            self.pagina_atual = self.paginas
            return f"Você chegou ao final do livro '{self.nome}'."
        return f"Você avançou {avancar} páginas e está na página {self.pagina_atual}."


li = Livro("Dez coisas que eu aprendi", 20)
print(li.avancar_paginas(5))
print(li.avancar_paginas(10))
print(li.avancar_paginas(6))
