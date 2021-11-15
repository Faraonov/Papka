def z(x):
    x = input("Ввод")
    a = list(x)
    while x != "":
        a.append(x)
        x = input()
    return a


print(z(" "))
