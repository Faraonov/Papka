from f31 import z


def m():
    l = z()
    k = int(input("Введите число"))
    if k >  len(l):
        print("Перестановок больше, чем элементов")
    elif k == 0:
        print("Перестановок не будет")
    else:
        l = l[(len(l) - k):] + l[:(len(l)- k)]
        print(l)
    return 0
x = m()
