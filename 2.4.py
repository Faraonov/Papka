x = input()
x1 = 0
x2 = 0
for i in x:
    if x[i] == "(":
        x1 +=1
    elif x[i] == ")":
        x2 +=1
if x1 > x2:
    print("Не хватает", x1 - x2, "закр. ск.")
elif x1 < x2:
    print("Не хватает", x2 - x1, "откр. ск.")
else:
    print("Скобок чётное число")
