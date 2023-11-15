def calculator():
    while True:
        num1 = float(input("Введите первое число: "))
        operator = input("Введите оператор (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            print("Некорректный оператор!")
            continue
        
        print("Результат:", result)
        
        choice = input("Хотите продолжить? (да/нет): ")
        if choice.lower() != 'да':
            break

calculator()
