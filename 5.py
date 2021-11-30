from f31 import z


def f(a, x):
    if a == []:
        return 'Пустой список'
    else:
        t = len(a) // 2
        j = len(a) - 1
        l = 0
        while int(a[t]) != x and l <= j:
            if x > int(a[t]):
                l = t + 1
            else:
                j = t - 1
            t = (l + j) // 2
        if l > j:
            return None
        else:
            for i in range(t+1):
                if a[i] == a[t] and i < t:
                    t = i
            return t


b = z()
b.sort(key=int)
print(b)
m = int(input("Введите искомый элемент"))
print(f(b, m))
assert f([5, 6, 7], 5) == 0
assert f([1, 2, 4, 5, 6, 7, 8], 17) == None
assert f([], 1) == "Пустой список"
assert f([1, 4, 5, 7, 7, 7, 8], 7) == 3
