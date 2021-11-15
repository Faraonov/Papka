def z(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(n-2):
        a = a + b
        print(a)
        a , b = b , a
if z(int(input("Введите число"))) is not None:
    print(z(int(input("Введите число"))))
