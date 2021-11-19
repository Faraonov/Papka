def z ():
    a = list()
    x = input("Ввод")
    while x != "":
        a.append(x)
        x = input()
    return a 


l = z ()
print("Элемент | Частота")
for i in set(l):
    y = l.count(i)
    print(i, "|", y)