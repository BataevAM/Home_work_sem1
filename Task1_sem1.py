# Напишите программу, которая принимает на вход
#  цифру, обозначающую день недели, и проверяет,
#  является ли этот день выходным.

day = int(input('Введите номер дня недели: '))
if day > 7 or day < 1:
    print('Попробуйте еще раз. Введите цифру от 1 до 7 !')
elif day == 6 or day == 7:
    print("Ура, это выходной!")
else:
    print("Нет:( это рабочий день!")