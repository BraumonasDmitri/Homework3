def my_func():
    res = 0
    numbers = int(input('Введите числа через пробел или R для выхода: ')).split()
    while True:
        for i in numbers:
            try:
                if i == 'R':
                    print(f'Сумма равна {res}.')
                    return
                else:
                    res += int(i)
            except ValueError:
                print('Введите числа через пробел или R для выхода: ')
        print(f'Сумма равна {res}.')