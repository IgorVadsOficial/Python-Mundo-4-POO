from salarios import Horista, Mensalista

f1 = Horista("Paulo", 12, 200)
print(f1.calc_sal())
f1.analisar_sal()

f2 = Mensalista("Amanda", 9500)
print(f2.calc_sal())
f2.analisar_sal()
