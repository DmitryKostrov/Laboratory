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
print(figure_1 + figure_2)

#
ch = input()
ussr = (len(ch) * 40)
u_1 = ussr % 100
ussr = ussr // 100
u_2 = ussr
print(u2, 'р.', u1, 'коп.')
#40 копеек
#
#
#
