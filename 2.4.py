x = input()
x1 = 0
x2 = 0
for i in x:
    if i == "(":
        x1 += 1
    elif i == ")":
        x2 += 1
if x1 > x2:
    print("Не хватает", x1 - x2, "закр. ск.")
elif x1 < x2:
    print("Не хватает", x2 - x1, "откр. ск.")
else:
    print("Откр. и закр. ск. поровну")
