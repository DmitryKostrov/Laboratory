from fractions import Fraction


def first():
    print('Введите число для возведения в факториал')
    n = int(input())
    n1 = 1
    for i in range(2, n+1):
        n1 *= i
    print(n1)


def second():
    print('Введите t')
    temp = float(input())
    days = 0
    for i in range(temp):
        if temp < 22.0:
           days += 1
    temp = float(input())

    print(days // 7)


def third():
    print('Введите число')
    num = int(input())
    otvet = 0
    cout = num
    while otvet != num:
        if num // cout == num / cout:
            if num // cout != 0:
                otvet = num // cout
                print(otvet, end=' ')
        cout = cout - 1
    if num == 1:
        print()
        print('НЕТ')
    elif num == 2:
        print()
        print('ПРОСТОЕ')
    elif num % 2 == 0:
        print()
        print('НЕТ')
    else:
        print()
        print('ПРОСТОЕ')


def fourth():
    print('Введите число')
    n = int(input())
    if n >= 0:
       for i in range(n):
           n -=1
           print('Осталось секунд:', n)
    print('Пуск')


def fifth():
    print('Введите число')
    n = int(input())
    a = 0
    p = 3.141592653589793
    for i in range(1, n + 1):
        a += 1 / (i ** 2)
    print((p ** 2) / a)


def sixth():
    n = int(input())
    count = Fraction(0, 1)
    for i in range(n):
         a = Fraction(int(input()), int(input()))
         count = count + a
    print(count)


# first()
# second()
# third()
# fourth()
# fifth()
# sixth()
