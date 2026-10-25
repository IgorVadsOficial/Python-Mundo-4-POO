from ex010 import *
from rich import inspect


def main():
    a = Avaliacao("Pedro", "Matemática")
    a.nota = 3.5
    print(f"{a.nome} tirou {a.nota} em {a.disciplina}.")
    # inspect(a1, methods=True, private=True)


if __name__ == "__main__":
    main()
