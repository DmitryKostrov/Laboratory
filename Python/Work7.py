def first():
    war = "Евразия"
    peace = "Остазия"
    com = int(input("Количество команд "))
    for i in range(1, com + 1):
        comand = str(input("Команда"))
        if comand == "С кем война?":
            print(war)
        if comand == "С кем мир?":
            print(peace)
        if comand == "Меняем":
            a = war
            war = peace
            peace = a


def second():
    num = int(input())
    flag = False
    for i in range(0, num):
        word=str(input())
        if 'Кот' in word or 'кот' in word:
            print("МЯУ")
            flag = True
            break
    if flag == False:
        print("НЕТ")


def third():
    num = []
    count = 0
    while True:
        string = input()
        count += 1
        if 'Кот' in string or 'кот' in string:
            num.append(count)
        if 'СТОП' in string:
            break
    if not num:
        print(-1)
    else:
        print(*num)


def fourth():
    num = []
    count = 0
    while True:
        string = input()
        count += 1
        if 'Кот' in string or 'кот' in string:
            num.append(count)
        if 'СТОП' in string:
            break
    if not num:
        print(-1)
    else:
        print(f"Количество строк {len(num)}"
              f"\nВпервые {num[0]}")

def fifth():
    list = []
    pay = 0
    sale = 0

    while True:
       list.append(int(input()))
       if len(list) > 1:
           if list[-2] < list[-1] and pay == 0:
               pay = list[-1]
           if list[-2] > list[-1] and sale == 0 and pay != 0:
               sale = list[-1]
       if list[-1] == 0:
           break
    print(pay, sale, sale-pay)

def sixth():
    num = int(input())
    onetwo = ['раз', 'два', 'три', 'четыре']
    jum = 0
    while num > 0:
        for i in range(4):
            word = input()
            if word != onetwo[i]:
                print('Правильных отсчётов было', jum, ', но теперь вы ошиблись.')
                jum = 0
                num -= 1
                break
            jum += 1
    print('На сегодня хватит.')

def seventh():
    n = int(input())
    p = 0
    bad = - 1
    for i in range(n):
        b = int(input())
        h, r, m = b % 256, (b // 256) % 256, b // 256 ** 2
        t = ((m + r + p) * 37) % 256
        if t != h or h >= 100:
            bad = i
            break
        p = h
    print(bad)

# inputt = [32,
#           30,
#           31,
#           34,
#           38,
#           37,
#           39,
#           0,
# ][::-1]

# inputt = [
#     5,
# 6122802,
# 14406496,
# 15230209,
# 2541121,
# 1758741,
#
# ][::-1]

inputt = [
5,
1865535,
13479687,
16689153,
1839958,
5214020,


][::-1]
def input(*args):
    return inputt.pop()

#first()
#second()
#third()
#fourth()
#fifth()
#sixth()
seventh()
