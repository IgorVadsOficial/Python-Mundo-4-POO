from termostato import Termostato
from rich import inspect


def main():
    t = Termostato()
    print(t.temperatura)
    t.temperatura = 25.8
    print(t.ftemperatura)
    
    inspect(t, private=True, methods=True)

if __name__ == "__main__":
    main()