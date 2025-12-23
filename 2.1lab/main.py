if __name__ == "__main__":
    pass
def create_squares_dict():
    squares_dict = {num: num**2 for num in range(1, 16)}
    return squares_dict
def create_frequency_dict(input_string):
    frequency_dict = {}
    for char in input_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return frequency_dict
def filter_dict(input_dict, min_value):
    filtered_dict = {key: value for key, value in input_dict.items() if value >= min_value}
    return filtered_dic
def main():
    print("Задание а: Словарь квадратов чисел")
    squares = create_squares_dict()
    print(squares)
    print()
    print("Задание б: Словарь частот символов")
    test_string = "hello world"
    frequency = create_frequency_dict(test_string)
    print(f"Строка: '{test_string}'")
    print(frequency)
    print()
    print("Задание в: Фильтрация словаря")
    test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    print(f"Исходный словарь: {test_dict}")
    filtered = filter_dict(test_dict, 3)  # Оставляем значения >= 3
    print(f"Отфильтрованный словарь: {filtered}")
if __name__ == "__main__":
    main()
