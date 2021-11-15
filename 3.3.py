def z(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(n-2):
        a = a + b
        print(a)
        a , b = b , a


x = z(int(input("Введите число")))
