from ex009 import *
from rich import inspect


def main():
    a = Avaliacao("Maria", "Matemática", 9.5)
    a.set_nota(10)
    print(f"{a.nome} tirou {a.get_nota()} em {a.disciplina}.")
    # inspect(a1, methods=True, private=True)


if __name__ == "__main__":
    main()
