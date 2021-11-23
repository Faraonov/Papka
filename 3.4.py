from f31 import z


l = z()
print("Элемент | Частота")
for i in set(l):
    y = l.count(i)
    print(i, "|", y)
