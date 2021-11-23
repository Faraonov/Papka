def z(n):
    if (n < 3) or (n == 12):
        return("зима")
    elif (n > 2) and (n < 6):
        return("весна")
    elif (n > 5) and (n < 9):
        return("лето")
    else:
        return("осень")


print(z(int(input("Введите число от 1 до 12"))))
