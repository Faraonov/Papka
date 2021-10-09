x = input()
i = 0
x1 = 0
x2 = 0
while i != len(x):
    if x[i] == "(":
        x1 = x1 + 1
    elif x[i] == ")":
        x2 = x2 + 1
    i += 1
if x1 > x2:
    print("Не хватает", x1 - x2, "закр. ск.")
elif x1 < x2:
    print("Не хватает", x2 - x1, "откр. ск.")
else:
    print("Скобок чётное число")
