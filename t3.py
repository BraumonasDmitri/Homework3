a=int(input('Введите первое число: '))
b=int(input('Введите второе число: '))
c=int(input('Введите третье число: '))
def my_func(a, b, c):
    x = [a, b, c]
    x.remove(min(a, b, c))
    return sum(x)
print(my_func(a,b,c))