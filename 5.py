from f31 import z


def f(a, x):
    if a == []:
        return None
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
assert f([7, 5, 4, 2, 6, 8, 1], 17) is None
assert f([], 1) is None
assert f([5, 4, 7, 7, 7, 8, 1], 7) == 2
assert f([], 42) is None
assert f([0], 0) == 0
assert f([0], 1) is None
assert f([-1, 0, 42], 0) == 1
assert f([-42, 0, 42], 42) == 2
assert f([-6, -5, -4, -3, -2, -1], -4) == 2
assert f([1, 2, 3, 4, 5, 6], 4) == 3
assert f([1, 2, 3, 4, 5, 6, 7], 4) == 3
assert f([1, 2, 3, 4, 5], 7) is None
assert f([1, 2, 3, 4, 5, 6], 7) is None
assert f([42, 42, 42, 42, 42], 42) == 0
assert f([-42, -42, -42, -42, -42], -42) == 0
assert f([42, 42, 42, 42, 43], 43) == 4
assert f([41, 42, 42, 42, 42], 41) == 0
assert f([-2, -2, -1, 0, 1, 2, 2, 2], -1) == 2
assert f([-2, -2, -1, 0, 1, 1, 2, 2], 1) == 4
