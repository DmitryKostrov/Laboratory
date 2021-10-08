
def first():
    print('Введите число камней')
    stones = int(input())
    while stones > 0:
        take = int(input())
        stones -= take
        print('Осталось', stones)


def second():
    print('Введите число камней')
    stones = int(input())
    while stones > 0:
        take = int(input())
        if take <= stones and take <= 3:
            stones = stones - take
            print('Осталось', stones)
        else:
            print('Осталось', stones)


def third():
    print('Введите число')
    num = int(input())
    (x, y) = (0, 1)
    while x <= num:
        print(x)
        (x, y) = (y, x+y)


def fourth():
    print('Введите день')
    d = int(input())
    print('Введите месяц')
    m = int(input()) - 2
    print('Введите год')
    e = int(input())

    c = int(e / 100)
    y = ((e-c) % 100)

    r = d + ((13*m - 1) // 5) + y + (y // 4 + c // 4 - 2*c + 777)
    r %= 7
    print(r)


def fifth():
    print('Введите число')
    num = int(input())
    count = 0

    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num - 1
        count += 1
    print(count)


def sixth():
    print('Введите кол-во камней')
    one = int(input(' - 1-ой кучи: '))
    two = int(input(' - 2-ой кучи: '))

    bunch = 0
    taken = 0

    while True:
        bunch = int(input('Введите номер кучи - из которой беруться камни: '))
        taken = int(input('Введите количество забираемых камней: '))

        if bunch == 1:
            if one - taken >= 0:
                one -= taken
        else:
            if two - taken >= 0:
                two -= taken
        print(one, two)
        if one == 0 or two == 0:
            break


# first()
# second()
# third()
# fourth()
# fifth()
sixth()
