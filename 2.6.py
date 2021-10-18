x = list(input("Введите строку"))
k = int(input())
j = 0
for i in x:
      if i.isdigit():
        j += 1
      if j == k:
        print(i)
        break
