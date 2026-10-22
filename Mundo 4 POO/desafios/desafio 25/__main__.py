from Transporte import *

dist = 8

entrega = Drone(dist)
print(f"Frete de {type(entrega).__name__} em {dist}Km = {entrega.calcular_frete()}")
