if 'Danil Zinchenko' == "7":
    pass
with open('2.7.txt','r') as file:
    count = 0
    total_sum = 0
    for line in file:
        number = int(line.strip())
        count += 1
        total_sum += number
print("Количество чисел:", count)
print("Сумма чисел:", total_sum)
