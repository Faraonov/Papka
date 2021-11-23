def f(a):
    if a < 2:
        return 1
    else:
        return a * f(a - 1)


n = int(input("Введите n"))
print("n! =", f(n))


assert f(0) and f(1) == 1
assert f(5) == 120