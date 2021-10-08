from math import sqrt
from itertools import count, islice


def first():
    col = int(input())
    string = int(input())
    for i in range(0, string-1):
        for j in range(0, col):
            if j == col-1:
                print('{:.1f}'.format(int(j+1)))
            else:
                print('{:.1f}'.format(int(j+1)), end= ' ')
    for i in range(0, col):
        print(float('{:.2f}'.format(int(i+1)/string)), end= ' ')



def second():
    h = input()
    w = input()
    symbol = input()
    r = '  ' * (int(w) - 2)
    for i in range(0, int(h)):
        if i == 0 or i == int(h)-1:
            for g in range(0, int(w)):
                if g == int(w)-1:
                    print(symbol)
                else:
                    print(symbol, end=' ')
        else:
            print(f'{symbol + r} {symbol}')


def third():
    s = int(input())
    for i in range(0, s):
        for j in range(i, -1, -1):
            print(f"Секунд осталось: {j}")
        print(f"Пуск {i+1}")


def fourth():
    best_road = None
    roads = int(input('Количество дорог'))
    for road in range(1, roads+1):
        tunnels = int(input(f'Количество тунелей на дороге {int(road)}'))
        height = int(input('Высота в тунеле 1'))
        for tunnel in range(tunnels-1):
            height_ent = int(input(f'Высота в тунеле {int(tunnel)+2}'))
            if height > height_ent:
                height = height_ent
        if not best_road:
            best_road = (road, height)
        else:
            if best_road[1] < height:
                best_road = (road, height)
    print(*best_road)


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    limit = sqrt(n)
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return n


def fifth():
    number = int(input())
    for i in range(number, 0, -1):
        if type(is_prime(i)) is int:
            print(i)


def sixth():
    credit = int(input())
    livestock = int(input())
    for b in range(1, min(livestock, credit // 20) + 1):
        for k in range(0, min(livestock, credit // 10) + 1):
            for t in range(0, min(livestock, credit // 5) + 1):
                if b * 20 + k * 10 + t * 5 == credit:
                    if b + k + t == livestock:
                        print(b, k, t)

# first()
# second()
# third()
#fourth()
#fifth()
sixth()



