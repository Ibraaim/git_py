import random

def get_info():
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    
    password = generate_password(first_name, last_name)
    
    return f"Сгенерированный пароль: {password}"

def generate_password(first_name, last_name):
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(7))
    password = first_name + last_name + random_numbers
    
    return password



print(get_info())
