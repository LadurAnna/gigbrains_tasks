"""Задача 38: Дополнить телефонный справочник возможностью
изменения и удаления данных. Пользователь также может
ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных и поиска по фамилии."""

FILE_NAME = "file.txt"


def AddInTB(number, name, sname):
    f = open(FILE_NAME, "a", encoding="utf8")
    data = number + " " + name + " " +  sname + "\n"
    f.write(data)
    f.close()


def DelTB(number):
    f = open(FILE_NAME, "r", encoding="utf8")
    data = f.read()
    f.close()
    print(data)
    data = data.split("\n")
    print(data)
    for s in data:
        if number == s.split(" ")[0]:
            data.remove(s)
            break
    data = "\n".join(data)
    f = open(FILE_NAME, "w", encoding="utf8")
    f.write(data)
    f.close()



def ShowTB():
    f = open(FILE_NAME, "r", encoding="utf8")
    data = f.read()
    f.close()
    print("\n############")
    print(data)
    print("############\n")


def ChangeTB(number):
    number_n = input("Введите новый номер телефона: ")
    name_n = input("Введите новое имя: ")
    sname_n = input("Введите новую фамилию: ")
    new = number_n + " " + name_n + " " + sname_n
    f = open(FILE_NAME, "r", encoding="utf8")
    data = f.read()
    f.close()
    data = data.split("\n")
    for i in range(len(data)):
        if number == data[i].split(" ")[0]:
            data[i] = new
            break
    data = "\n".join(data)
    f = open(FILE_NAME, "w", encoding="utf8")
    f.write(data)
    f.close()



while True:
    help = "Выбери действие:\n1. Показать книгу\n2. Добавить в книгу\n3. Изменить запись\n4. Удалить запись\n5. Выйти"
    print(help)
    n = int(input("Введите номер дейтвия: "))
    if n == 1:
        ShowTB()
    elif n == 2:
        number = input("Введите номер телефона: ")
        name = input("Введите имя: ")
        sname = input("Введите фамилию: ")
        AddInTB(number, name, sname)
    elif n == 3:
        number = input("Введите номер телефона: ")
        ChangeTB(number)
    elif n == 4:
        number = input("Введите номер телефона: ")
        DelTB(number)
    elif n == 5:
        print("Закрываю книгу. Иду спать)")
        break
    else:
        print("Ой! Что-то не то скушал...")
    print("------------------")


print("Пока =)")






