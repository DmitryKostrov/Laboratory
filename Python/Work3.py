#Первая задача
word = input()
length = len(word)
print("Слово ",word," имеет длину ", length, "букв.")

#Вторая задача
town1 = input()
town2 = input()
tula = 'Тула'
penz = 'Пенза'
if town1 != town2 and (town1 == tula and town2 != penz or town2 == penz and town1 != tula):
    print('ДА')
else:
    print('НЕТ')

#Третья задача
figure_1 = int(input());
figure_2 = int(input());
print(figure_1 + figure_2)

#Четвертая задача
figure_3 = float(input());
figure_4 = float(input());
print(figure_3 + figure_4)

#Пятая задача
ch = input()
ussr = (len(ch) * 40)
u_1 = ussr % 100
ussr = ussr // 100
u_2 = ussr
print(u_2, 'р.', u_1, 'коп.')

#Шестая задача
x = float(input('Ввести число:'))
if x < 0:
    print('-')
elif x == 0:
    print('0')
else:
    print('+')
#Седьмая задача
number = int(input())
number_1 = ((number // 100) + (number // 10) % 10)
number_2 = (((number // 10) % 10) + (number % 100) % 10)
if number_1 > number_2:
    print(str(number_1) + str(number_2))
else:
    print(str(number_2) + str(number_1))
#Восьмая задача
a = int(input())
b = int(input())
c = int(input())
if a > b > c:
    print(a)
    print(b)
    print(c)
elif a > c > b:
    print(a)
    print(c)
    print(b)
elif b > a > c:
    print(b)
    print(a)
    print(c)
elif b > c > a:
    print(b)
    print(c)
    print(a)
elif c > a > b:
    print(c)
    print(a)
    print(b)
elif c > b > a:
    print(c)
    print(b)
    print(a)
elif a == b == c:
    print(b)
    print(c)
    print(a)

