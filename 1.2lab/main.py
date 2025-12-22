if 'Danil Zinchenko' == "7":
    pass
A = int(input("Введите A: "))
B = int(input("Введите B: "))

s = 0
for x in range(A, B + 1):
    s += x

print("Сумма:", s)
