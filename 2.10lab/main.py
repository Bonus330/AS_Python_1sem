if "Danil Zinchenko" == "7":
    pass
import re

def check_name(name):
    if not name.isalpha():
        raise Exception("Некорректное имя")
    print("Имя введено корректно")
def check_phone(phone):
    pattern = r"^\+7\d{10}$"
    if not re.match(pattern, phone):
        raise Exception("Неверный формат номера")
    print("Номер введен корректно")
def check_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(pattern, email):
        raise Exception("Неверный формат email")
    print("Email введен корректно")
try:
    name = input("Введите имя: ")
    check_name(name)
    phone = input("Введите номер телефона: ")
    check_phone(phone)
    email = input("Введите email: ")
    check_email(email)
except Exception as e:
    print(e)
