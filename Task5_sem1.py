# Напишите программу, которая принимает на вход
#  координаты двух точек и находит расстояние 
# между ними в 2D пространстве.

def input_numbers(x): 
    xy = ["X", "Y"]
    list1 = []
    for i in range(x):
        correct = False
        while not correct:
            try:
                number = int(input(f"Введите координату по оси {xy[i]}: "))
                list1.append(number)
                correct = True
            except ValueError:
                print("Вы ввели не целое число")
    return list1


def Distance(a, b):  
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)  
    return lengthSegment

print("Введите координаты точки А")
pointA = input_numbers(2)
print("Введите координаты точки В")
pointB = input_numbers(2)

print(f"Расстояние между точками: {round(Distance(pointA, pointB),2)}")  