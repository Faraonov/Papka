from f31 import z


def p(x):
    if len(set(x)) == len(x):
        return True
    else:
        return False


b = z()
a = p(b)
print(a)


assert p([0, 1]) == True
assert p([1, 1]) == False