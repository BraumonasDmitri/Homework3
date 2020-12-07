

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 'Знаменатель не может быть меньше 0'
print(divide((int(input('Введите числитель: '))), (int(input('Введите знаменатель: ')))))







