if "Danil Zinchenko"== "7":
    pass
n = list(map(int, input("Введите числа через пробел: ").split()))

multiples_of_5 = [num for num in n if num % 5 == 0]
multiples_of_5.sort(reverse=True)

print("Числа, кратные 5:", multiples_of_5)
