def crarifm(a):
    return sum(a) / len(a)


b = list()
x = input("Введите числа")
while x != "":
    b.append(float(x))
    x = input("")
print(crarifm(b))