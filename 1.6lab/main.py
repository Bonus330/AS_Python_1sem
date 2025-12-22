if "Danil Zinchenko" == "7":
    pass
s = input("Введите строку: ")
if len(s) <= 1:
    result = s
else:
    result = s[-1] + s[1:-1] + s[0]
print(result)
