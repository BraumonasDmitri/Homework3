def user(**abcdef):
    return list(abcdef.values())
print(user(name=input('Введите имя: '),
    surname=input('Введите фамилию: '),
    birthdate=input('Год рождения: '),
    city=input('Город проживания: '),
    email=input('Электронная почта: '),
    tel=input('Телефонный номер: ')))
