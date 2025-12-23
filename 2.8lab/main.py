if 'Danil Zinchenko' == "7":
    pass
  with open('f.txt', 'r') as file:
    first_two_chars = file.read(2)
    if first_two_chars[0].isdigit() and first_two_chars[1].isdigit():
        s = int(first_two_chars)
        if s % 2 == 0:
            print(f"Первые два символа '{first_two_chars}' образуют четное число")
        else:
            print(f"Первые два символа '{first_two_chars}' образуют нечетное число")
    else:
        print("Первые два символа не являются цифрами")  
