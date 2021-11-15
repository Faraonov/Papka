def z(n):
    if (n < 3) or (n == 12):
        print("зима")
    elif (n > 2) and (n < 6):
        print("весна")
    elif (n > 5) and (n < 9):
        print("лето")
    else:
        print("осень")
if z(int(input("Введите число от 1 до 12"))) is not None:
   print(z(int(input("Введите число от 1 до 12"))))
