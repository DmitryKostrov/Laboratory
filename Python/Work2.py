#Первая задача
variable = input("Введите значение Да или Нет: ")   #Ввод данных
if variable == "Да" or variable == "Нет": #Проверка данных
    print("ВЕРНО")
else: 
    print("НЕВЕРНО")

#Вторая задача
furTree_1 = input()  #Ввод данных
furTree_2 = input()  #Ввод данных
furTree_3 = input()  #Ввод данных
if furTree_1 == "Раз" and furTree_2 == "Два" and furTree_3 == "Три": #Проверка данных
    print("ГОРИ")
else:
    print("НЕ ГОРИ")

#Третья задача
furTree_4 = input()  #Ввод данных
furTree_5 = input()  #Ввод данных
furTree_6 = input()  #Ввод данных
if furTree_4 == "Раз" and furTree_5 == "Два" and furTree_6 == "Три":   #Проверка данных
    print("ГОРИ")
elif furTree_4 == "1" and furTree_5 == "2" and furTree_6 == "3":   #Доп. проверка данных
    print("ГОРИ")
else:
    print("НЕ ГОРИ")

#Четвертая задача
furTree_7 = input()  #Ввод данных
furTree_8 = input()  #Ввод данных
furTree_9 = input()  #Ввод данных
if furTree_7 == "Один" and furTree_8 == "Два" and furTree_9 == "Три":    #Проверка данных
    print("ГОРИ")
else:
    print("НЕ ГОРИ")

#Пятая задача
mail = input("Введите почту: ") #Ввод данных
if "@" in mail:   #Проверка данных
    print("ОК")
else:
    print("Некорректный логин")
